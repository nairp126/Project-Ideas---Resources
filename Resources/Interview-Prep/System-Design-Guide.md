# System Design Interview Guide

## Overview

System design interviews test your ability to architect large-scale distributed systems. Unlike coding interviews, there's rarely a single correct answer — interviewers want to see how you think, communicate trade-offs, and make reasoned decisions under constraints.

**Topics covered:** Scalability, Caching, Databases, Load Balancing, API Design Patterns

**Who this is for:** Mid-level to senior engineers interviewing at companies that run distributed systems at scale (FAANG, growth-stage startups, etc.)

---

## Key Concepts

### Scalability

- **Vertical scaling (scale up):** Add more CPU/RAM to a single machine. Simple but has a hard ceiling and creates a single point of failure.
- **Horizontal scaling (scale out):** Add more machines. Requires stateless services and a load balancer. Preferred for large-scale systems.
- **Stateless services:** Each request carries all the context needed to process it. Enables any server to handle any request — critical for horizontal scaling.
- **Bottleneck identification:** Profile before optimizing. Common bottlenecks: database reads, network I/O, CPU-bound computation, lock contention.

### Caching

- **Purpose:** Reduce latency and database load by storing frequently accessed data in fast memory (RAM).
- **Cache-aside (lazy loading):** Application checks cache first; on miss, fetches from DB and populates cache. Most common pattern.
- **Write-through:** Write to cache and DB simultaneously. Keeps cache consistent but adds write latency.
- **Write-behind (write-back):** Write to cache immediately, flush to DB asynchronously. Fast writes, risk of data loss on crash.
- **Eviction policies:** LRU (Least Recently Used) is the default choice; LFU (Least Frequently Used) for access-frequency-skewed workloads.
- **Cache invalidation:** The hard problem. Strategies: TTL expiry, event-driven invalidation, versioned keys.
- **Tools:** Redis (in-memory data structures, pub/sub, persistence), Memcached (pure cache, simpler, multi-threaded).

### Databases

- **SQL (relational):** ACID guarantees, strong consistency, joins, schema enforcement. Best for transactional data (orders, payments, user accounts). Examples: PostgreSQL, MySQL.
- **NoSQL (non-relational):** Flexible schema, horizontal scaling, eventual consistency. Best for high-volume reads/writes with simple access patterns. Examples: MongoDB (document), Cassandra (wide-column), DynamoDB (key-value).
- **CAP Theorem:** A distributed system can guarantee at most two of: Consistency, Availability, Partition Tolerance. In practice, partition tolerance is required, so you choose between CP (consistent) and AP (available).
- **Replication:** Primary-replica (read scaling, failover). Multi-primary (write scaling, conflict resolution needed).
- **Sharding:** Partition data across multiple DB nodes by a shard key. Eliminates single-node write bottleneck. Challenges: cross-shard queries, rebalancing, hotspots.
- **Indexes:** Speed up reads at the cost of write overhead and storage. B-tree indexes for range queries; hash indexes for exact lookups.

### Load Balancing

- **Purpose:** Distribute incoming traffic across multiple servers to prevent overload and enable horizontal scaling.
- **Algorithms:** Round-robin (simple, even distribution), least connections (routes to least-busy server), IP hash (sticky sessions), weighted round-robin (heterogeneous servers).
- **Layer 4 vs Layer 7:** L4 (TCP/UDP) is faster but less intelligent. L7 (HTTP) can route based on URL path, headers, or content — enables features like A/B testing and canary deployments.
- **Health checks:** Load balancers periodically probe backends; unhealthy instances are removed from rotation automatically.
- **Tools:** Nginx, HAProxy, AWS ALB/NLB, Cloudflare.

### API Design Patterns

