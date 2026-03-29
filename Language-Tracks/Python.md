# Python Projects

**Language Version:** Python 3.10+

A collection of project ideas for Python learners, from beginner scripts to intermediate applications.

---

## Beginner

### 1. Command-Line To-Do List
**Language Version:** Python 3.10+
**Description:** Build a CLI application that lets users add, list, complete, and delete tasks. Tasks are persisted to a local JSON file so they survive between sessions.
**Key Concepts:** File I/O, JSON serialization, argparse or sys.argv, list manipulation
**Bonus:** Add due dates and a `--overdue` filter that highlights tasks past their deadline.

---

### 2. Number Guessing Game
**Language Version:** Python 3.10+
**Description:** Create a game where the program picks a random number and the user has a limited number of guesses. After each guess, the program tells the user whether to guess higher or lower.
**Key Concepts:** random module, while loops, input validation, conditional logic
**Bonus:** Add difficulty levels (easy/medium/hard) that change the range and number of allowed guesses.

---

### 3. Unit Converter
**Language Version:** Python 3.10+
**Description:** Write a program that converts between common units: temperature (Celsius/Fahrenheit/Kelvin), length (km/miles/feet), and weight (kg/lbs). Accept input from the command line.
**Key Concepts:** Functions, dictionaries, type conversion, match/case statement (Python 3.10+)
**Bonus:** Add a currency converter that fetches live exchange rates from a free public API.

---

### 4. Text File Word Frequency Analyzer
**Language Version:** Python 3.10+
**Description:** Read a plain-text file and output the top N most frequent words, excluding common stop words. Display results as a sorted table in the terminal.
**Key Concepts:** File reading, string methods, collections.Counter, sorting, f-strings
**Bonus:** Generate a simple bar chart in the terminal using only standard library tools.

---

### 5. Personal Expense Tracker
**Language Version:** Python 3.10+
**Description:** Build a CLI tool to log daily expenses by category (food, transport, entertainment, etc.). Store data in a CSV file and provide a monthly summary showing totals per category.
**Key Concepts:** csv module, datetime, dataclasses, formatted output
**Bonus:** Add a monthly budget limit per category and warn the user when they are close to the limit.

---

## Intermediate

### 1. REST API with FastAPI
**Language Version:** Python 3.10+
**Description:** Build a RESTful API for a simple blog platform. Users can create accounts, write posts, and comment on posts. Use FastAPI for routing and Pydantic for request/response validation. Persist data with SQLite via SQLAlchemy.
**Key Concepts:** FastAPI, Pydantic models, SQLAlchemy ORM, JWT authentication, HTTP status codes, dependency injection
**Bonus:** Add pagination to the posts endpoint and a full-text search endpoint using SQLite's FTS5 extension.

---

### 2. Web Scraper and Data Pipeline
**Language Version:** Python 3.10+
**Description:** Scrape a public website (e.g., a job board or news site) using BeautifulSoup and requests. Clean and normalize the extracted data, store it in a SQLite database, and export a daily CSV report.
**Key Concepts:** requests, BeautifulSoup, data cleaning, sqlite3, scheduling with schedule or cron, logging
**Bonus:** Add a simple Flask dashboard that visualizes the scraped data with charts using Chart.js.

---

### 3. Async Chat Application
**Language Version:** Python 3.10+
**Description:** Create a multi-user chat server and client using Python's asyncio and websockets libraries. Support multiple chat rooms, usernames, and a `/history` command that returns the last 20 messages.
**Key Concepts:** asyncio, websockets, concurrency, message queues, JSON protocol design
**Bonus:** Add end-to-end encryption using the cryptography library so messages are encrypted before transmission.
