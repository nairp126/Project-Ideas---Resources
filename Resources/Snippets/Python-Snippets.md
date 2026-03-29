# Python Snippets

A collection of reusable Python code snippets for common patterns. Copy and adapt these into your projects to avoid rewriting boilerplate.

## Table of Contents

- [Authentication Patterns](#authentication-patterns)
- [API Request Patterns](#api-request-patterns)
- [Database Connection Patterns](#database-connection-patterns)
- [Sorting and Searching](#sorting-and-searching)
- [String Manipulation](#string-manipulation)

---

## Authentication Patterns

### Password Hashing with bcrypt

Hash a plain-text password before storing it, and verify a login attempt against the stored hash. Requires `bcrypt` (`pip install bcrypt`).

```python
import bcrypt

def hash_password(plain_text: str) -> bytes:
    """Hash a password for storage."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_text.encode("utf-8"), salt)

def verify_password(plain_text: str, hashed: bytes) -> bool:
    """Return True if the plain-text password matches the stored hash."""
    return bcrypt.checkpw(plain_text.encode("utf-8"), hashed)

# Usage
hashed = hash_password("my_secret_password")
print(verify_password("my_secret_password", hashed))   # True
print(verify_password("wrong_password", hashed))        # False
```

### JWT Token Generation and Verification

Create and validate JSON Web Tokens for stateless API authentication. Requires `PyJWT` (`pip install PyJWT`).

```python
import jwt
import datetime

SECRET_KEY = "your-secret-key"  # Store in environment variable in production
ALGORITHM = "HS256"

def create_access_token(user_id: int, expires_minutes: int = 30) -> str:
    """Generate a signed JWT access token."""
    payload = {
        "sub": str(user_id),
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_minutes),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    """Decode and validate a JWT. Raises jwt.ExpiredSignatureError or jwt.InvalidTokenError on failure."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

# Usage
token = create_access_token(user_id=42)
data = decode_access_token(token)
print(data["sub"])  # "42"
```

### OAuth2 Bearer Token Header Helper

Build the Authorization header required by most OAuth2-protected APIs, and refresh the token when it expires.

```python
import time
import requests

class BearerTokenSession:
    """Wraps requests.Session with automatic Bearer token injection and refresh."""

    def __init__(self, token_url: str, client_id: str, client_secret: str):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self._token: str | None = None
        self._expires_at: float = 0

    def _fetch_token(self) -> None:
        resp = requests.post(
            self.token_url,
            data={"grant_type": "client_credentials"},
            auth=(self.client_id, self.client_secret),
            timeout=10,
        )
        resp.raise_for_status()
        body = resp.json()
        self._token = body["access_token"]
        self._expires_at = time.time() + body.get("expires_in", 3600) - 60  # 60s buffer

    @property
    def headers(self) -> dict:
        if not self._token or time.time() >= self._expires_at:
            self._fetch_token()
        return {"Authorization": f"Bearer {self._token}"}

# Usage
session = BearerTokenSession("https://auth.example.com/token", "client_id", "client_secret")
response = requests.get("https://api.example.com/data", headers=session.headers)
```

---

## API Request Patterns

### HTTP GET with Retry and Exponential Back-off

Retry failed requests with increasing delays to handle transient network errors. Requires `requests` (`pip install requests`).

```python
import time
import requests
from requests.exceptions import RequestException

def get_with_retry(url: str, max_retries: int = 3, backoff_factor: float = 0.5, **kwargs) -> requests.Response:
    """
    Perform a GET request, retrying on 5xx errors or network failures.
    Waits backoff_factor * (2 ** attempt) seconds between retries.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10, **kwargs)
            if response.status_code < 500:
                response.raise_for_status()
                return response
        except RequestException as exc:
            if attempt == max_retries - 1:
                raise
            wait = backoff_factor * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed ({exc}). Retrying in {wait}s...")
            time.sleep(wait)
    raise RuntimeError("Unreachable")

# Usage
data = get_with_retry("https://api.example.com/users", headers={"Accept": "application/json"})
print(data.json())
```

### Paginated API Fetcher

Automatically follow cursor- or page-based pagination and collect all results into a single list.

```python
import requests

def fetch_all_pages(base_url: str, params: dict | None = None, page_key: str = "page") -> list:
    """
    Fetch every page of a paginated REST API.
    Assumes the response JSON has a 'results' list and a 'next' URL (or None when done).
    """
    params = params or {}
    results = []
    url = base_url

    while url:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        body = response.json()
        results.extend(body.get("results", []))
        url = body.get("next")   # None signals the last page
        params = {}              # 'next' URL already contains query params

    return results

# Usage
all_users = fetch_all_pages("https://api.example.com/users", params={"page_size": 100})
print(f"Fetched {len(all_users)} users")
```

### Async HTTP Requests with aiohttp

Fire multiple API calls concurrently using asyncio to dramatically reduce total wait time. Requires `aiohttp` (`pip install aiohttp`).

```python
import asyncio
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch a single URL and return parsed JSON."""
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
        response.raise_for_status()
        return await response.json()

async def fetch_all(urls: list[str]) -> list[dict]:
    """Fetch all URLs concurrently and return results in order."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 6)]
results = asyncio.run(fetch_all(urls))
for post in results:
    print(post["title"])
```

---

## Database Connection Patterns

### SQLite Connection with Context Manager

Open a SQLite database, run queries safely inside a context manager, and ensure the connection is always closed.

```python
import sqlite3
from contextlib import contextmanager

DB_PATH = "app.db"

@contextmanager
def get_db():
    """Yield a SQLite connection and commit/rollback automatically."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Access columns by name
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def create_tables():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

def insert_user(name: str, email: str) -> int:
    with get_db() as conn:
        cursor = conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        return cursor.lastrowid

# Usage
create_tables()
user_id = insert_user("Alice", "alice@example.com")
print(f"Created user {user_id}")
```

### PostgreSQL Connection Pool with psycopg2

Use a connection pool to efficiently share database connections across threads. Requires `psycopg2-binary` (`pip install psycopg2-binary`).

```python
import psycopg2
from psycopg2 import pool

DATABASE_URL = "postgresql://user:password@localhost:5432/mydb"

# Create a thread-safe connection pool (min 2, max 10 connections)
connection_pool = psycopg2.pool.ThreadedConnectionPool(
    minconn=2,
    maxconn=10,
    dsn=DATABASE_URL,
)

def query(sql: str, params: tuple = ()) -> list[dict]:
    """Execute a SELECT query and return rows as a list of dicts."""
    conn = connection_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in cur.fetchall()]
    finally:
        connection_pool.putconn(conn)

# Usage
users = query("SELECT id, name FROM users WHERE email = %s", ("alice@example.com",))
print(users)
```

### SQLAlchemy ORM Session Factory

Set up SQLAlchemy with a session factory for clean, ORM-based database access that works with any supported backend.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

DATABASE_URL = "sqlite:///app.db"  # Swap for postgresql://... in production

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True, index=True)
    name  = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

Base.metadata.create_all(engine)

def get_session() -> Session:
    """Return a new database session. Caller is responsible for closing it."""
    return SessionLocal()

# Usage
with get_session() as session:
    new_user = User(name="Bob", email="bob@example.com")
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    print(new_user.id)
```

---

## Sorting and Searching

### Binary Search

Efficiently locate a target value in a sorted list in O(log n) time, returning its index or -1 if not found.

```python
def binary_search(arr: list, target) -> int:
    """
    Return the index of target in a sorted list, or -1 if not present.
    Time: O(log n) | Space: O(1)
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Usage
numbers = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numbers, 7))   # 3
print(binary_search(numbers, 6))   # -1
```

### Merge Sort

Sort a list using the divide-and-conquer merge sort algorithm, which guarantees O(n log n) performance.

```python
def merge_sort(arr: list) -> list:
    """
    Return a new sorted list using merge sort.
    Time: O(n log n) | Space: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)

def _merge(left: list, right: list) -> list:
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Usage
unsorted = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(unsorted))  # [3, 9, 10, 27, 38, 43, 82]
```

### Sort a List of Dicts by Multiple Keys

Sort a collection of records by multiple fields with mixed sort directions — a common need when displaying tabular data.

```python
from operator import itemgetter

def sort_records(records: list[dict], *keys: str, reverse: bool = False) -> list[dict]:
    """
    Sort a list of dicts by one or more keys.
    Prefix a key with '-' to sort that field in descending order.
    """
    def sort_key(record):
        return tuple(
            (-record[k[1:]] if k.startswith("-") else record[k])
            for k in keys
        )
    return sorted(records, key=sort_key, reverse=reverse)

# Usage
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 95000},
    {"name": "Bob",   "dept": "Marketing",   "salary": 72000},
    {"name": "Carol", "dept": "Engineering", "salary": 88000},
]