- **REST:** Resource-based URLs, stateless, HTTP verbs (GET/POST/PUT/DELETE/PATCH). Widely understood, easy to cache, good for CRUD-heavy APIs.
- **GraphQL:** Client specifies exact data shape. Eliminates over-fetching and under-fetching. Adds complexity on the server side.
- **gRPC:** Binary protocol (Protocol Buffers), strongly typed, bidirectional streaming. Best for internal service-to-service communication where performance matters.
- **Pagination:** Offset-based (simple, but slow on large offsets), cursor-based (efficient, consistent under mutations). Prefer cursor-based for feeds and large datasets.
- **Rate limiting:** Protect APIs from abuse. Algorithms: token bucket (bursty traffic), leaky bucket (smooth output), fixed window, sliding window.
- **Idempotency:** Safe to retry. GET, PUT, DELETE are idempotent by definition. POST is not — use idempotency keys for payment and order APIs.
- **Versioning:** URL versioning (`/v1/users`), header versioning (`Accept: application/vnd.api+json;version=2`). URL versioning is simpler and more visible.

### Additional Concepts

- **Message queues:** Decouple producers from consumers, enable async processing, absorb traffic spikes. Tools: Kafka (high-throughput, durable log), RabbitMQ (flexible routing, lower throughput), SQS (managed, simple).
- **CDN (Content Delivery Network):** Cache static assets at edge nodes geographically close to users. Reduces latency and origin server load.
- **Consistent hashing:** Distribute keys across nodes such that adding/removing a node only remaps a fraction of keys. Used in distributed caches and databases.
- **Circuit breaker:** Prevent cascading failures by stopping calls to a failing downstream service and returning a fallback response.
- **Back-of-the-envelope estimation:** Quickly estimate QPS, storage, bandwidth. Know: 1M users × 1 req/day ≈ 12 QPS; 1 byte × 1B = 1 GB.

---

## Example Questions

### Q1: Design a URL Shortener (e.g., bit.ly)
**Framework:** Core service + unique ID generation + redirect flow

**Answer:**
> **Requirements:** Shorten long URLs, redirect short URLs to originals, handle ~100M URLs, ~10B redirects/month.
>
> **Core components:**
> - **API:** `POST /shorten` → returns short code; `GET /{code}` → 301/302 redirect
> - **ID generation:** Base62-encode a 7-character ID. Use a distributed counter (Snowflake ID) or random ID with collision check.
> - **Storage:** SQL or key-value store mapping `short_code → original_url`. Key-value (Redis/DynamoDB) is ideal — simple access pattern, high read volume.
> - **Caching:** Cache hot short codes in Redis (LRU). ~80% of traffic hits ~20% of URLs.
> - **Redirect type:** 301 (permanent, browser caches — reduces server load) vs 302 (temporary, every redirect hits server — better for analytics).
>
> **Scale:** 10B redirects/month ≈ 3,900 QPS. A single Redis node handles ~100K QPS — easily covered with a small cluster.

---

### Q2: Design a Rate Limiter
**Framework:** Token bucket algorithm + distributed counter in Redis

**Answer:**
> **Requirements:** Limit each user to N requests per time window. Must work across multiple API servers.
>
> **Algorithm choice:** Token bucket — allows controlled bursts while enforcing an average rate. Each user has a bucket of N tokens; tokens refill at a fixed rate; each request consumes one token.
>
> **Implementation:**
> - Store `{user_id: {tokens, last_refill_time}}` in Redis.
> - Use a Lua script for atomic check-and-decrement (prevents race conditions).
> - On limit exceeded, return HTTP 429 with `Retry-After` header.
>
> **Sliding window alternative:** Store request timestamps in a Redis sorted set; count entries in the last N seconds. More accurate but higher memory usage.
>
> **Trade-off:** Fixed window is simplest but allows 2× burst at window boundaries. Sliding window is accurate but expensive. Token bucket balances both.

---

### Q3: Design a News Feed (e.g., Twitter/Facebook)
**Framework:** Fan-out on write vs fan-out on read

