# Python Cheatsheet

A quick reference for Python syntax, built-ins, and common patterns.

## Table of Contents
- [Data Types & Variables](#data-types--variables)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Data Structures](#data-structures)
- [List & Dict Comprehensions](#list--dict-comprehensions)
- [File I/O](#file-io)
- [Error Handling](#error-handling)
- [Classes & OOP](#classes--oop)
- [Modules & Packages](#modules--packages)

---

## Data Types & Variables

Python's core types and how to work with them.

```python
# Numbers
x = 42          # int
y = 3.14        # float
z = 2 + 3j      # complex

# Strings
name = "Alice"
multi = """
Multi-line
string
"""
raw = r"C:\Users\name"   # raw string (no escape)

# String methods
"hello".upper()          # "HELLO"
"  hello  ".strip()      # "hello"
"a,b,c".split(",")       # ["a", "b", "c"]
",".join(["a", "b"])     # "a,b"
f"Hello, {name}!"        # f-string formatting
"{}!".format("Hello")    # .format()

# Boolean
is_active = True
is_done = False

# None
value = None

# Type checking
type(42)          # <class 'int'>
isinstance(42, int)  # True

# Type conversion
int("42")         # 42
float("3.14")     # 3.14
str(100)          # "100"
bool(0)           # False
bool("hello")     # True
```

---

## Control Flow

Conditionals, loops, and flow control.

```python
# if / elif / else
age = 20
if age < 13:
    print("child")
elif age < 18:
    print("teen")
else:
    print("adult")

# Ternary expression
label = "adult" if age >= 18 else "minor"

# for loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)

for item in ["a", "b", "c"]:
    print(item)

# enumerate (index + value)
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break, continue, else on loops
for n in range(10):
    if n == 3:
        continue   # skip 3
    if n == 7:
        break      # stop at 7
    print(n)

# match statement (Python 3.10+)
command = "quit"
match command:
    case "quit":
        print("Quitting")
    case "help":
        print("Help menu")
    case _:
        print("Unknown command")
```

---

## Functions

Define and call functions with various argument styles.

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# *args (variable positional)
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)   # 6

# **kwargs (variable keyword)
def display(**info):
    for key, val in info.items():
        print(f"{key}: {val}")

display(name="Alice", age=30)

# Type hints (Python 3.5+)
def add(a: int, b: int) -> int:
    return a + b

# Lambda (anonymous function)
square = lambda x: x ** 2
double = lambda x: x * 2

# Higher-order functions
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

from functools import reduce
product = reduce(lambda a, b: a * b, nums)  # 120

# Decorators
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def say_hello():
    print("Hello!")
```

---

## Data Structures

Lists, tuples, sets, and dictionaries.

```python
# List (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")
fruits.pop()           # remove last
fruits.pop(0)          # remove by index
fruits.sort()
fruits.reverse()
len(fruits)
"apple" in fruits      # True

# Tuple (immutable, ordered)
point = (10, 20)
x, y = point           # unpacking
a, *rest = (1, 2, 3, 4)  # a=1, rest=[2,3,4]

# Set (unique, unordered)
tags = {"python", "dev", "code"}
tags.add("open-source")
tags.discard("dev")
a = {1, 2, 3}
b = {2, 3, 4}
a | b   # union: {1, 2, 3, 4}
a & b   # intersection: {2, 3}
a - b   # difference: {1}

# Dictionary (key-value, ordered in 3.7+)
user = {"name": "Alice", "age": 30}
user["email"] = "alice@example.com"
user.get("phone", "N/A")   # safe access with default
user.keys()
user.values()
user.items()
del user["age"]
user.update({"age": 31, "city": "NYC"})
```

---

## List & Dict Comprehensions

Concise syntax for building collections.

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [item for sublist in [[1,2],[3,4]] for item in sublist]

# Dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}
inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}

# Generator expression (lazy, memory-efficient)
total = sum(x**2 for x in range(1000000))
```

---

## File I/O

Read and write files safely.

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Write to file
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

# Append to file
with open("log.txt", "a") as f:
    f.write("New log entry\n")

# Work with JSON
import json

with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Work with CSV
import csv

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])

with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
```

---

## Error Handling

Handle exceptions gracefully.

```python
# try / except / else / finally
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or value error: {e}")
else:
    print("No error occurred")
finally:
    print("Always runs")

# Raise an exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Custom exception
class AppError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

raise AppError("Something went wrong", code=500)

# Context manager for cleanup
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    try:
        yield
    finally:
        print("Releasing resource")

with managed_resource():
    print("Using resource")
```

---

## Classes & OOP

Object-oriented programming in Python.

```python
class Animal:
    # Class variable
    kingdom = "Animalia"

    def __init__(self, name: str, sound: str):
        self.name = name      # instance variable
        self._sound = sound   # convention: "protected"

    def speak(self) -> str:
        return f"{self.name} says {self._sound}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r})"

    @classmethod
    def from_dict(cls, data: dict) -> "Animal":
        return cls(data["name"], data["sound"])

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name and name.isalpha())


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, "woof")
        self.breed = breed

    def speak(self) -> str:
        return f"{super().speak()} ({self.breed})"


# Dataclass (Python 3.7+)
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "point"
    tags: list = field(default_factory=list)

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5
```

---

## Modules & Packages

Import and organize code.

```python
# Import module
import os
import sys

# Import specific names
from pathlib import Path
from datetime import datetime, timedelta

# Import with alias
import numpy as np
import pandas as pd

# Useful standard library modules
import os
os.getcwd()
os.listdir(".")
os.path.join("dir", "file.txt")
os.path.exists("file.txt")
os.makedirs("new/dir", exist_ok=True)

import sys
sys.argv          # command-line arguments
sys.exit(0)       # exit with code

from pathlib import Path
p = Path("data/file.txt")
p.parent          # Path("data")
p.stem            # "file"
p.suffix          # ".txt"
p.read_text()
p.write_text("content")
list(Path(".").glob("**/*.py"))

import re
re.search(r"\d+", "abc123")
re.findall(r"\w+", "hello world")
re.sub(r"\s+", " ", "too   many   spaces")

from datetime import datetime
now = datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")
datetime.strptime("2024-01-15", "%Y-%m-%d")
```
