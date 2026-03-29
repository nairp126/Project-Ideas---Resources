# JavaScript Cheatsheet

A quick reference for modern JavaScript (ES6+) syntax and patterns.

## Table of Contents
- [Variables & Data Types](#variables--data-types)
- [Functions](#functions)
- [Arrays](#arrays)
- [Objects](#objects)
- [Destructuring & Spread](#destructuring--spread)
- [Async JavaScript](#async-javascript)
- [Classes & Modules](#classes--modules)
- [DOM Manipulation](#dom-manipulation)
- [Error Handling](#error-handling)

---

## Variables & Data Types

Declaring variables and understanding JavaScript types.

```javascript
// Variable declarations
const PI = 3.14159;       // block-scoped, immutable binding
let count = 0;            // block-scoped, mutable
var legacy = "avoid";     // function-scoped, avoid in modern JS

// Primitive types
const num = 42;
const float = 3.14;
const str = "hello";
const bool = true;
const nothing = null;
const undef = undefined;
const sym = Symbol("id");
const big = 9007199254740991n;  // BigInt

// Type checking
typeof 42          // "number"
typeof "hi"        // "string"
typeof null        // "object" (historical quirk)
typeof undefined   // "undefined"
Array.isArray([])  // true

// Template literals
const name = "Alice";
const greeting = `Hello, ${name}! Today is ${new Date().toDateString()}.`;

// Nullish coalescing
const value = null ?? "default";   // "default"
const val2 = 0 ?? "default";       // 0 (only null/undefined triggers)

// Optional chaining
const city = user?.address?.city;  // undefined if any part is null/undefined
const len = arr?.length ?? 0;
```

---

## Functions

Different ways to define and use functions.

```javascript
// Function declaration (hoisted)
function add(a, b) {
  return a + b;
}

// Function expression
const multiply = function(a, b) {
  return a * b;
};

// Arrow function
const square = (x) => x * x;
const greet = name => `Hello, ${name}!`;
const sum = (a, b) => {
  const result = a + b;
  return result;
};

// Default parameters
function greet(name = "World") {
  return `Hello, ${name}!`;
}

// Rest parameters
function total(...nums) {
  return nums.reduce((acc, n) => acc + n, 0);
}

// Spread in function call
const nums = [1, 2, 3];
Math.max(...nums);   // 3

// Immediately Invoked Function Expression (IIFE)
(function() {
  console.log("Runs immediately");
})();

// Higher-order functions
const double = x => x * 2;
[1, 2, 3].map(double);   // [2, 4, 6]

// Closures
function makeCounter() {
  let count = 0;
  return () => ++count;
}
const counter = makeCounter();
counter();  // 1
counter();  // 2
```

---

## Arrays

Working with JavaScript arrays.

```javascript
const arr = [1, 2, 3, 4, 5];

// Access & modify
arr[0];              // 1
arr.length;          // 5
arr.push(6);         // add to end
arr.pop();           // remove from end
arr.unshift(0);      // add to start
arr.shift();         // remove from start
arr.splice(2, 1);    // remove 1 element at index 2

// Iteration
arr.forEach(n => console.log(n));

// Transformation
arr.map(n => n * 2);           // [2, 4, 6, 8, 10]
arr.filter(n => n % 2 === 0);  // [2, 4]
arr.reduce((acc, n) => acc + n, 0);  // 15
arr.find(n => n > 3);          // 4
arr.findIndex(n => n > 3);     // 3
arr.some(n => n > 4);          // true
arr.every(n => n > 0);         // true

// Slicing & combining
arr.slice(1, 3);               // [2, 3] (non-mutating)
[...arr, 6, 7];                // spread to combine
arr.flat();                    // flatten one level
arr.flatMap(n => [n, n * 2]);  // map then flatten

// Sorting
arr.sort((a, b) => a - b);     // ascending numeric
arr.sort((a, b) => b - a);     // descending numeric
["banana", "apple"].sort();    // alphabetical

// Searching
arr.includes(3);               // true
arr.indexOf(3);                // 2
arr.lastIndexOf(3);            // 2

// Array creation
Array.from({length: 5}, (_, i) => i);  // [0, 1, 2, 3, 4]
Array.from("hello");                    // ["h","e","l","l","o"]
[...new Set([1, 1, 2, 3])];            // [1, 2, 3] (deduplicate)
```

---

## Objects

Creating and manipulating JavaScript objects.

```javascript
// Object literal
const user = {
  name: "Alice",
  age: 30,
  greet() {
    return `Hi, I'm ${this.name}`;
  }
};

// Property access
user.name;          // dot notation
user["name"];       // bracket notation (dynamic keys)

// Shorthand property names
const name = "Bob";
const age = 25;
const person = { name, age };  // { name: "Bob", age: 25 }

// Computed property names
const key = "color";
const obj = { [key]: "blue" };  // { color: "blue" }

// Object methods
Object.keys(user);    // ["name", "age", "greet"]
Object.values(user);  // ["Alice", 30, function]
Object.entries(user); // [["name","Alice"], ["age",30], ...]
Object.assign({}, user, { age: 31 });  // shallow copy + override
Object.freeze(user);  // make immutable

// Spread (shallow copy / merge)
const updated = { ...user, age: 31 };
const merged = { ...defaults, ...overrides };

// Optional chaining & nullish coalescing
const zip = user?.address?.zip ?? "N/A";

// Checking properties
"name" in user;              // true
user.hasOwnProperty("name"); // true
```

---

## Destructuring & Spread

Extract values from arrays and objects concisely.

```javascript
// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

// Skip elements
const [, , third] = [1, 2, 3];  // third=3

// Default values
const [a = 0, b = 0] = [1];  // a=1, b=0

// Object destructuring
const { name, age, city = "Unknown" } = user;

// Rename while destructuring
const { name: userName, age: userAge } = user;

// Nested destructuring
const { address: { street, zip } } = user;

// Function parameter destructuring
function display({ name, age = 0 }) {
  console.log(`${name} is ${age}`);
}

// Swap variables
let x = 1, y = 2;
[x, y] = [y, x];

// Spread operator
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];  // [1,2,3,4,5,6]

const obj1 = { a: 1 };
const obj2 = { b: 2 };
const merged = { ...obj1, ...obj2 };  // { a:1, b:2 }
```

---

## Async JavaScript

Handle asynchronous operations with Promises and async/await.

```javascript
// Promise
const fetchData = () =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve("data"), 1000);
  });

fetchData()
  .then(data => console.log(data))
  .catch(err => console.error(err))
  .finally(() => console.log("done"));

// Promise combinators
Promise.all([fetch("/a"), fetch("/b")])
  .then(([resA, resB]) => { /* both resolved */ });

Promise.allSettled([p1, p2])
  .then(results => results.forEach(r => console.log(r.status)));

Promise.race([p1, p2])
  .then(first => console.log("First resolved:", first));

// async / await
async function getUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Failed to fetch user:", error);
    throw error;
  }
}

// Parallel async operations
async function loadAll() {
  const [users, posts] = await Promise.all([
    fetch("/api/users").then(r => r.json()),
    fetch("/api/posts").then(r => r.json()),
  ]);
  return { users, posts };
}

// Async iteration
async function* generateNumbers() {
  for (let i = 0; i < 5; i++) {
    await new Promise(r => setTimeout(r, 100));
    yield i;
  }
}

for await (const num of generateNumbers()) {
  console.log(num);
}
```

---

## Classes & Modules

Organize code with classes and ES modules.

```javascript
// Class definition
class Animal {
  #sound;  // private field (ES2022)

  constructor(name, sound) {
    this.name = name;
    this.#sound = sound;
  }

  speak() {
    return `${this.name} says ${this.#sound}`;
  }

  static create(name, sound) {
    return new Animal(name, sound);
  }

  get info() {
    return `${this.name} (${this.#sound})`;
  }
}

// Inheritance
class Dog extends Animal {
  constructor(name, breed) {
    super(name, "woof");
    this.breed = breed;
  }

  speak() {
    return `${super.speak()} (${this.breed})`;
  }
}

// ES Modules
// math.js
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export default class Calculator { /* ... */ }

// main.js
import Calculator, { PI, add } from "./math.js";
import * as math from "./math.js";
```

---

## DOM Manipulation

Interact with the browser's Document Object Model.

```javascript
// Select elements
document.getElementById("my-id");
document.querySelector(".my-class");
document.querySelectorAll("p");

// Modify content
element.textContent = "New text";
element.innerHTML = "<strong>Bold</strong>";

// Modify attributes
element.setAttribute("href", "https://example.com");
element.getAttribute("href");
element.removeAttribute("disabled");

// Modify styles
element.style.color = "red";
element.classList.add("active");
element.classList.remove("hidden");
element.classList.toggle("open");
element.classList.contains("active");  // true/false

// Create & insert elements
const div = document.createElement("div");
div.textContent = "Hello";
parent.appendChild(div);
parent.insertBefore(div, referenceNode);
parent.removeChild(div);

// Event listeners
button.addEventListener("click", (event) => {
  event.preventDefault();
  console.log("Clicked!", event.target);
});

// Event delegation
document.querySelector("ul").addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log("List item clicked:", e.target.textContent);
  }
});
```

---

## Error Handling

Handle runtime errors gracefully.

```javascript
// try / catch / finally
try {
  const data = JSON.parse(invalidJson);
} catch (error) {
  if (error instanceof SyntaxError) {
    console.error("Invalid JSON:", error.message);
  } else {
    throw error;  // re-throw unexpected errors
  }
} finally {
  console.log("Cleanup");
}

// Custom error classes
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

function validateAge(age) {
  if (typeof age !== "number") throw new ValidationError("Must be a number", "age");
  if (age < 0) throw new ValidationError("Must be non-negative", "age");
  return age;
}

// Error handling in async code
async function safeRequest(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error("Request failed:", err.message);
    return null;
  }
}
```