**Answer:**
> **Requirements:** Users follow others; see a ranked feed of recent posts from followed accounts.
>
> **Fan-out on write (push model):** When a user posts, immediately write to all followers' feed caches. Fast reads (O(1) feed fetch), but expensive writes for users with millions of followers (celebrities).
>
> **Fan-out on read (pull model):** On feed request, fetch posts from all followed accounts and merge. Simple writes, but slow reads that scale with follow count.
>
> **Hybrid (Twitter's approach):** Fan-out on write for regular users; fan-out on read for celebrities (>N followers). Merge at read time.
>
> **Storage:**
> - Posts: SQL or Cassandra (time-series access pattern)
> - Feed cache: Redis sorted set per user (score = timestamp)
> - Media: Object storage (S3) + CDN
>
> **Ranking:** Simple: reverse chronological. Complex: ML model scoring engagement signals (likes, recency, relationship strength).

---

### Q4: Design a Distributed Cache (e.g., Redis Cluster)
**Framework:** Consistent hashing + replication + eviction

**Answer:**
> **Requirements:** Low-latency key-value store, horizontally scalable, fault-tolerant.
>
> **Data partitioning:** Use consistent hashing to distribute keys across nodes. Each node owns a range of the hash ring. Adding/removing a node remaps only ~1/N of keys.
>
> **Replication:** Each primary node has 1–2 replicas. Replicas serve reads (eventual consistency) and take over on primary failure.
>
> **Eviction:** LRU by default. Configure `maxmemory-policy` based on workload (allkeys-lru, volatile-lru, etc.).
>
> **Consistency trade-off:** Redis replication is asynchronous — a primary crash before replication completes can lose recent writes. For strong consistency, use synchronous replication (higher latency) or accept the trade-off.
>
> **Cache stampede prevention:** When a hot key expires, many requests simultaneously hit the DB. Solutions: probabilistic early expiration, mutex lock on cache miss, background refresh.

---

### Q5: Design a Ride-Sharing Service (e.g., Uber)
**Framework:** Location tracking + matching + trip lifecycle

**Answer:**
> **Requirements:** Riders request rides; drivers accept; real-time location tracking; ETA calculation.
>
> **Location service:** Drivers send GPS updates every 4 seconds. Store in Redis geospatial index (`GEOADD`/`GEORADIUS`) for fast proximity queries. Persist to Cassandra for trip history.
>
> **Matching service:** On ride request, query nearby available drivers within radius R. Rank by ETA (not just distance). Offer to closest driver; if declined, offer to next.
>
> **Trip state machine:** `REQUESTED → ACCEPTED → DRIVER_EN_ROUTE → TRIP_IN_PROGRESS → COMPLETED`. Use a message queue (Kafka) to propagate state changes to relevant services (notifications, billing, analytics).
>
> **Surge pricing:** Compute supply/demand ratio per geohash cell. Multiply base fare by surge multiplier. Update every 1–5 minutes.
>
> **Scale:** 1M concurrent drivers sending updates every 4s = 250K writes/sec. Redis handles this; Cassandra handles the durable write-behind.

---

### Q6: Design a Search Autocomplete System
**Framework:** Trie + top-k suggestions + caching

**Answer:**
> **Requirements:** Return top 5 search suggestions as user types, < 100ms latency.
>
> **Data structure:** Trie where each node stores the top-k most frequent completions for that prefix. Precomputed at index time.
>
> **Storage:** For large datasets, store the trie in a distributed key-value store (prefix → top-k list). Redis is ideal — prefix as key, sorted set as value (score = frequency).
>
> **Update pipeline:** Log search queries → batch aggregate frequencies (Spark/Flink) → update trie/Redis periodically (every hour or day). Real-time updates for trending queries via a streaming pipeline.
>
> **Caching:** Cache top-k results for common prefixes at the CDN edge. Most queries are short prefixes with high repetition.
>
> **Personalization:** Blend global frequency with user's personal search history. Weight recent queries higher.

---

### Q7: Design a Notification System
**Framework:** Event-driven pipeline + multi-channel delivery + deduplication

**Answer:**
> **Requirements:** Send push, email, and SMS notifications reliably; support millions of users; avoid duplicate delivery.
>
> **Architecture:**
> - **Event producers:** Any service publishes events to Kafka (e.g., `order.shipped`, `friend.request`).
> - **Notification service:** Consumes events, applies user preferences (opted out? correct channel?), and routes to channel workers.
> - **Channel workers:** Separate services for push (APNs/FCM), email (SendGrid/SES), SMS (Twilio). Each has its own queue.
>
> **Reliability:** Use at-least-once delivery with idempotency keys to prevent duplicates. Store notification state in DB; mark as `SENT` after successful delivery.
>
> **Rate limiting:** Respect per-user notification frequency caps to avoid spam. Aggregate low-priority notifications into digests.
>
> **Failure handling:** Retry with exponential backoff. Dead-letter queue for permanently failed notifications. Alert on DLQ depth.

---

### Q8: Design a File Storage Service (e.g., Dropbox/Google Drive)
**Framework:** Chunked upload + metadata service + sync protocol

**Answer:**
> **Requirements:** Upload/download files, sync across devices, share with others, handle large files.
>
> **Chunking:** Split files into fixed-size chunks (e.g., 4 MB). Upload chunks in parallel. Only re-upload changed chunks on sync (delta sync). Hash each chunk (SHA-256) for deduplication.
>
> **Storage:** Chunks → object storage (S3). Metadata (file name, path, chunk list, version) → SQL database. Deduplication: if chunk hash already exists, skip upload.
>
> **Sync protocol:** Client maintains a local index. On change, compute diff, upload new/modified chunks, update metadata. Server pushes change notifications via WebSocket or long-polling.
>
> **Conflict resolution:** Last-write-wins for simple cases. Create conflict copies (like Dropbox) when concurrent edits are detected.
>
> **Access control:** Per-file/folder ACLs stored in DB. Pre-signed S3 URLs for time-limited direct downloads (avoids proxying large files through app servers).

---

### Q9: Design a Distributed Message Queue (e.g., Kafka)
**Framework:** Log-based storage + partitioning + consumer groups

**Answer:**
> **Requirements:** High-throughput, durable, ordered message delivery; support multiple consumers; replay capability.
>
> **Core design:** Append-only log per topic partition. Producers write to the end; consumers track their offset. Messages are retained for a configurable period (not deleted on consume).
>
> **Partitioning:** Topics split into N partitions distributed across brokers. Partition key determines which partition a message goes to (consistent hashing). Enables parallel consumption.
>
> **Consumer groups:** Multiple consumers in a group each own a subset of partitions. Enables horizontal scaling of consumers. Each group maintains independent offsets — same messages can be consumed by multiple groups.
>
> **Durability:** Replication factor R means each partition has R-1 replicas. Leader handles reads/writes; followers replicate. ISR (In-Sync Replicas) set determines commit acknowledgment.
>
> **Ordering guarantee:** Strict ordering within a partition; no ordering guarantee across partitions. Use a single partition for global ordering (sacrifices throughput).

---

### Q10: Design a Video Streaming Service (e.g., YouTube/Netflix)
**Framework:** Upload pipeline + transcoding + adaptive bitrate delivery

**Answer:**
> **Requirements:** Upload videos, transcode to multiple resolutions, stream to millions of concurrent viewers.
>
> **Upload pipeline:**
> 1. Client uploads raw video to object storage (S3) via pre-signed URL.
> 2. Upload completion triggers a transcoding job (via message queue).
> 3. Transcoding workers (GPU instances) produce multiple resolutions (360p, 720p, 1080p, 4K) and formats (HLS, DASH).
> 4. Transcoded segments stored in object storage; metadata updated in DB.
>
> **Streaming:** HLS/DASH splits video into small segments (2–10 seconds). Client player selects quality based on available bandwidth (adaptive bitrate). Segments served from CDN edge nodes.
>
> **CDN strategy:** Popular videos cached at edge globally. Long-tail videos served from origin. Pre-warm CDN for anticipated high-traffic content (new releases).
>
> **Metadata service:** Video title, description, tags, view count, recommendations stored in a combination of SQL (structured metadata) and Elasticsearch (full-text search).
>
> **Scale:** 500 hours of video uploaded per minute (YouTube scale). Transcoding is the bottleneck — scale with a large pool of async workers.

---

### Q11: Design a Web Crawler
**Framework:** BFS frontier + politeness + deduplication

**Answer:**
> **Requirements:** Crawl billions of web pages, respect robots.txt, avoid duplicate crawling, store content for indexing.
>
> **Architecture:**
> - **URL frontier:** Priority queue of URLs to crawl. Prioritize by PageRank, freshness, or domain importance. Partition by domain to enforce per-domain crawl rate limits.
> - **Fetcher workers:** Download page content. Respect `robots.txt` and `Crawl-delay`. Use a DNS cache to avoid repeated lookups.
> - **Content processor:** Extract links, detect duplicates (SimHash for near-duplicate detection), store content in object storage.
> - **URL deduplication:** Bloom filter for fast probabilistic membership check (seen this URL before?). Persistent store for confirmed deduplication.
>
> **Politeness:** Rate-limit requests per domain (e.g., 1 req/sec). Honor `robots.txt`. Use a polite delay between requests to the same host.
>
> **Scale:** 1B pages, avg 100 KB each = 100 TB storage. At 1000 pages/sec, crawling 1B pages takes ~11.5 days.

---

### Q12: Design an E-Commerce Order System
**Framework:** Saga pattern for distributed transactions + inventory reservation

**Answer:**
> **Requirements:** Place orders, reserve inventory, process payments, handle failures atomically across services.
>
> **Challenge:** An order involves multiple services (inventory, payment, shipping) — no single distributed transaction.
>
> **Saga pattern:** Break the transaction into a sequence of local transactions, each publishing an event. On failure, execute compensating transactions to undo previous steps.
>
> **Order flow:**
> 1. `OrderService` creates order in `PENDING` state → publishes `OrderCreated`
> 2. `InventoryService` reserves stock → publishes `InventoryReserved` (or `ReservationFailed`)
> 3. `PaymentService` charges card → publishes `PaymentProcessed` (or `PaymentFailed`)
> 4. `OrderService` marks order `CONFIRMED` → triggers fulfillment
>
> **Compensations:** If payment fails → release inventory reservation. If inventory fails → cancel order.
>
> **Idempotency:** Each step must be idempotent (safe to retry). Use idempotency keys for payment API calls.

---

## Practice Resources

### Recommended Platforms
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — comprehensive open-source reference
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview) — structured course with common interview questions
- [ByteByteGo](https://bytebytego.com) — visual system design explanations by Alex Xu
- [High Scalability](http://highscalability.com) — real-world architecture case studies

### Interview Framework (RESHADED)
Use this structure to organize your answer in any system design interview:

| Step | What to Cover |
|---|---|
| **R**equirements | Functional + non-functional; clarify scale, SLAs, constraints |
| **E**stimation | QPS, storage, bandwidth — back-of-envelope |
| **S**torage | Data model, DB choice (SQL vs NoSQL), schema |
| **H**igh-level design | Core components, data flow diagram |
| **A**PIs | Key endpoints, request/response format |
| **D**etailed design | Deep-dive on 1–2 critical components |
| **E**dge cases | Failure modes, bottlenecks, hot spots |
| **D**eep dive | Scaling, caching, monitoring, trade-offs |

### Key Numbers to Memorize
| Metric | Value |
|---|---|
| L1 cache reference | 1 ns |
| L2 cache reference | 4 ns |
| RAM read | 100 ns |
| SSD random read | 100 µs |
| HDD seek | 10 ms |
| Network round trip (same DC) | 500 µs |
| Network round trip (cross-continent) | 150 ms |
| 1 Gbps network throughput | 125 MB/s |

### Common Trade-offs to Know
| Decision | Option A | Option B |
|---|---|---|
| Consistency vs Availability | Strong consistency (CP) | High availability (AP) |
| SQL vs NoSQL | ACID, joins, schema | Scale, flexibility, speed |
| Push vs Pull (feed) | Fast reads, expensive writes | Cheap writes, slow reads |
| Synchronous vs Async | Simple, coupled | Resilient, decoupled |
| Monolith vs Microservices | Simple ops, tight coupling | Independent scaling, complexity |

### Additional Reading
- [DSA Study Guide](./DSA-Study-Guide.md) — algorithms and data structures for coding rounds
- [Big-O Cheatsheet](./Big-O-Cheatsheet.md) — complexity reference
- [Practice Problems](./Practice-Problems.md) — curated problem list by topic
- *Designing Data-Intensive Applications* — Martin Kleppmann (essential reading)
- *System Design Interview* Vol. 1 & 2 — Alex Xu
