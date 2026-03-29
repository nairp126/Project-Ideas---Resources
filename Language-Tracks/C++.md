# C++ Projects

**Language Standard:** C++17

A collection of project ideas for C++ learners, from beginner console programs to intermediate systems-level applications.

---

## Beginner

### 1. Contact Book
**Language Version:** C++17
**Description:** Build a console application to manage a contact list. Users can add contacts (name, phone, email), search by name, update details, and delete entries. Store contacts in a vector and persist them to a binary file.
**Key Concepts:** structs, std::vector, std::string, file I/O with fstream, linear search, range-based for loops
**Bonus:** Sort contacts alphabetically using std::sort with a custom comparator and add a case-insensitive search option.

---

### 2. Matrix Calculator
**Language Version:** C++17
**Description:** Implement a matrix calculator that supports addition, subtraction, multiplication, and transposition for matrices of arbitrary size. Read matrix dimensions and values from the user and display results in a formatted grid.
**Key Concepts:** 2D vectors, operator overloading, templates, input validation, nested loops
**Bonus:** Add determinant calculation and matrix inversion for square matrices using Gaussian elimination.

---

### 3. Simple Stack-Based Calculator
**Language Version:** C++17
**Description:** Write a Reverse Polish Notation (RPN) calculator. The user enters an expression like `3 4 + 2 *` and the program evaluates it using a stack. Support +, -, *, /, and % operators.
**Key Concepts:** std::stack, std::istringstream, exception handling (std::invalid_argument), LIFO data structure
**Bonus:** Extend the calculator to support variables: users can assign values (`x = 5`) and use them in expressions.

---

### 4. File Encryption Tool
**Language Version:** C++17
**Description:** Create a command-line tool that encrypts and decrypts text files using a simple XOR cipher with a user-provided key. The tool reads the input file, applies the cipher byte-by-byte, and writes the result to an output file.
**Key Concepts:** Binary file I/O, bitwise XOR, command-line argument parsing with argc/argv, std::filesystem (C++17)
**Bonus:** Implement a Caesar cipher as an alternative mode and add a `--mode` flag to select between XOR and Caesar.

---

### 5. Inventory Management System
**Language Version:** C++17
**Description:** Build a console-based inventory system for a small store. Support adding products (name, SKU, quantity, price), updating stock levels, searching by SKU, and generating a low-stock report for items below a threshold.
**Key Concepts:** std::map, std::optional (C++17), structured bindings (C++17), formatted output with iomanip, file persistence
**Bonus:** Add a simple transaction log that records every stock change with a timestamp using std::chrono.

---

## Intermediate

### 1. Thread-Safe Bounded Queue
**Language Version:** C++17
**Description:** Implement a generic, thread-safe bounded queue (producer-consumer buffer) using std::mutex, std::condition_variable, and std::thread. Write a test harness that spawns multiple producer and consumer threads and verifies correctness under load.
**Key Concepts:** std::mutex, std::condition_variable, std::thread, RAII lock guards, template classes, move semantics
**Bonus:** Implement a lock-free version using std::atomic and compare throughput between the two implementations using std::chrono benchmarks.

---

### 2. HTTP Server from Scratch
**Language Version:** C++17
**Description:** Build a minimal HTTP/1.1 server using POSIX sockets. The server should handle GET requests, serve static files from a configurable directory, return correct status codes (200, 404, 405), and handle multiple concurrent connections using a thread pool.
**Key Concepts:** POSIX sockets (socket, bind, listen, accept), HTTP request parsing, thread pool with std::thread, MIME type detection, std::filesystem
**Bonus:** Add support for chunked transfer encoding and implement a simple router that maps URL paths to handler functions.

---

### 3. Memory Allocator
**Language Version:** C++17
**Description:** Implement a custom memory allocator that manages a fixed-size memory pool. Support malloc-style allocation and free operations with a free-list strategy. Track fragmentation and provide a stats() function reporting total, used, and free bytes.
**Key Concepts:** Placement new, pointer arithmetic, free-list data structure, alignment, operator new/delete overloading, unit testing
**Bonus:** Implement a buddy allocator as an alternative strategy and benchmark both allocators against the system allocator using a realistic allocation pattern.
