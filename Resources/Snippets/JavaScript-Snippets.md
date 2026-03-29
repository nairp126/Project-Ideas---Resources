# JavaScript Snippets

A collection of reusable JavaScript code snippets for common patterns. Copy and adapt these into your projects to avoid rewriting boilerplate. All examples use modern JavaScript (ES2020+, Node.js 18+).

## Table of Contents

- [Authentication Patterns](#authentication-patterns)
- [API Request Patterns](#api-request-patterns)
- [Database Connection Patterns](#database-connection-patterns)
- [Sorting and Searching](#sorting-and-searching)
- [String Manipulation](#string-manipulation)

---

## Authentication Patterns

### Password Hashing with bcryptjs

Hash a plain-text password before storing it, and verify a login attempt against the stored hash. Requires `bcryptjs` (`npm install bcryptjs`).

```javascript
import bcrypt from 'bcryptjs';

const SALT_ROUNDS = 12;

/**
 * Hash a plain-text password for storage.
 * @param {string} plainText
 * @returns {Promise<string>} The bcrypt hash
 */
async function hashPassword(plainText) {
  return bcrypt.hash(plainText, SALT_ROUNDS);
}

/**
 * Verify a login attempt against a stored hash.
 * @param {string} plainText
 * @param {string} hash
 * @returns {Promise<boolean>}
 */
async function verifyPassword(plainText, hash) {
  return bcrypt.compare(plainText, hash);
}

// Usage
const hashed = await hashPassword('my_secret_password');
console.log(await verifyPassword('my_secret_password', hashed)); // true
console.log(await verifyPassword('wrong_password', hashed));     // false
```

### JWT Token Generation and Verification

Create and validate JSON Web Tokens for stateless API authentication. Requires `jsonwebtoken` (`npm install jsonwebtoken`).

```javascript
import jwt from 'jsonwebtoken';

const SECRET_KEY = process.env.JWT_SECRET; // Never hard-code in production
const ALGORITHM = 'HS256';

/**
 * Generate a signed JWT access token.
 * @param {number|string} userId
 * @param {number} expiresInMinutes
 * @returns {string} Signed JWT
 */
function createAccessToken(userId, expiresInMinutes = 30) {
  return jwt.sign(
    { sub: String(userId) },
    SECRET_KEY,
    { algorithm: ALGORITHM, expiresIn: `${expiresInMinutes}m` }
  );
}

/**
 * Decode and validate a JWT. Throws on expiry or invalid signature.
 * @param {string} token
 * @returns {object} Decoded payload
 */
function decodeAccessToken(token) {
  return jwt.verify(token, SECRET_KEY, { algorithms: [ALGORITHM] });
}

// Usage
const token = createAccessToken(42);
const payload = decodeAccessToken(token);
console.log(payload.sub); // "42"
```

### OAuth2 Client Credentials Token Manager

Fetch and cache an OAuth2 Bearer token using the client credentials flow, refreshing it automatically before it expires.

```javascript
/**
 * Manages an OAuth2 client credentials token with automatic refresh.
 */
class TokenManager {
  #tokenUrl;
  #clientId;
  #clientSecret;
  #token = null;
  #expiresAt = 0;

  constructor(tokenUrl, clientId, clientSecret) {
    this.#tokenUrl = tokenUrl;
    this.#clientId = clientId;
    this.#clientSecret = clientSecret;
  }

  async #fetchToken() {
    const credentials = Buffer.from(`${this.#clientId}:${this.#clientSecret}`).toString('base64');
    const res = await fetch(this.#tokenUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${credentials}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'grant_type=client_credentials',
    });
    if (!res.ok) throw new Error(`Token fetch failed: ${res.status}`);
    const body = await res.json();
    this.#token = body.access_token;
    this.#expiresAt = Date.now() + (body.expires_in ?? 3600) * 1000 - 60_000; // 60s buffer
  }

  async getAuthHeader() {
    if (!this.#token || Date.now() >= this.#expiresAt) {
      await this.#fetchToken();
    }
    return { Authorization: `Bearer ${this.#token}` };
  }
}

// Usage
const manager = new TokenManager('https://auth.example.com/token', 'client_id', 'client_secret');
const headers = await manager.getAuthHeader();
const res = await fetch('https://api.example.com/data', { headers });
```

---

## API Request Patterns

### Fetch with Retry and Exponential Back-off

Retry failed requests with increasing delays to handle transient network errors. Uses the built-in `fetch` API available in Node.js 18+.

```javascript
/**
 * Perform a fetch request, retrying on 5xx errors or network failures.
 * Waits backoffFactor * (2 ** attempt) ms between retries.
 *
 * @param {string} url
 * @param {RequestInit} options
 * @param {number} maxRetries
 * @param {number} backoffFactor - Base delay multiplier in milliseconds
 * @returns {Promise<Response>}
 */
async function fetchWithRetry(url, options = {}, maxRetries = 3, backoffFactor = 300) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const res = await fetch(url, { signal: AbortSignal.timeout(10_000), ...options });
      if (res.status < 500) return res;
      throw new Error(`Server error: ${res.status}`);
    } catch (err) {
      if (attempt === maxRetries - 1) throw err;
      const wait = backoffFactor * 2 ** attempt;
      console.warn(`Attempt ${attempt + 1} failed (${err.message}). Retrying in ${wait}ms...`);
      await new Promise(resolve => setTimeout(resolve, wait));
    }
  }
}

