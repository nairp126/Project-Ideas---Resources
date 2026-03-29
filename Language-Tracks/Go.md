# Go Projects

**Language Version:** Go 1.21+

A collection of project ideas for Go learners, from beginner CLI tools to intermediate networked services.

---

## Beginner

### 1. URL Shortener CLI
**Language Version:** Go 1.21+
**Description:** Build a command-line URL shortener that generates a short alphanumeric code for any URL the user provides. Store the mappings in a local JSON file. Support `shorten`, `expand`, and `list` subcommands.
**Key Concepts:** os/exec, encoding/json, flag package, maps, file I/O, string generation with math/rand
**Bonus:** Add an expiry date to shortened URLs and a `cleanup` command that removes expired entries.

---

### 2. Static Site Generator
**Language Version:** Go 1.21+
**Description:** Write a tool that reads Markdown files from an `input/` directory, converts them to HTML using a template, and writes the output to an `output/` directory. Support a simple front-matter format (title, date) parsed from the top of each file.
**Key Concepts:** os.ReadDir, text/template, html/template, strings.TrimPrefix, bufio.Scanner, filepath.Walk
**Bonus:** Add a `--watch` flag that monitors the input directory for changes and regenerates affected pages automatically using fsnotify.

---

### 3. Port Scanner
**Language Version:** Go 1.21+
**Description:** Create a concurrent TCP port scanner that checks a range of ports on a given host and reports which ports are open. Use goroutines and a worker pool to scan multiple ports simultaneously.
**Key Concepts:** goroutines, channels, sync.WaitGroup, net.DialTimeout, worker pool pattern, time.Duration
**Bonus:** Add banner grabbing — for each open port, attempt to read the first response bytes to identify the service running on that port.

---

### 4. CSV Data Processor
**Language Version:** Go 1.21+
**Description:** Build a CLI tool that reads a CSV file, applies user-specified transformations (filter rows by column value, select specific columns, sort by a column), and writes the result to a new CSV file or prints it to stdout.
**Key Concepts:** encoding/csv, os.Args, slices, sort.Slice, error handling with fmt.Errorf and %w, io.Reader/Writer interfaces
**Bonus:** Add a `--aggregate` flag that groups rows by a column and computes sum/average/count for a numeric column.

---

### 5. Key-Value Store CLI
**Language Version:** Go 1.21+
**Description:** Implement a simple persistent key-value store with a CLI interface. Support `set key value`, `get key`, `delete key`, and `list` commands. Persist data to a file using a simple append-only log format.
**Key Concepts:** bufio.Scanner, os.OpenFile with append flags, string splitting, map for in-memory index, init function for loading state
**Bonus:** Add a `compact` command that rewrites the log file removing superseded entries to reclaim disk space.

---

## Intermediate

### 1. REST API with Gin and PostgreSQL
**Language Version:** Go 1.21+
**Description:** Build a RESTful API for a recipe management app using the Gin web framework. Users can create, read, update, and delete recipes. Each recipe has a title, ingredients list, steps, and tags. Use pgx to connect to PostgreSQL and implement JWT-based authentication.
**Key Concepts:** Gin router and middleware, pgx/v5, database/sql, JWT with golang-jwt/jwt, struct tags, context propagation, graceful shutdown
**Bonus:** Add a full-text search endpoint that queries PostgreSQL's tsvector index on recipe titles and ingredients.

---

### 2. gRPC Microservice
**Language Version:** Go 1.21+
**Description:** Design and implement a gRPC-based currency conversion service. Define the service in a .proto file with a `Convert` RPC and a `StreamRates` server-streaming RPC. Implement the server, a CLI client, and a simple rate-limiting interceptor.
**Key Concepts:** Protocol Buffers, google.golang.org/grpc, server and client interceptors, server-side streaming, protoc code generation, context deadlines
**Bonus:** Add mutual TLS authentication between the client and server using self-signed certificates generated with the crypto/tls package.

---

### 3. Distributed Task Queue
**Language Version:** Go 1.21+
**Description:** Build a lightweight distributed task queue where producers submit jobs (defined as JSON payloads) and worker processes pick them up and execute them. Use Redis as the broker via the go-redis client. Support job retries, priority levels, and a dead-letter queue for permanently failed jobs.
**Key Concepts:** go-redis/v9, goroutines, context cancellation, JSON marshaling, atomic operations with Redis INCR, graceful shutdown with os/signal
**Bonus:** Add a web dashboard (using net/http and html/template) that shows queue depth, worker status, and recent job history in real time using Server-Sent Events.
