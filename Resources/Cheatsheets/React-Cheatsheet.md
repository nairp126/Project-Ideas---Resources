# React Cheatsheet

A quick reference for React hooks, patterns, and best practices (React 18+).

## Table of Contents
- [Components & JSX](#components--jsx)
- [Core Hooks](#core-hooks)
- [Additional Hooks](#additional-hooks)
- [Event Handling](#event-handling)
- [Lists & Conditional Rendering](#lists--conditional-rendering)
- [Forms](#forms)
- [Context API](#context-api)
- [Performance Optimization](#performance-optimization)
- [Custom Hooks](#custom-hooks)

---

## Components & JSX

Building blocks of React applications.

```jsx
// Functional component
function Greeting({ name, age = 0 }) {
  return (
    <div className="greeting">
      <h1>Hello, {name}!</h1>
      {age > 0 && <p>Age: {age}</p>}
    </div>
  );
}

// Arrow function component
const Button = ({ onClick, children, disabled = false }) => (
  <button onClick={onClick} disabled={disabled}>
    {children}
  </button>
);

// Component with TypeScript props
interface CardProps {
  title: string;
  description?: string;
  onClose: () => void;
}

const Card: React.FC<CardProps> = ({ title, description, onClose }) => (
  <div className="card">
    <h2>{title}</h2>
    {description && <p>{description}</p>}
    <button onClick={onClose}>Close</button>
  </div>
);

// JSX rules
// - className instead of class
// - htmlFor instead of for
// - Self-close empty tags: <img />, <br />
// - Expressions in curly braces: {variable}
// - Must return a single root element (or Fragment)

// Fragment (avoid extra DOM node)
return (
  <>
    <h1>Title</h1>
    <p>Paragraph</p>
  </>
);
```

---

## Core Hooks

The most commonly used React hooks.

```jsx
import { useState, useEffect, useRef } from "react";

// useState — local component state
function Counter() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState({ name: "", age: 0 });

  // Functional update (safe when new state depends on old)
  const increment = () => setCount(prev => prev + 1);

  // Update object state (spread to preserve other fields)
  const updateName = (name) => setUser(prev => ({ ...prev, name }));

  return <button onClick={increment}>{count}</button>;
}

// useEffect — side effects and lifecycle
function DataFetcher({ userId }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Runs after every render (no dependency array)
  });

  useEffect(() => {
    // Runs once on mount (empty dependency array)
    console.log("Mounted");
    return () => console.log("Unmounted");  // cleanup
  }, []);

  useEffect(() => {
    // Runs when userId changes
    let cancelled = false;
    setLoading(true);

    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(d => {
        if (!cancelled) {
          setData(d);
          setLoading(false);
        }
      });

    return () => { cancelled = true; };  // cleanup on re-run
  }, [userId]);

  if (loading) return <p>Loading...</p>;
  return <div>{data?.name}</div>;
}

// useRef — mutable ref, DOM access, persist values without re-render
function TextInput() {
  const inputRef = useRef(null);
  const renderCount = useRef(0);

  useEffect(() => {
    renderCount.current += 1;
  });

  const focusInput = () => inputRef.current?.focus();

  return (
    <>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus</button>
    </>
  );
}
```

---

## Additional Hooks

Hooks for complex state and optimization.

```jsx
import { useReducer, useCallback, useMemo } from "react";

// useReducer — complex state logic
const initialState = { count: 0, step: 1 };

function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + state.step };
    case "decrement":
      return { ...state, count: state.count - state.step };
    case "setStep":
      return { ...state, step: action.payload };
    case "reset":
      return initialState;
    default:
      throw new Error(`Unknown action: ${action.type}`);
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
      <button onClick={() => dispatch({ type: "reset" })}>Reset</button>
    </div>
  );
}

// useCallback — memoize function reference
function Parent() {
  const [count, setCount] = useState(0);

  // Without useCallback, this creates a new function on every render
  const handleClick = useCallback(() => {
    console.log("Clicked");
  }, []);  // stable reference — only recreated if deps change

  return <Child onClick={handleClick} />;
}

// useMemo — memoize expensive computation
function ExpensiveList({ items, filter }) {
  const filteredItems = useMemo(
    () => items.filter(item => item.name.includes(filter)),
    [items, filter]  // only recompute when items or filter changes
  );

  return <ul>{filteredItems.map(item => <li key={item.id}>{item.name}</li>)}</ul>;
}
```

---

## Event Handling

Handle user interactions in React.

```jsx
// Basic event handler
function Form() {
  const handleClick = (event) => {
    event.preventDefault();
    console.log("Clicked");
  };

  // Inline handler (fine for simple cases)
  return <button onClick={() => console.log("hi")}>Click</button>;
}

// Passing arguments to handlers
function List({ items }) {
  const handleDelete = (id) => {
    console.log("Delete", id);
  };

  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>
          {item.name}
          <button onClick={() => handleDelete(item.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}

// Common events
// onClick, onDoubleClick
// onChange, onInput, onSubmit
// onKeyDown, onKeyUp, onKeyPress
// onMouseEnter, onMouseLeave, onMouseMove
// onFocus, onBlur
// onScroll, onWheel
// onDragStart, onDrop

// Synthetic event properties
function InputHandler() {
  const handleChange = (e) => {
    console.log(e.target.value);    // input value
    console.log(e.target.checked);  // checkbox state
    console.log(e.target.name);     // input name attribute
  };

  return <input onChange={handleChange} />;
}
```

---

## Lists & Conditional Rendering

Render dynamic content.

```jsx
// Rendering lists — always use a stable key
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} — {user.email}
        </li>
      ))}
    </ul>
  );
}

// Conditional rendering patterns
function Status({ isLoading, error, data }) {
  // Early return
  if (isLoading) return <Spinner />;
  if (error) return <ErrorMessage message={error.message} />;

  // Ternary
  return (
    <div>
      {data ? <DataView data={data} /> : <EmptyState />}
    </div>
  );
}

// Short-circuit (&&)
function Notification({ message }) {
  return (
    <div>
      {message && <p className="notification">{message}</p>}
    </div>
  );
}

// Nullish coalescing for defaults
function Profile({ user }) {
  return <p>{user?.bio ?? "No bio provided."}</p>;
}
```

---

## Forms

Controlled and uncontrolled form patterns.

```jsx
// Controlled form (React manages state)
function LoginForm() {
  const [form, setForm] = useState({ email: "", password: "" });
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // validate and submit
    console.log(form);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        name="email"
        value={form.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <input
        type="password"
        name="password"
        value={form.password}
        onChange={handleChange}
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  );
}

// Uncontrolled form (DOM manages state)
function UncontrolledForm() {
  const emailRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(emailRef.current.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input ref={emailRef} type="email" defaultValue="" />
      <button type="submit">Submit</button>
    </form>
  );
}
```

---

## Context API

Share state across the component tree without prop drilling.

```jsx
import { createContext, useContext, useState } from "react";

// 1. Create context
const ThemeContext = createContext({
  theme: "light",
  toggleTheme: () => {},
});

// 2. Create provider
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");

  const toggleTheme = () =>
    setTheme(prev => (prev === "light" ? "dark" : "light"));

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// 3. Custom hook for consuming context
function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) throw new Error("useTheme must be used within ThemeProvider");
  return context;
}

// 4. Consume in any child component
function ThemedButton() {
  const { theme, toggleTheme } = useTheme();
  return (
    <button
      onClick={toggleTheme}
      className={`btn btn-${theme}`}
    >
      Toggle Theme
    </button>
  );
}

// 5. Wrap app
function App() {
  return (
    <ThemeProvider>
      <ThemedButton />
    </ThemeProvider>
  );
}
```

---

## Performance Optimization

Avoid unnecessary re-renders.

```jsx
import { memo, useCallback, useMemo, lazy, Suspense } from "react";

// React.memo — skip re-render if props unchanged
const ExpensiveChild = memo(function ExpensiveChild({ value }) {
  console.log("Rendered");
  return <div>{value}</div>;
});

// Lazy loading components
const HeavyComponent = lazy(() => import("./HeavyComponent"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}

// Key rules for performance
// 1. Don't create objects/arrays/functions inline in JSX if passed to memoized children
// 2. Use useCallback for event handlers passed as props
// 3. Use useMemo for expensive derived data
// 4. Use stable keys in lists (never use array index for dynamic lists)
// 5. Avoid deeply nested state — keep state as flat as possible
```

---

## Custom Hooks

Extract and reuse stateful logic.

```jsx
// useFetch — data fetching hook
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);

    fetch(url)
      .then(r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(d => { if (!cancelled) { setData(d); setLoading(false); } })
      .catch(e => { if (!cancelled) { setError(e); setLoading(false); } });

    return () => { cancelled = true; };
  }, [url]);

  return { data, loading, error };
}

// useLocalStorage — persist state in localStorage
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setStoredValue = (newValue) => {
    setValue(newValue);
    localStorage.setItem(key, JSON.stringify(newValue));
  };

  return [value, setStoredValue];
}

// useDebounce — delay value updates
function useDebounce(value, delay = 300) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// Usage
function SearchBar() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query, 400);
  const { data, loading } = useFetch(`/api/search?q=${debouncedQuery}`);

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      {loading ? <p>Searching...</p> : <Results data={data} />}
    </div>
  );
}
```
