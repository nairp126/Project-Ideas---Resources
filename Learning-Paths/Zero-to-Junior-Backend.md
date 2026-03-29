# Zero to Junior Backend Developer

## Overview

**Who this is for:** Complete beginners with little or no programming experience who want to land their first backend, API, or server-side engineering role.

**Estimated total time:** 6–9 months (assuming 10–15 hours per week)

**Roadmap:** [Backend Engineer Roadmap](../Roadmaps/Backend-Engineer.md)

This path takes you from zero programming knowledge to a portfolio strong enough to apply for junior backend roles. You'll learn Python fundamentals, then move into web frameworks, databases, and APIs, finishing with a capstone project that demonstrates production-ready thinking.

---

## Phase 1: Programming Fundamentals (~6 weeks)

**Goal:** Write clean, working Python code and understand core computer science concepts.

**Roadmap:** [Backend Engineer Roadmap](../Roadmaps/Backend-Engineer.md)

**What to learn:**
- Python syntax: variables, data types, control flow, functions
- Data structures: lists, dictionaries, sets, tuples
- Object-oriented programming: classes, inheritance, encapsulation
- File I/O and working with JSON and CSV
- Error handling with try/except
- Basic Git and GitHub (commits, branches, pull requests)

**Projects to Build:**

1. [Simple Calculator](../Project-Ideas/Beginner/README.md) — Implement a CLI calculator with all basic operations. Focus on clean function design and input validation.
2. [Contact Book](../Project-Ideas/Beginner/README.md) — Build a CLI contact manager that reads and writes to a JSON file. Reinforces file I/O, dictionaries, and CRUD operations.
3. [Personal Budget Tracker](../Project-Ideas/Beginner/README.md) — A CLI app that logs income and expenses to a CSV file and prints monthly summaries. Introduces data aggregation patterns.

**Resources:**
- [Python Cheatsheet](../Resources/Cheatsheets/Python-Cheatsheet.md) — syntax reference for the language features you're learning
- [Python Snippets](../Resources/Snippets/Python-Snippets.md) — reusable patterns for file I/O, string manipulation, and data processing
- [Git Cheatsheet](../Resources/Cheatsheets/Git-Cheatsheet.md) — essential Git commands for version control
- [Linux/Bash Cheatsheet](../Resources/Cheatsheets/Linux-Bash-Cheatsheet.md) — terminal commands you'll use every day
- [Developer Workflow Guide](../Resources/Guides/Developer-Workflow-Guide.md) — set up your editor, terminal, pyenv, and Git aliases

**Milestone:** You can write a multi-file Python program, handle errors gracefully, read and write files, and push your code to GitHub.

---

## Phase 2: Databases & SQL (~4 weeks)

**Goal:** Design relational database schemas and query data with SQL.

**Roadmap:** [Backend Engineer Roadmap](../Roadmaps/Backend-Engineer.md)

**What to learn:**
- Relational database concepts (tables, rows, columns, primary/foreign keys)
- SQL fundamentals: SELECT, INSERT, UPDATE, DELETE, WHERE, JOIN
- Aggregation: GROUP BY, COUNT, SUM, AVG, HAVING
- Indexes and query performance basics
- Using SQLite with Python (sqlite3 module)
- Introduction to PostgreSQL

**Projects to Build:**

4. [Grade Calculator](../Project-Ideas/Beginner/README.md) — Extend this project to persist grades in a SQLite database instead of in-memory. Practice schema design and basic queries.

**Resources:**
- [SQL Cheatsheet](../Resources/Cheatsheets/SQL-Cheatsheet.md) — SQL syntax reference covering SELECT, JOIN, aggregation, and more
- [Data Structures Reference](../Resources/Algorithms/Data-Structures-Reference.md) — understand hash maps and trees, which underpin database indexes

**Milestone:** You can design a normalized database schema, write JOIN queries, and connect a Python script to a SQLite or PostgreSQL database.

---

## Phase 3: Web APIs & Frameworks (~6 weeks)

**Goal:** Build RESTful APIs with a Python web framework and understand HTTP.

