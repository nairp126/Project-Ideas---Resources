# JavaScript Projects

**Runtime:** Node.js 18+

A collection of project ideas for JavaScript learners, from beginner scripts to intermediate full-stack applications.

---

## Beginner

### 1. Interactive Quiz App
**Language Version:** Node.js 18+
**Description:** Build a browser-based multiple-choice quiz. Questions are stored in a JSON file. The app tracks the score, shows feedback after each answer, and displays a final results screen.
**Key Concepts:** DOM manipulation, event listeners, fetch API, JSON, ES6 modules
**Bonus:** Add a countdown timer per question and a leaderboard stored in localStorage.

---

### 2. Weather Dashboard
**Language Version:** Node.js 18+
**Description:** Create a web page that lets users search for a city and displays current weather conditions (temperature, humidity, wind speed, description) using the OpenWeatherMap free API.
**Key Concepts:** fetch API, async/await, DOM manipulation, error handling, CSS Flexbox
**Bonus:** Show a 5-day forecast and allow the user to toggle between Celsius and Fahrenheit.

---

### 3. Markdown Previewer
**Language Version:** Node.js 18+
**Description:** Build a two-panel editor where the left panel accepts raw Markdown input and the right panel renders the live HTML preview. Use the marked.js library for parsing.
**Key Concepts:** Event listeners, innerHTML, third-party library integration via CDN, debouncing
**Bonus:** Add a toolbar with buttons for common Markdown formatting (bold, italic, code block, link).

---

### 4. CLI Task Manager
**Language Version:** Node.js 18+
**Description:** Write a Node.js command-line tool to manage a to-do list. Support commands: `add`, `list`, `done`, and `delete`. Persist tasks to a local JSON file using the fs module.
**Key Concepts:** Node.js fs module, process.argv, JSON.parse/stringify, ES modules
**Bonus:** Add colorized output using the chalk package and a `--priority` flag for tasks.

---

### 5. Expense Splitter
**Language Version:** Node.js 18+
**Description:** Build a web app where a group of friends can enter shared expenses and the app calculates who owes whom and how much to settle all debts with the minimum number of transactions.
**Key Concepts:** Array methods (reduce, map, filter), algorithm design, form handling, local state management
**Bonus:** Allow users to export the settlement summary as a PDF using the browser's print API.

---

## Intermediate

### 1. Real-Time Collaborative Notes App
**Language Version:** Node.js 18+
**Description:** Build a web application where multiple users can create and edit notes simultaneously. Use Socket.io for real-time synchronization, Express for the backend, and a simple frontend with vanilla JS. Store notes in a MongoDB database.
**Key Concepts:** Socket.io, Express.js, MongoDB with Mongoose, real-time events, conflict resolution (last-write-wins)
**Bonus:** Add operational transformation (OT) so concurrent edits to the same note are merged intelligently rather than overwritten.

---

### 2. E-Commerce Product Catalog API
**Language Version:** Node.js 18+
**Description:** Build a RESTful API for an e-commerce product catalog. Support CRUD operations for products and categories, image URL storage, inventory tracking, and basic search/filter by price range and category. Use Express and PostgreSQL.
**Key Concepts:** Express.js, PostgreSQL with pg or Prisma, RESTful design, query parameters, input validation with Joi or Zod, pagination
**Bonus:** Add a Redis cache layer for the product listing endpoint to reduce database load on repeated queries.

---

### 3. Browser Extension: Reading Time Estimator
**Language Version:** Node.js 18+ (build tooling)
**Description:** Create a Chrome/Firefox browser extension that injects a reading time estimate at the top of any article page. The estimate is based on word count and an adjustable words-per-minute setting stored in extension storage.
**Key Concepts:** Browser extension manifest v3, content scripts, background service workers, chrome.storage API, DOM traversal
**Bonus:** Add a progress bar that fills as the user scrolls through the article, and a "bookmark for later" button that saves the URL to a popup list.
