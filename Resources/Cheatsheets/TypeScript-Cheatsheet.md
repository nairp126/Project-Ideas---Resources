# TypeScript Cheatsheet

A quick reference for TypeScript types, interfaces, generics, and advanced patterns.

## Table of Contents
- [Basic Types](#basic-types)
- [Interfaces & Type Aliases](#interfaces--type-aliases)
- [Functions](#functions)
- [Generics](#generics)
- [Union, Intersection & Utility Types](#union-intersection--utility-types)
- [Classes](#classes)
- [Type Narrowing & Guards](#type-narrowing--guards)
- [Modules & Declaration Files](#modules--declaration-files)
- [tsconfig Reference](#tsconfig-reference)

---

## Basic Types

TypeScript's primitive and structural types.

```typescript
// Primitives
const name: string = "Alice";
const age: number = 30;
const active: boolean = true;
const nothing: null = null;
const undef: undefined = undefined;
const sym: symbol = Symbol("id");
const big: bigint = 9007199254740991n;

// Arrays
const nums: number[] = [1, 2, 3];
const strs: Array<string> = ["a", "b"];
const pairs: [string, number][] = [["a", 1]];  // array of tuples

// Tuple
const point: [number, number] = [10, 20];
const labeled: [x: number, y: number] = [10, 20];

// Enum
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT",
}
const dir: Direction = Direction.Up;

// const enum (inlined at compile time)
const enum Status {
  Active,
  Inactive,
  Pending,
}

// any, unknown, never, void
let anything: any = "could be anything";
let safe: unknown = fetchData();  // must narrow before use
function throwError(msg: string): never { throw new Error(msg); }
function logMessage(msg: string): void { console.log(msg); }

// Literal types
type Direction2 = "north" | "south" | "east" | "west";
type StatusCode = 200 | 201 | 400 | 401 | 404 | 500;
```

---

## Interfaces & Type Aliases

Define the shape of objects and data structures.

```typescript
// Interface
interface User {
  readonly id: number;       // immutable
  name: string;
  email: string;
  age?: number;              // optional
  address?: {
    street: string;
    city: string;
  };
}

// Interface extension
interface Admin extends User {
  role: "admin" | "superadmin";
  permissions: string[];
}

// Interface merging (declaration merging)
interface Window {
  myCustomProp: string;
}

// Type alias
type Point = {
  x: number;
  y: number;
};

// Type alias for union
type ID = string | number;
type Result<T> = { success: true; data: T } | { success: false; error: string };

// Interface vs Type alias
// - Interface: use for object shapes, supports declaration merging
// - Type alias: use for unions, intersections, primitives, tuples

// Index signature (dynamic keys)
interface StringMap {
  [key: string]: string;
}

interface NumberMap {
  [key: string]: number;
  length: number;  // specific key must match index type
}

// Callable interface
interface Formatter {
  (value: string): string;
  locale: string;
}
```

---

## Functions

Typing function parameters, return values, and overloads.

```typescript
// Basic function types
function add(a: number, b: number): number {
  return a + b;
}

const multiply = (a: number, b: number): number => a * b;

// Optional and default parameters
function greet(name: string, greeting?: string): string {
  return `${greeting ?? "Hello"}, ${name}!`;
}

function createUser(name: string, role: string = "user"): User {
  return { id: Date.now(), name, email: "", role };
}

// Rest parameters
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}

// Function type alias
type Predicate<T> = (value: T) => boolean;
type Transformer<T, U> = (value: T) => U;

const isEven: Predicate<number> = n => n % 2 === 0;
const toString: Transformer<number, string> = n => String(n);

// Overloads
function format(value: string): string;
function format(value: number, decimals: number): string;
function format(value: string | number, decimals?: number): string {
  if (typeof value === "string") return value.trim();
  return value.toFixed(decimals ?? 2);
}

// this parameter
interface Button {
  label: string;
  onClick(this: Button): void;
}
```

---

## Generics

Write reusable, type-safe code.

```typescript
// Generic function
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

// Generic with constraint
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// Generic interface
interface Repository<T> {
  findById(id: number): Promise<T | null>;
  findAll(): Promise<T[]>;
  save(entity: T): Promise<T>;
  delete(id: number): Promise<void>;
}

// Generic class
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }

  get size(): number {
    return this.items.length;
  }
}

// Multiple type parameters
function zip<A, B>(a: A[], b: B[]): [A, B][] {
  return a.map((item, i) => [item, b[i]]);
}

// Default type parameter
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
  message: string;
}
```

---

## Union, Intersection & Utility Types

Compose and transform types.

```typescript
// Union type
type StringOrNumber = string | number;
type Status = "active" | "inactive" | "pending";

// Intersection type
type AdminUser = User & { permissions: string[] };

// Built-in utility types
interface Todo {
  id: number;
  title: string;
  completed: boolean;
  description: string;
}

// Partial — all properties optional
type PartialTodo = Partial<Todo>;

// Required — all properties required
type RequiredTodo = Required<Partial<Todo>>;

// Readonly — all properties immutable
type ReadonlyTodo = Readonly<Todo>;

// Pick — select subset of properties
type TodoPreview = Pick<Todo, "id" | "title">;

// Omit — exclude properties
type TodoWithoutId = Omit<Todo, "id">;

// Record — map keys to values
type PageMap = Record<string, Todo[]>;
const pages: Record<"home" | "about", string> = { home: "/", about: "/about" };

// Exclude / Extract
type T1 = Exclude<"a" | "b" | "c", "a">;  // "b" | "c"
type T2 = Extract<"a" | "b" | "c", "a" | "b">;  // "a" | "b"

// NonNullable
type T3 = NonNullable<string | null | undefined>;  // string

// ReturnType / Parameters
function fetchUser(): Promise<User> { /* ... */ return Promise.resolve({} as User); }
type FetchReturn = ReturnType<typeof fetchUser>;  // Promise<User>
type FetchParams = Parameters<typeof fetchUser>;  // []

// Conditional types
type IsArray<T> = T extends any[] ? true : false;
type Flatten<T> = T extends Array<infer U> ? U : T;
```

---

## Classes

TypeScript class features and access modifiers.

```typescript
class BankAccount {
  // Access modifiers
  public readonly id: string;
  private balance: number;
  protected owner: string;

  // Parameter shorthand
  constructor(
    public name: string,
    private initialBalance: number = 0
  ) {
    this.id = crypto.randomUUID();
    this.balance = initialBalance;
    this.owner = name;
  }

  // Getter / setter
  get currentBalance(): number {
    return this.balance;
  }

  set deposit(amount: number) {
    if (amount <= 0) throw new Error("Amount must be positive");
    this.balance += amount;
  }

  // Method
  withdraw(amount: number): boolean {
    if (amount > this.balance) return false;
    this.balance -= amount;
    return true;
  }

  // Static method
  static create(name: string, balance?: number): BankAccount {
    return new BankAccount(name, balance);
  }
}

// Abstract class
abstract class Shape {
  abstract area(): number;
  abstract perimeter(): number;

  describe(): string {
    return `Area: ${this.area()}, Perimeter: ${this.perimeter()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) { super(); }
  area(): number { return Math.PI * this.radius ** 2; }
  perimeter(): number { return 2 * Math.PI * this.radius; }
}

// Implementing interfaces
interface Serializable {
  serialize(): string;
  deserialize(data: string): void;
}

class Config implements Serializable {
  private data: Record<string, unknown> = {};
  serialize(): string { return JSON.stringify(this.data); }
  deserialize(data: string): void { this.data = JSON.parse(data); }
}
```

---

## Type Narrowing & Guards

Safely work with union types.

```typescript
// typeof narrowing
function process(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase();  // TypeScript knows it's string here
  }
  return value.toFixed(2);  // TypeScript knows it's number here
}

// instanceof narrowing
function handleError(error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  } else {
    console.error("Unknown error", error);
  }
}

// in operator narrowing
interface Cat { meow(): void; }
interface Dog { bark(): void; }

function makeSound(animal: Cat | Dog) {
  if ("meow" in animal) {
    animal.meow();
  } else {
    animal.bark();
  }
}

// Custom type guard
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

// Discriminated union
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; side: number }
  | { kind: "rectangle"; width: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":    return Math.PI * shape.radius ** 2;
    case "square":    return shape.side ** 2;
    case "rectangle": return shape.width * shape.height;
  }
}

// Assertion functions
function assertDefined<T>(value: T | null | undefined): asserts value is T {
  if (value == null) throw new Error("Value is null or undefined");
}
```

---

## Modules & Declaration Files

Organize TypeScript code and type third-party libraries.

```typescript
// Named exports
export interface Config { apiUrl: string; timeout: number; }
export function createConfig(url: string): Config { /* ... */ return { apiUrl: url, timeout: 5000 }; }
export const DEFAULT_TIMEOUT = 5000;

// Default export
export default class ApiClient { /* ... */ }

// Re-export
export { Config, createConfig } from "./config";
export * from "./utils";
export * as utils from "./utils";

// Import
import ApiClient from "./api-client";
import { Config, createConfig } from "./config";
import type { User } from "./types";  // type-only import (erased at runtime)

// Declaration file (.d.ts) for untyped JS library
declare module "my-untyped-lib" {
  export function doSomething(value: string): number;
  export interface Options {
    timeout?: number;
    retries?: number;
  }
}

// Augment existing module
declare module "express" {
  interface Request {
    user?: User;
  }
}
```

---

## tsconfig Reference

Common TypeScript compiler options.

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ES2022", "DOM"],
    "outDir": "./dist",
    "rootDir": "./src",

    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUncheckedIndexedAccess": true,

    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "resolveJsonModule": true,
    "allowJs": false,

    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,

    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```