// Usage
const res = await fetchWithRetry('https://api.example.com/users', {
  headers: { Accept: 'application/json' },
});
const data = await res.json();
console.log(data);
```

### Paginated API Fetcher

Automatically follow cursor- or page-based pagination and collect all results into a single array.

```javascript
/**
 * Fetch every page of a paginated REST API.
 * Assumes the response JSON has a `results` array and a `next` URL (or null when done).
 *
 * @param {string} baseUrl
 * @param {Record<string, string>} params - Initial query parameters
 * @returns {Promise<Array>}
 */
async function fetchAllPages(baseUrl, params = {}) {
  const results = [];
  let url = new URL(baseUrl);

  Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));

  while (url) {
    const res = await fetch(url.toString(), { headers: { Accept: 'application/json' } });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const body = await res.json();
    results.push(...(body.results ?? []));
    url = body.next ? new URL(body.next) : null;
  }

  return results;
}

// Usage
const allUsers = await fetchAllPages('https://api.example.com/users', { page_size: '100' });
console.log(`Fetched ${allUsers.length} users`);
```

### Concurrent Requests with Promise.allSettled

Fire multiple API calls concurrently and handle both successes and failures without short-circuiting on the first error.

```javascript
/**
 * Fetch multiple URLs concurrently and return results with status.
 * Uses Promise.allSettled so one failure does not cancel the rest.
 *
 * @param {string[]} urls
 * @returns {Promise<Array<{url: string, data?: any, error?: string}>>}
 */
async function fetchConcurrent(urls) {
  const results = await Promise.allSettled(
    urls.map(url => fetch(url, { signal: AbortSignal.timeout(10_000) }).then(r => r.json()))
  );

  return results.map((result, i) => ({
    url: urls[i],
    ...(result.status === 'fulfilled'
      ? { data: result.value }
      : { error: result.reason?.message }),
  }));
}

// Usage
const urls = Array.from({ length: 5 }, (_, i) => `https://jsonplaceholder.typicode.com/posts/${i + 1}`);
const responses = await fetchConcurrent(urls);
responses.forEach(({ url, data, error }) => {
  if (error) console.error(`${url} failed: ${error}`);
  else console.log(data.title);
});
```

---

## Database Connection Patterns

### MongoDB Connection with Mongoose

Connect to MongoDB using Mongoose with a singleton pattern to reuse the connection across requests. Requires `mongoose` (`npm install mongoose`).

```javascript
import mongoose from 'mongoose';

const MONGODB_URI = process.env.MONGODB_URI; // e.g. mongodb://localhost:27017/mydb

let isConnected = false;

/**
 * Connect to MongoDB, reusing an existing connection if available.
 * Safe to call on every request in serverless environments.
 */
async function connectDB() {
  if (isConnected) return;

  await mongoose.connect(MONGODB_URI, {
    serverSelectionTimeoutMS: 5000,
    maxPoolSize: 10,
  });

  isConnected = true;
  console.log('MongoDB connected');
}

// Define a schema and model
const userSchema = new mongoose.Schema({
  name:  { type: String, required: true },
  email: { type: String, required: true, unique: true },
}, { timestamps: true });

