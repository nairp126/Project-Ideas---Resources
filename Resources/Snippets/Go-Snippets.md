# Go Snippets

A collection of reusable Go code snippets for common patterns. Copy and adapt these into your projects to avoid rewriting boilerplate. All snippets target Go 1.21+.

## Table of Contents

- [Authentication Patterns](#authentication-patterns)
- [API Request Patterns](#api-request-patterns)
- [Database Connection Patterns](#database-connection-patterns)
- [Sorting and Searching](#sorting-and-searching)
- [String Manipulation](#string-manipulation)

---

## Authentication Patterns

### Password Hashing with bcrypt

Hash a plain-text password before storing it, and verify a login attempt against the stored hash. Uses `golang.org/x/crypto/bcrypt` (`go get golang.org/x/crypto`).

```go
package auth

import (
    "errors"
    "golang.org/x/crypto/bcrypt"
)

const bcryptCost = 12

// HashPassword hashes a plain-text password using bcrypt.
func HashPassword(password string) (string, error) {
    bytes, err := bcrypt.GenerateFromPassword([]byte(password), bcryptCost)
    if err != nil {
        return "", err
    }
    return string(bytes), nil
}

// CheckPassword returns nil if the plain-text password matches the stored hash.
func CheckPassword(password, hash string) error {
    err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
    if errors.Is(err, bcrypt.ErrMismatchedHashAndPassword) {
        return errors.New("invalid credentials")
    }
    return err
}

// Usage
// hash, _ := HashPassword("my_secret_password")
// err := CheckPassword("my_secret_password", hash) // nil
// err  = CheckPassword("wrong_password", hash)     // "invalid credentials"
```

### JWT Token Generation and Verification

Create and validate JSON Web Tokens for stateless API authentication. Uses `github.com/golang-jwt/jwt/v5` (`go get github.com/golang-jwt/jwt/v5`).

```go
package auth

import (
    "errors"
    "time"

    "github.com/golang-jwt/jwt/v5"
)

var secretKey = []byte("your-secret-key") // Store in environment variable in production

type Claims struct {
    UserID int64 `json:"user_id"`
    jwt.RegisteredClaims
}

// CreateToken generates a signed JWT access token that expires after the given duration.
func CreateToken(userID int64, expiry time.Duration) (string, error) {
    claims := Claims{
        UserID: userID,
        RegisteredClaims: jwt.RegisteredClaims{
            IssuedAt:  jwt.NewNumericDate(time.Now()),
            ExpiresAt: jwt.NewNumericDate(time.Now().Add(expiry)),
        },
    }
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(secretKey)
}

// ParseToken validates a JWT string and returns the embedded claims.
func ParseToken(tokenStr string) (*Claims, error) {
    token, err := jwt.ParseWithClaims(tokenStr, &Claims{}, func(t *jwt.Token) (any, error) {
        if _, ok := t.Method.(*jwt.SigningMethodHMAC); !ok {
            return nil, errors.New("unexpected signing method")
        }
        return secretKey, nil
    })
    if err != nil {
        return nil, err
    }
    claims, ok := token.Claims.(*Claims)
    if !ok || !token.Valid {
        return nil, errors.New("invalid token")
    }
    return claims, nil
}

// Usage
// tokenStr, _ := CreateToken(42, 30*time.Minute)
// claims, err := ParseToken(tokenStr)
// fmt.Println(claims.UserID) // 42
```

### HTTP Middleware for Bearer Token Authentication

Protect HTTP handler routes by validating the Authorization header before passing the request downstream.

```go
package middleware

import (
    "context"
    "net/http"
    "strings"
)

type contextKey string

const contextKeyUserID contextKey = "userID"

// BearerAuth wraps an http.Handler and rejects requests without a valid Bearer token.
// validateToken should return (userID, nil) on success or ("", error) on failure.
func BearerAuth(next http.Handler, validateToken func(token string) (string, error)) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        authHeader := r.Header.Get("Authorization")
        if !strings.HasPrefix(authHeader, "Bearer ") {
            http.Error(w, "missing or malformed Authorization header", http.StatusUnauthorized)
            return
        }

        token := strings.TrimPrefix(authHeader, "Bearer ")
        userID, err := validateToken(token)
        if err != nil {
            http.Error(w, "invalid or expired token", http.StatusUnauthorized)
            return
        }

        ctx := context.WithValue(r.Context(), contextKeyUserID, userID)
        next.ServeHTTP(w, r.WithContext(ctx))
    })
}
```

---

## API Request Patterns

### HTTP GET with Retry and Exponential Back-off

Retry failed requests with increasing delays to handle transient network errors. Uses the standard `net/http` package.

```go
package httpclient

import (
    "fmt"
    "net/http"
    "time"
)

// GetWithRetry performs a GET request, retrying on 5xx responses or network errors.
// It waits baseDelay * 2^attempt between retries.
func GetWithRetry(url string, maxRetries int, baseDelay time.Duration) (*http.Response, error) {
    client := &http.Client{Timeout: 10 * time.Second}

    var lastErr error
    for attempt := range maxRetries {
        resp, err := client.Get(url)
        if err == nil && resp.StatusCode < 500 {
            return resp, nil
        }
        if err == nil {
            resp.Body.Close()
            lastErr = fmt.Errorf("server error: %d", resp.StatusCode)
        } else {
            lastErr = err
        }

        wait := baseDelay * (1 << attempt)
        fmt.Printf("Attempt %d failed (%v). Retrying in %v...\n", attempt+1, lastErr, wait)
        time.Sleep(wait)
    }
    return nil, fmt.Errorf("all %d attempts failed: %w", maxRetries, lastErr)
}

// Usage
// resp, err := GetWithRetry("https://api.example.com/users", 3, 500*time.Millisecond)
// if err != nil { log.Fatal(err) }
// defer resp.Body.Close()
```

### JSON API Client with Generic Response Decoding

Send a GET request to a JSON API and decode the response body directly into a typed Go struct using generics.

```go
package httpclient

import (
    "encoding/json"
    "fmt"
    "net/http"
    "time"
)

var defaultClient = &http.Client{Timeout: 10 * time.Second}

// GetJSON fetches a URL and decodes the JSON response body into the target type T.
func GetJSON[T any](url string, headers map[string]string) (T, error) {
    var zero T
    req, err := http.NewRequest(http.MethodGet, url, nil)
    if err != nil {
        return zero, err
    }
    req.Header.Set("Accept", "application/json")
    for k, v := range headers {
        req.Header.Set(k, v)
    }

    resp, err := defaultClient.Do(req)
    if err != nil {
        return zero, err
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        return zero, fmt.Errorf("unexpected status: %d", resp.StatusCode)
    }

    var result T
    if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
        return zero, err
    }
    return result, nil
}

// Usage
// type Post struct { ID int `json:"id"`; Title string `json:"title"` }
// post, err := GetJSON[Post]("https://jsonplaceholder.typicode.com/posts/1", nil)
// fmt.Println(post.Title)
```

### Paginated API Fetcher

Automatically follow cursor- or page-based pagination and collect all results into a single slice.

```go
package httpclient

import (
    "encoding/json"
    "fmt"
    "net/http"
)

type PagedResponse[T any] struct {
    Results []T    `json:"results"`
    Next    string `json:"next"` // Empty string signals last page
}

// FetchAllPages collects every page of a paginated REST API into a single slice.
func FetchAllPages[T any](baseURL string, pageSize int) ([]T, error) {
    client := &http.Client{}
    var all []T

    nextURL := fmt.Sprintf("%s?page_size=%d", baseURL, pageSize)
    for nextURL != "" {
        resp, err := client.Get(nextURL)
        if err != nil {
            return nil, err
        }
        defer resp.Body.Close()

        var page PagedResponse[T]
        if err := json.NewDecoder(resp.Body).Decode(&page); err != nil {
            return nil, err
        }
        all = append(all, page.Results...)
        nextURL = page.Next
    }
    return all, nil
}

// Usage
// type User struct { ID int `json:"id"`; Name string `json:"name"` }
// users, err := FetchAllPages[User]("https://api.example.com/users", 100)
// fmt.Printf("Fetched %d users\n", len(users))
```

---

## Database Connection Patterns

### SQLite with database/sql

Open a SQLite database using the standard `database/sql` interface and run queries safely. Uses `github.com/mattn/go-sqlite3` (`go get github.com/mattn/go-sqlite3`).

```go
package db

import (
    "database/sql"
    "fmt"

    _ "github.com/mattn/go-sqlite3"
)

// OpenSQLite opens (or creates) a SQLite database file and verifies connectivity.
func OpenSQLite(path string) (*sql.DB, error) {
    db, err := sql.Open("sqlite3", path)
    if err != nil {
        return nil, fmt.Errorf("open sqlite: %w", err)
    }
    if err := db.Ping(); err != nil {
        return nil, fmt.Errorf("ping sqlite: %w", err)
    }
    return db, nil
}

// CreateUsersTable creates the users table if it does not already exist.
func CreateUsersTable(db *sql.DB) error {
    _, err := db.Exec(`
        CREATE TABLE IF NOT EXISTS users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    `)
    return err
}

// InsertUser inserts a new user and returns the generated ID.
func InsertUser(db *sql.DB, name, email string) (int64, error) {
    result, err := db.Exec("INSERT INTO users (name, email) VALUES (?, ?)", name, email)
    if err != nil {
        return 0, err
    }
    return result.LastInsertId()
}

// Usage
// db, _ := OpenSQLite("app.db")
// defer db.Close()
// CreateUsersTable(db)
// id, _ := InsertUser(db, "Alice", "alice@example.com")
```

### PostgreSQL Connection Pool with pgx

Use `pgxpool` to efficiently share PostgreSQL connections across goroutines. Uses `github.com/jackc/pgx/v5` (`go get github.com/jackc/pgx/v5`).

```go
package db

import (
    "context"
    "fmt"

    "github.com/jackc/pgx/v5/pgxpool"
)

// NewPostgresPool creates a connection pool for PostgreSQL.
// connStr format: "postgres://user:password@localhost:5432/mydb"
func NewPostgresPool(ctx context.Context, connStr string) (*pgxpool.Pool, error) {
    config, err := pgxpool.ParseConfig(connStr)
    if err != nil {
        return nil, fmt.Errorf("parse config: %w", err)
    }
    config.MaxConns = 10

    pool, err := pgxpool.NewWithConfig(ctx, config)
    if err != nil {
        return nil, fmt.Errorf("create pool: %w", err)
    }
    if err := pool.Ping(ctx); err != nil {
        return nil, fmt.Errorf("ping postgres: %w", err)
    }
    return pool, nil
}

// QueryUsers fetches all users and returns them as a slice of maps.
func QueryUsers(ctx context.Context, pool *pgxpool.Pool) ([]map[string]any, error) {
    rows, err := pool.Query(ctx, "SELECT id, name, email FROM users")
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    var users []map[string]any
    for rows.Next() {
        var id int64
        var name, email string
        if err := rows.Scan(&id, &name, &email); err != nil {
            return nil, err
        }
        users = append(users, map[string]any{"id": id, "name": name, "email": email})
    }
    return users, rows.Err()
}
```

### Transaction Helper

Wrap multiple SQL statements in a transaction that automatically commits on success and rolls back on any error.

```go
package db

import (
    "context"
    "database/sql"
    "fmt"
)

// WithTx runs fn inside a database transaction.
// It commits if fn returns nil, or rolls back and returns the error otherwise.
func WithTx(ctx context.Context, db *sql.DB, fn func(tx *sql.Tx) error) error {
    tx, err := db.BeginTx(ctx, nil)
    if err != nil {
        return fmt.Errorf("begin tx: %w", err)
    }

    if err := fn(tx); err != nil {
        _ = tx.Rollback()
        return err
    }
    return tx.Commit()
}

// Usage
// err := WithTx(ctx, db, func(tx *sql.Tx) error {
//     if _, err := tx.ExecContext(ctx, "UPDATE accounts SET balance = balance - $1 WHERE id = $2", 100, fromID); err != nil {
//         return err
//     }
//     _, err := tx.ExecContext(ctx, "UPDATE accounts SET balance = balance + $1 WHERE id = $2", 100, toID)
//     return err
// })
```

---

## Sorting and Searching

### Binary Search

Efficiently locate a target value in a sorted slice in O(log n) time using the standard library's `sort.Search`.

```go
package search

import "sort"

// BinarySearch returns the index of target in a sorted int slice, or -1 if not found.
// Time: O(log n) | Space: O(1)
func BinarySearch(sorted []int, target int) int {
    n := len(sorted)
    idx := sort.Search(n, func(i int) bool { return sorted[i] >= target })
    if idx < n && sorted[idx] == target {
        return idx
    }
    return -1
}

// Usage
// numbers := []int{1, 3, 5, 7, 9, 11, 13}
// fmt.Println(BinarySearch(numbers, 7))  // 3
// fmt.Println(BinarySearch(numbers, 6))  // -1
```

### Sort a Slice of Structs by Multiple Fields

Sort a collection of records by multiple fields with mixed sort directions using `sort.Slice`.

```go
package sorting

import "sort"

type Employee struct {
    Name   string
    Dept   string
    Salary int
}

// SortEmployees sorts employees by department ascending, then salary descending.
func SortEmployees(employees []Employee) {
    sort.Slice(employees, func(i, j int) bool {
        a, b := employees[i], employees[j]
        if a.Dept != b.Dept {
            return a.Dept < b.Dept
        }
        return a.Salary > b.Salary
    })
}

// Usage
// employees := []Employee{
//     {"Alice", "Engineering", 95000},
//     {"Bob",   "Marketing",   72000},
//     {"Carol", "Engineering", 88000},
// }
// SortEmployees(employees)
// // Result: Alice (Eng, 95k), Carol (Eng, 88k), Bob (Mkt, 72k)
```

### Merge Sort

Sort a slice using the divide-and-conquer merge sort algorithm, guaranteeing O(n log n) performance regardless of input order.

```go
package sorting

// MergeSort returns a new sorted slice using merge sort.
// Time: O(n log n) | Space: O(n)
func MergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr) / 2
    left := MergeSort(arr[:mid])
    right := MergeSort(arr[mid:])
    return mergeSorted(left, right)
}

func mergeSorted(left, right []int) []int {
    result := make([]int, 0, len(left)+len(right))
    i, j := 0, 0
    for i < len(left) && j < len(right) {
        if left[i] <= right[j] {
            result = append(result, left[i])
            i++
        } else {
            result = append(result, right[j])
            j++
        }
    }
    result = append(result, left[i:]...)
    result = append(result, right[j:]...)
    return result
}

// Usage
// unsorted := []int{38, 27, 43, 3, 9, 82, 10}
// fmt.Println(MergeSort(unsorted)) // [3 9 10 27 38 43 82]
```

---

## String Manipulation

### Slugify a String

Convert an arbitrary string into a URL-safe slug (e.g., for blog post URLs or file names). Uses the standard `strings` and `regexp` packages.

```go
package strutil

import (
    "regexp"
    "strings"
)

var (
    nonWordRe   = regexp.MustCompile(`[^\w\s-]`)
    whitespaceRe = regexp.MustCompile(`[\s_]+`)
    multiHyphen = regexp.MustCompile(`-{2,}`)
)

// Slugify converts text to a lowercase, hyphen-separated URL slug.
func Slugify(text string) string {
    text = strings.ToLower(text)
    text = nonWordRe.ReplaceAllString(text, "")
    text = whitespaceRe.ReplaceAllString(text, "-")
    text = multiHyphen.ReplaceAllString(text, "-")
    return strings.Trim(text, "-")
}

// Usage
// fmt.Println(Slugify("Hello, World!"))            // "hello-world"
// fmt.Println(Slugify("  Go 1.21 -- What's New?")) // "go-121-whats-new"
```

### Extract and Validate Email Addresses

Parse a block of text to find all email addresses, then validate each one against a stricter pattern.

```go
package strutil

import "regexp"

var emailRe = regexp.MustCompile(`[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}`)

// ExtractEmails returns all email-like strings found in text.
func ExtractEmails(text string) []string {
    return emailRe.FindAllString(text, -1)
}

// IsValidEmail returns true if the string is a well-formed email address.
func IsValidEmail(email string) bool {
    match := emailRe.FindString(email)
    return match == email
}

// Usage
// body := "Contact us at support@example.com or sales@company.co.uk for help."
// fmt.Println(ExtractEmails(body))           // [support@example.com sales@company.co.uk]
// fmt.Println(IsValidEmail("bad@"))          // false
// fmt.Println(IsValidEmail("good@test.io"))  // true
```

### Truncate Text with Ellipsis

Shorten a string to a maximum rune count without cutting words in the middle — useful for UI previews and notifications.

```go
package strutil

import "strings"

// Truncate shortens text to maxLen runes without breaking words.
// Appends ellipsis if the text was shortened.
func Truncate(text string, maxLen int, ellipsis string) string {
    runes := []rune(text)
    if len(runes) <= maxLen {
        return text
    }
    cutoff := maxLen - len([]rune(ellipsis))
    truncated := string(runes[:cutoff])
    if idx := strings.LastIndex(truncated, " "); idx > 0 {
        truncated = truncated[:idx]
    }
    return truncated + ellipsis
}

// Usage
// long := "The quick brown fox jumps over the lazy dog"
// fmt.Println(Truncate(long, 20, "..."))  // "The quick brown..."
// fmt.Println(Truncate(long, 100, "...")) // (unchanged)
```
