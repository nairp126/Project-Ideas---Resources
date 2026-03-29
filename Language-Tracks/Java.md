# Java Projects

**Language Version:** Java 17+

A collection of project ideas for Java learners, from beginner console applications to intermediate backend services.

---

## Beginner

### 1. Student Grade Calculator
**Language Version:** Java 17+
**Description:** Build a console application that accepts a list of student names and their scores for multiple assignments, calculates the weighted average, assigns a letter grade, and prints a formatted report.
**Key Concepts:** Arrays, ArrayList, HashMap, Scanner, String formatting, switch expressions (Java 14+)
**Bonus:** Read student data from a CSV file using BufferedReader and write the report to an output file.

---

### 2. Bank Account Simulator
**Language Version:** Java 17+
**Description:** Implement a simple bank account system with classes for Account, SavingsAccount, and CheckingAccount. Support deposit, withdrawal, and transfer operations. Enforce a minimum balance rule on savings accounts.
**Key Concepts:** OOP (inheritance, encapsulation, polymorphism), abstract classes, exception handling, interfaces
**Bonus:** Add a transaction history list to each account and a method to print a formatted statement.

---

### 3. Library Book Catalog
**Language Version:** Java 17+
**Description:** Create a console-based library catalog where librarians can add books, search by title or author, check out books to borrowers, and return them. Track availability status for each book.
**Key Concepts:** Records (Java 16+), Collections (List, Map), Optional, streams, lambda expressions
**Bonus:** Persist the catalog to a JSON file using the Jackson library so data survives between runs.

---

### 4. Text-Based Adventure Game
**Language Version:** Java 17+
**Description:** Build a simple text adventure where the player navigates between rooms, picks up items, and solves a puzzle to win. Each room has a description, a list of exits, and optional items.
**Key Concepts:** Enums, sealed classes (Java 17+), pattern matching for instanceof, Scanner, game loop design
**Bonus:** Add a save/load feature using Java serialization so the player can resume their game.

---

### 5. Multi-Threaded File Downloader
**Language Version:** Java 17+
**Description:** Write a command-line tool that downloads a list of URLs concurrently. Show a progress indicator for each download and report the total time taken. Handle network errors gracefully with retries.
**Key Concepts:** ExecutorService, CompletableFuture, HttpClient (Java 11+), synchronized output, exception handling
**Bonus:** Add a checksum verification step that computes the SHA-256 hash of each downloaded file and compares it to an expected value.

---

## Intermediate

### 1. Spring Boot REST API for a Task Manager
**Language Version:** Java 17+
**Description:** Build a RESTful task management API using Spring Boot. Support user registration and login with JWT authentication, CRUD operations for tasks, and task assignment to users. Use Spring Data JPA with an H2 or PostgreSQL database.
**Key Concepts:** Spring Boot, Spring Security, JWT, JPA/Hibernate, DTO pattern, Bean Validation, ResponseEntity
**Bonus:** Add a WebSocket endpoint using Spring WebSocket so clients receive real-time notifications when a task is assigned to them.

---

### 2. Event-Driven Order Processing System
**Language Version:** Java 17+
**Description:** Simulate an e-commerce order processing pipeline using an event-driven architecture. An order service publishes events (OrderPlaced, PaymentProcessed, OrderShipped) and separate consumer services handle each event. Use an in-memory event bus or Apache Kafka.
**Key Concepts:** Event-driven design, producer/consumer pattern, Spring Kafka or a simple BlockingQueue, domain events, eventual consistency
**Bonus:** Add a dead-letter queue for failed events and a retry mechanism with exponential backoff.

---

### 3. Concurrent Web Crawler
**Language Version:** Java 17+
**Description:** Build a multi-threaded web crawler that starts from a seed URL, fetches pages, extracts all links, and recursively crawls up to a configurable depth. Store visited URLs and page metadata in a concurrent data structure.
**Key Concepts:** Virtual threads (Java 21 preview or structured concurrency), ConcurrentHashMap, Jsoup for HTML parsing, rate limiting, BFS traversal
**Bonus:** Export the crawl results as a site map in XML format and detect broken links (HTTP 4xx/5xx responses).