const User = mongoose.models.User ?? mongoose.model('User', userSchema);

// Usage
await connectDB();
const user = await User.create({ name: 'Alice', email: 'alice@example.com' });
console.log(user._id);
```

### PostgreSQL Connection Pool with node-postgres

Use a connection pool to efficiently share database connections across async operations. Requires `pg` (`npm install pg`).

```javascript
import pg from 'pg';

const { Pool } = pg;

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  // e.g. postgresql://user:password@localhost:5432/mydb
  max: 10,
  idleTimeoutMillis: 30_000,
  connectionTimeoutMillis: 2_000,
});

/**
 * Execute a parameterized query and return rows.
 * @param {string} sql
 * @param {any[]} params
 * @returns {Promise<any[]>}
 */
async function query(sql, params = []) {
  const client = await pool.connect();
  try {
    const result = await client.query(sql, params);
    return result.rows;
  } finally {
    client.release();
  }
}

// Usage
const users = await query(
  'SELECT id, name FROM users WHERE email = $1',
  ['alice@example.com']
);
console.log(users);
```

### SQLite with better-sqlite3 (Synchronous)

Use better-sqlite3 for lightweight, synchronous SQLite access — ideal for CLIs, scripts, and local-first apps. Requires `better-sqlite3` (`npm install better-sqlite3`).

```javascript
import Database from 'better-sqlite3';

const db = new Database('app.db');

// Enable WAL mode for better concurrent read performance
db.pragma('journal_mode = WAL');

// Create table if it doesn't exist
db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
  )
`);

const insertUser = db.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
const getUserByEmail = db.prepare('SELECT * FROM users WHERE email = ?');

/**
 * Insert a user and return the new row id.
 * @param {string} name
 * @param {string} email
 * @returns {number}
 */
function createUser(name, email) {
  const result = insertUser.run(name, email);
  return result.lastInsertRowid;
}

// Usage
const id = createUser('Bob', 'bob@example.com');
const user = getUserByEmail.get('bob@example.com');
console.log(user); // { id: 1, name: 'Bob', email: 'bob@example.com' }
```

---

## Sorting and Searching

### Binary Search

Efficiently locate a target value in a sorted array in O(log n) time, returning its index or -1 if not found.

```javascript
/**
 * Return the index of target in a sorted array, or -1 if not present.
 * Time: O(log n) | Space: O(1)
 *
 * @param {number[]} arr - Sorted array
 * @param {number} target
 * @returns {number}
 */
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    const mid = (low + high) >>> 1; // Unsigned right shift avoids overflow
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
  }

  return -1;
}

// Usage
const numbers = [1, 3, 5, 7, 9, 11, 13];
console.log(binarySearch(numbers, 7));  // 3
console.log(binarySearch(numbers, 6));  // -1
```

### Merge Sort

Sort an array using the divide-and-conquer merge sort algorithm, which guarantees O(n log n) performance.

```javascript
/**
 * Return a new sorted array using merge sort.
 * Time: O(n log n) | Space: O(n)
 *
 * @param {number[]} arr
 * @returns {number[]}
 */
function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left, right) {
  const result = [];
  let i = 0, j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) result.push(left[i++]);
    else result.push(right[j++]);
  }

  return result.concat(left.slice(i), right.slice(j));
}

// Usage
const unsorted = [38, 27, 43, 3, 9, 82, 10];
console.log(mergeSort(unsorted)); // [3, 9, 10, 27, 38, 43, 82]
```

### Sort an Array of Objects by Multiple Keys

Sort a collection of records by multiple fields with mixed sort directions — a common need when displaying tabular data.

```javascript
/**
 * Sort an array of objects by one or more keys.
 * Prefix a key with '-' to sort that field in descending order.
 *
 * @param {object[]} records
 * @param {...string} keys
 * @returns {object[]}
 */
function sortBy(records, ...keys) {
  return [...records].sort((a, b) => {
    for (const key of keys) {
      const desc = key.startsWith('-');
      const field = desc ? key.slice(1) : key;
      const dir = desc ? -1 : 1;
      if (a[field] < b[field]) return -1 * dir;
      if (a[field] > b[field]) return 1 * dir;
    }
    return 0;
  });
}

// Usage
const employees = [
  { name: 'Alice', dept: 'Engineering', salary: 95000 },
  { name: 'Bob',   dept: 'Marketing',   salary: 72000 },
  { name: 'Carol', dept: 'Engineering', salary: 88000 },
];

// Sort by department ascending, then salary descending
const sorted = sortBy(employees, 'dept', '-salary');
sorted.forEach(e => console.log(e.name, e.dept, e.salary));
// Alice Engineering 95000
// Carol Engineering 88000
// Bob   Marketing   72000
```