# Sort by department ascending, then salary descending
sorted_employees = sort_records(employees, "dept", "-salary")
for e in sorted_employees:
    print(e["name"], e["dept"], e["salary"])
```

---

## String Manipulation

### Slugify a String

Convert an arbitrary string into a URL-safe slug (e.g., for blog post URLs or file names).

```python
import re
import unicodedata

def slugify(text: str) -> str:
    """
    Convert text to a lowercase, hyphen-separated URL slug.
    Handles Unicode characters, punctuation, and extra whitespace.
    """
    # Normalize unicode (e.g., é -> e)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)       # Remove non-word chars
    text = re.sub(r"[\s_]+", "-", text)         # Replace spaces/underscores with hyphens
    text = re.sub(r"-{2,}", "-", text)          # Collapse multiple hyphens
    return text.strip("-")

# Usage
print(slugify("Hello, World!"))              # "hello-world"
print(slugify("  Python 3.11 -- What's New?"))  # "python-311-whats-new"
```

### Extract and Validate Email Addresses

Parse a block of text to find all email addresses, then validate each one against a stricter pattern.

```python
import re

EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
)

def extract_emails(text: str) -> list[str]:
    """Return all email-like strings found in text."""
    return EMAIL_PATTERN.findall(text)

def is_valid_email(email: str) -> bool:
    """Return True if the string is a well-formed email address."""
    return bool(EMAIL_PATTERN.fullmatch(email))

# Usage
body = "Contact us at support@example.com or sales@company.co.uk for help."
print(extract_emails(body))           # ['support@example.com', 'sales@company.co.uk']
print(is_valid_email("bad@"))         # False
print(is_valid_email("good@test.io")) # True
```

### Truncate Text with Ellipsis

Shorten a string to a maximum length without cutting words in the middle — useful for UI previews and notifications.

```python
def truncate(text: str, max_length: int, ellipsis: str = "...") -> str:
    """
    Truncate text to max_length characters without breaking words.
    Appends ellipsis if the text was shortened.
    """
    if len(text) <= max_length:
        return text
    truncated = text[: max_length - len(ellipsis)].rsplit(" ", 1)[0]
    return truncated + ellipsis

# Usage
long_text = "The quick brown fox jumps over the lazy dog"
print(truncate(long_text, 20))   # "The quick brown..."
print(truncate(long_text, 100))  # (unchanged)
```