**Roadmap:** [Backend Engineer Roadmap](../Roadmaps/Backend-Engineer.md)

**What to learn:**
- HTTP fundamentals (methods, status codes, headers, request/response cycle)
- REST API design principles (resources, endpoints, versioning)
- FastAPI or Flask: routing, request parsing, response formatting
- Authentication: JWT tokens, password hashing (bcrypt)
- Input validation and error handling in APIs
- Environment variables and configuration management
- Docker basics: containerizing a Python app

**Projects to Build:**

5. [Study Group Finder](../Project-Ideas/Intermediate/README.md) — Build the full REST API: user auth, group CRUD, availability scheduling, and basic messaging. Use FastAPI + PostgreSQL.
6. [Expense Splitting App](../Project-Ideas/Intermediate/README.md) — Implement the backend API for group expense tracking, balance calculation, and settlement recording.

**Resources:**
- [Docker Cheatsheet](../Resources/Cheatsheets/Docker-Cheatsheet.md) — containerize your API for consistent local development and deployment
- [Python Snippets](../Resources/Snippets/Python-Snippets.md) — authentication patterns, database connection patterns, and API request patterns
- [Sorting Algorithms](../Resources/Algorithms/Sorting-Algorithms.md) — understand the algorithms behind the data processing you're implementing

**Milestone:** You can build a fully functional REST API with authentication, connect it to a PostgreSQL database, and run it in a Docker container.

---

## Phase 4: Portfolio & Interview Prep (~6 weeks)

**Goal:** Polish your portfolio, practice interview questions, and apply for jobs.

**Roadmap:** [Backend Engineer Roadmap](../Roadmaps/Backend-Engineer.md)

**What to learn:**
- System design fundamentals (load balancing, caching, databases at scale)
- Message queues and async processing concepts
- API security (rate limiting, input sanitization, HTTPS)
- Writing tests (pytest, unit tests, integration tests)
- Deploying to a cloud provider (Railway, Render, or AWS EC2)
- Technical interview patterns (arrays, hash maps, trees, graphs)

**Projects to Build:**

7. [Local Service Marketplace](../Project-Ideas/Intermediate/README.md) — Your capstone: a full-featured marketplace API with provider profiles, booking management, reviews, and availability calendars. Deploy it publicly.
8. [Data Analysis CLI Tool](../Project-Ideas/Intermediate/README.md) — Build a Python CLI that loads CSVs, computes statistics, filters rows, and exports results. Demonstrates data processing skills valued in backend roles.

**Resources:**
- [DSA Study Guide](../Resources/Interview-Prep/DSA-Study-Guide.md) — arrays, hash maps, trees, and graphs are the most common backend interview topics
- [System Design Guide](../Resources/Interview-Prep/System-Design-Guide.md) — prepare for system design rounds with scalability, caching, and database design patterns
- [Big-O Cheatsheet](../Resources/Interview-Prep/Big-O-Cheatsheet.md) — understand time and space complexity for interview questions
- [Behavioral Interview Guide](../Resources/Interview-Prep/Behavioral-Interview-Guide.md) — prepare STAR-format answers for HR and hiring manager rounds
- [Practice Problems](../Resources/Interview-Prep/Practice-Problems.md) — work through easy and medium problems on arrays, strings, and hash maps
- [Open Source Guide](../Resources/Guides/Open-Source-Guide.md) — contribute to an open source Python project to strengthen your portfolio

**Milestone:** You have 2–3 deployed APIs on your portfolio, a polished GitHub profile, and can solve easy LeetCode problems in Python.

---

## What's Next

After landing your first role, explore:
- [Full-Stack Developer Roadmap](../Roadmaps/Full-Stack-Developer.md) — add frontend skills to your toolkit
- [DevOps Engineer Roadmap](../Roadmaps/DevOps-Engineer.md) — learn CI/CD, Kubernetes, and infrastructure as code
- [Advanced Project Ideas](../Project-Ideas/Advanced/README.md) — tackle microservices, distributed systems, and cloud architecture
- [System Design Guide](../Resources/Interview-Prep/System-Design-Guide.md) — go deeper on scalability and architecture patterns
