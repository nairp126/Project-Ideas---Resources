# 📐 Content Standards

This document defines the required format and fields for every content type in this repository. All contributors must follow these standards before opening a pull request. The [PR template](.github/PULL_REQUEST_TEMPLATE.md) includes a checklist that references this document.

---

## Table of Contents

- [Project Idea — Beginner](#project-idea--beginner)
- [Project Idea — Intermediate](#project-idea--intermediate)
- [Project Idea — Advanced](#project-idea--advanced)
- [Cheatsheet](#cheatsheet)
- [Roadmap](#roadmap)
- [Snippet](#snippet)
- [Algorithm](#algorithm)
- [Language Track Entry](#language-track-entry)
- [Learning Path](#learning-path)

---

## Project Idea — Beginner

**Location:** `Project-Ideas/Beginner/README.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `title` | Short, descriptive project name with an emoji |
| `core_concept` | The CS or programming concepts the project teaches |
| `description` | 2–4 sentence problem description |
| `tech_stack` | Recommended language(s) and tools |
| `bonus_challenge` | At least one extension idea to push further |

### Format Example

```markdown
## 1. To-Do List CLI 📝

**Core Concept:** File I/O, CRUD operations, data persistence
**Description:** Build a command-line to-do list manager that lets users add, view,
complete, and delete tasks. Tasks are saved to a local JSON file so they persist
between sessions.
**Tech Stack:** Python or JavaScript (Node.js)
**Bonus Challenge:** Add due dates and a priority system; display overdue tasks in red.
```

---

## Project Idea — Intermediate

**Location:** `Project-Ideas/Intermediate/README.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `title` | Short, descriptive project name with an emoji |
| `problem_statement` | 2–4 sentence description of the problem being solved |
| `key_features` | Bulleted MVP feature list |
| `database_schema` | Text-format table definitions |
| `api_endpoints` | List of `METHOD /path` — description pairs |

### Format Example

```markdown
## 1. Blog Platform API 📰

**Problem Statement:** Build a RESTful API for a blogging platform where users can
register, create posts, add comments, and follow other authors. The API should support
pagination and full-text search.

### Key Features (MVP)
- User registration and JWT authentication
- Create, read, update, delete blog posts
- Comment on posts
- Follow/unfollow authors
- Paginated post listing

### Database Schema
```text
Users: id, username, email, password_hash, created_at
Posts: id, user_id, title, body, published_at
Comments: id, post_id, user_id, body, created_at
Follows: follower_id, followee_id, created_at
```

### API Endpoints
- `POST /auth/register` — Register a new user
- `POST /auth/login` — Authenticate and receive a JWT
- `GET /posts` — List all posts (paginated)
- `POST /posts` — Create a new post (auth required)
- `GET /posts/:id` — Get a single post
- `PUT /posts/:id` — Update a post (owner only)
- `DELETE /posts/:id` — Delete a post (owner only)
- `POST /posts/:id/comments` — Add a comment
```

---

## Project Idea — Advanced

**Location:** `Project-Ideas/Advanced/README.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `title` | Short, descriptive project name with an emoji |
| `project_overview` | 2–4 sentence description |
| `microservices` | Numbered list of services with their responsibilities |
| `containerization` | Dockerfile or Kubernetes YAML example |
| `cloud_infrastructure` | Bulleted list of cloud components and their roles |
| `system_design_challenge` | Problem statement and key considerations |

### Format Example

```markdown
## 1. E-Commerce Platform ⚡

**Project Overview:** Build a production-grade e-commerce platform using a microservices
architecture. The system handles product catalog, inventory, orders, payments, and
notifications as independent services communicating via a message broker.

### Microservices Architecture
1. **API Gateway** — Routes requests, handles auth, rate limiting
2. **Product Service** — Manages product catalog and search
3. **Inventory Service** — Tracks stock levels and reservations
4. **Order Service** — Processes and tracks orders
5. **Payment Service** — Handles payment processing via Stripe
6. **Notification Service** — Sends email/SMS confirmations

### Containerization Strategy
```yaml
# docker-compose.yml (excerpt)
services:
  api-gateway:
    build: ./api-gateway
    ports: ["3000:3000"]
  product-service:
    build: ./product-service
    depends_on: [postgres, redis]
```

### Cloud Infrastructure
- **AWS ECS / Kubernetes** — Container orchestration
- **RDS (PostgreSQL)** — Persistent data storage per service
- **ElastiCache (Redis)** — Session store and caching layer
- **SQS / RabbitMQ** — Async messaging between services
- **CloudFront + S3** — Static asset delivery

### System Design Challenge
**Problem:** How do you handle a flash sale where 10,000 users simultaneously try to
purchase the last 100 units of a product?
**Key Considerations:** Optimistic locking vs. pessimistic locking, Redis-based inventory
reservation, idempotent payment processing, eventual consistency.
```

---

## Cheatsheet

**Location:** `Resources/Cheatsheets/{Topic}-Cheatsheet.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `title` | `# Topic Cheatsheet` as the H1 heading |
| `table_of_contents` | Links to every `##` section using anchor syntax |
| `sections` | At least 3 labeled `##` sections |
| `code_blocks` | All commands and syntax examples in fenced code blocks with a language identifier |

### Format Example

```markdown
# Git Cheatsheet

## Table of Contents
- [Setup](#setup)
- [Basic Workflow](#basic-workflow)
- [Branching](#branching)

---

## Setup

Configure your identity before your first commit.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Basic Workflow

```bash
git init          # Initialize a new repo
git add .         # Stage all changes
git commit -m ""  # Commit with a message
git push          # Push to remote
```

## Branching

```bash
git checkout -b feature/my-feature   # Create and switch to a new branch
git merge feature/my-feature         # Merge branch into current branch
git branch -d feature/my-feature     # Delete a branch
```
```

---

## Roadmap

**Location:** `Roadmaps/{Role}.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `last_updated` | ISO date (`YYYY-MM-DD`) at the top of the document |
| `topic_badges` | Shield.io or text badges for primary technologies |
| `monthly_phases` | Each phase must include: Focus, Technologies, Key Concepts, Build This, Resources, Success Criteria |
| `salary_section` | Median salary ranges, top hiring companies, in-demand skills |
| `common_mistakes` | At least 3 pitfalls learners commonly encounter |

### Format Example

```markdown
# 🗺️ Backend Engineer Roadmap

*Last Updated: 2025-01-15*

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)

## Month 1: Foundations
**Focus:** Core programming and web fundamentals
**Technologies:** Python or JavaScript, HTTP basics
**Key Concepts:** Variables, functions, REST, request/response cycle
**Build This:** A simple HTTP server that returns JSON
**Resources:** MDN Web Docs, The Odin Project
**Success Criteria:** Can explain what happens when a browser makes an HTTP request

---

## 💰 Salary & Job Market
- **Median Salary (US):** $110,000–$145,000
- **Top Hiring Companies:** Amazon, Stripe, Shopify, startups
- **In-Demand Skills:** Node.js, PostgreSQL, Docker, REST APIs, system design

## ⚠️ Common Mistakes
1. Skipping fundamentals to jump straight to frameworks
2. Ignoring database indexing and query optimization
3. Not learning how to read and write documentation
```

---

## Snippet

**Location:** `Resources/Snippets/{Language}-Snippets.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `category` | `##` section grouping related snippets |
| `title` | `###` heading for the individual snippet |
| `description` | 1–3 sentence explanation of purpose and usage, placed directly above the code block |
| `code_block` | Fenced code block with the language identifier on the opening fence |

### Format Example

```markdown
# Python Snippets

## Authentication Patterns

### JWT Token Generation

Generate a signed JWT token with an expiry time. Requires the `PyJWT` library.
Use this pattern for stateless API authentication.

```python
import jwt
import datetime

def generate_token(user_id: int, secret: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    return jwt.encode(payload, secret, algorithm="HS256")
```
```

---

## Algorithm

**Location:** `Resources/Algorithms/{Category}.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `name` | `##` heading with the algorithm name |
| `time_complexity` | Big-O time complexity |
| `space_complexity` | Big-O space complexity |
| `explanation` | Plain-English description of how the algorithm works |
| `pseudocode` | Language-agnostic pseudocode in a fenced code block |
| `implementation` | Working code in at least one language in a fenced code block with language id |

### Format Example

```markdown
## Merge Sort

**Category:** Sorting
**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

### Explanation
Merge sort divides the array in half recursively until each sub-array has one element,
then merges the sub-arrays back together in sorted order. It is a stable sort and
performs consistently regardless of input order.

### Pseudocode
```
function mergeSort(array):
    if length(array) <= 1:
        return array
    mid = length(array) / 2
    left = mergeSort(array[0..mid])
    right = mergeSort(array[mid..end])
    return merge(left, right)
```

### Implementation
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```
```

---

## Language Track Entry

**Location:** `Language-Tracks/{Language}.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `title` | `###` heading with the project name |
| `language_version` | Exact version or runtime requirement (e.g., `Python 3.10+`) |
| `description` | 2–3 sentence problem description |
| `key_concepts` | CS or language concepts the project practices |
| `difficulty` | `Beginner` or `Intermediate` |

### Format Example

```markdown
# Python Projects

## Beginner

### 1. File Organizer Script
**Language Version:** Python 3.10+
**Difficulty:** Beginner
**Description:** Build a script that scans a directory and automatically moves files
into subdirectories based on their extension (e.g., `.jpg` → `Images/`).
**Key Concepts:** `pathlib`, file system operations, string manipulation
**Bonus:** Add a dry-run flag that previews changes without moving files.
```

---

## Learning Path

**Location:** `Learning-Paths/{Path-Name}.md`

### Required Fields

| Field | Description |
| :--- | :--- |
| `overview` | Who the path is for and the total estimated time |
| `phases` | At least 2 phases, each with a time estimate in weeks |
| `roadmap_link` | Link to the relevant Roadmap file |
| `projects` | 5–8 Project_Ideas in recommended build order with links |
| `resources` | At least 5 links to repository Resources |
| `time_estimate` | Weeks per phase, stated in the phase heading or body |

### Format Example

```markdown
# Zero to Junior Frontend Developer

## Overview
This path takes a complete beginner from zero programming experience to job-ready
junior frontend developer. Estimated total time: 6–9 months.

## Phase 1: Foundations (~6 weeks)
**Roadmap:** [Frontend Developer Roadmap](../Roadmaps/Frontend-Developer.md)

**Projects to Build:**
1. [Personal Portfolio Page](../Project-Ideas/Beginner/README.md#portfolio)
2. [Calculator App](../Project-Ideas/Beginner/README.md#calculator)

**Resources:**
- [JavaScript Cheatsheet](../Resources/Cheatsheets/JavaScript-Cheatsheet.md)
- [Git Cheatsheet](../Resources/Cheatsheets/Git-Cheatsheet.md)
```