---

## String Manipulation

### Slugify a String

Convert an arbitrary string into a URL-safe slug (e.g., for blog post URLs or file names).

```javascript
/**
 * Convert text to a lowercase, hyphen-separated URL slug.
 * Handles Unicode characters, punctuation, and extra whitespace.
 *
 * @param {string} text
 * @returns {string}
 */
function slugify(text) {
  return text
    .normalize('NFKD')                        // Decompose unicode (é → e + combining accent)
    .replace(/[\u0300-\u036f]/g, '')          // Strip combining diacritical marks
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')                 // Remove non-word characters
    .replace(/[\s_]+/g, '-')                  // Replace spaces/underscores with hyphens
    .replace(/-{2,}/g, '-')                   // Collapse multiple hyphens
    .replace(/^-+|-+$/g, '');                 // Trim leading/trailing hyphens
}

// Usage
console.log(slugify('Hello, World!'));                  // "hello-world"
console.log(slugify('  JavaScript ES2020 -- What\'s New?')); // "javascript-es2020-whats-new"
console.log(slugify('Ångström & Ünits'));               // "angstrom-units"
```

### Extract and Validate Email Addresses

Parse a block of text to find all email addresses, then validate each one against a stricter pattern.

```javascript
const EMAIL_PATTERN = /[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}/g;
const EMAIL_FULL = /^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$/;

/**
 * Return all email-like strings found in text.
 * @param {string} text
 * @returns {string[]}
 */
function extractEmails(text) {
  return text.match(EMAIL_PATTERN) ?? [];
}

/**
 * Return true if the string is a well-formed email address.
 * @param {string} email
 * @returns {boolean}
 */
function isValidEmail(email) {
  return EMAIL_FULL.test(email);
}

// Usage
const body = 'Contact us at support@example.com or sales@company.co.uk for help.';
console.log(extractEmails(body));           // ['support@example.com', 'sales@company.co.uk']
console.log(isValidEmail('bad@'));          // false
console.log(isValidEmail('good@test.io')); // true
```

### Truncate Text with Ellipsis

Shorten a string to a maximum length without cutting words in the middle — useful for UI previews and notifications.

```javascript
/**
 * Truncate text to maxLength characters without breaking words.
 * Appends ellipsis if the text was shortened.
 *
 * @param {string} text
 * @param {number} maxLength
 * @param {string} ellipsis
 * @returns {string}
 */
function truncate(text, maxLength, ellipsis = '...') {
  if (text.length <= maxLength) return text;
  const truncated = text.slice(0, maxLength - ellipsis.length).replace(/\s+\S*$/, '');
  return truncated + ellipsis;
}

// Usage
const longText = 'The quick brown fox jumps over the lazy dog';
console.log(truncate(longText, 20));  // "The quick brown..."
console.log(truncate(longText, 100)); // (unchanged)
```

### Template Literal Tag for Safe HTML Escaping

A tagged template literal that automatically escapes interpolated values to prevent XSS when building HTML strings.

```javascript
const ESCAPE_MAP = {
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#39;',
};

/**
 * Tagged template literal that HTML-escapes all interpolated values.
 * Use instead of string concatenation when building HTML.
 *
 * @param {TemplateStringsArray} strings
 * @param {...any} values
 * @returns {string}
 */
function html(strings, ...values) {
  const escape = str =>
    String(str).replace(/[&<>"']/g, ch => ESCAPE_MAP[ch]);

  return strings.reduce((result, str, i) =>
    result + str + (i < values.length ? escape(values[i]) : ''), '');
}

// Usage
const username = '<script>alert("xss")</script>';
const greeting = html`<p>Welcome, ${username}!</p>`;
console.log(greeting);
// <p>Welcome, &lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;!</p>
```
