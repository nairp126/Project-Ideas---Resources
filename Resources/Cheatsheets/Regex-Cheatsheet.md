# Regex Cheatsheet

A quick reference for regular expression syntax, character classes, and common patterns.

## Table of Contents
- [Basic Syntax](#basic-syntax)
- [Character Classes & Shorthand](#character-classes--shorthand)
- [Quantifiers](#quantifiers)
- [Anchors & Boundaries](#anchors--boundaries)
- [Groups & Capturing](#groups--capturing)
- [Lookahead & Lookbehind](#lookahead--lookbehind)
- [Flags & Modifiers](#flags--modifiers)
- [Common Patterns](#common-patterns)
- [Language Examples](#language-examples)

---

## Basic Syntax

Fundamental regex building blocks.

```text
.       Any character except newline
\       Escape special character (e.g., \. matches literal dot)
|       Alternation (OR): cat|dog matches "cat" or "dog"
[abc]   Character class: matches a, b, or c
[^abc]  Negated class: matches anything except a, b, or c
[a-z]   Range: matches any lowercase letter
[A-Z]   Range: matches any uppercase letter
[0-9]   Range: matches any digit
```

---

## Character Classes & Shorthand

Predefined sets of characters.

```text
\d      Digit: [0-9]
\D      Non-digit: [^0-9]
\w      Word character: [a-zA-Z0-9_]
\W      Non-word character: [^a-zA-Z0-9_]
\s      Whitespace: [ \t\n\r\f\v]
\S      Non-whitespace
\b      Word boundary (zero-width)
\B      Non-word boundary (zero-width)
\n      Newline
\t      Tab
\r      Carriage return
```

```text
# Examples
\d{3}       Three digits: "123"
\w+         One or more word chars: "hello_world"
\s+         One or more whitespace chars
[a-zA-Z]+   One or more letters
[^,]+       One or more non-comma chars (useful for CSV)
```

---

## Quantifiers

Control how many times a pattern repeats.

```text
*       Zero or more (greedy)
+       One or more (greedy)
?       Zero or one (optional)
{n}     Exactly n times
{n,}    At least n times
{n,m}   Between n and m times (inclusive)

# Lazy (non-greedy) — add ? after quantifier
*?      Zero or more (lazy)
+?      One or more (lazy)
{n,m}?  Between n and m (lazy)
```

```text
# Greedy vs Lazy example
Input: "<b>bold</b> and <i>italic</i>"

<.+>    Greedy: matches entire "<b>bold</b> and <i>italic</i>"
<.+?>   Lazy:   matches "<b>", then "</b>", then "<i>", then "</i>"

# Quantifier examples
\d{4}       Exactly 4 digits: "2024"
\d{2,4}     2 to 4 digits: "24", "240", "2024"
colou?r     Matches "color" or "colour"
https?      Matches "http" or "https"
```

---

## Anchors & Boundaries

Match positions, not characters.

```text
^       Start of string (or line in multiline mode)
$       End of string (or line in multiline mode)
\b      Word boundary
\B      Non-word boundary
\A      Start of string (not affected by multiline)
\Z      End of string (not affected by multiline)
```

```text
# Examples
^Hello          Matches "Hello" only at start of string
world$          Matches "world" only at end of string
^\d{5}$         Matches exactly a 5-digit string (e.g., ZIP code)
\bcat\b         Matches "cat" but not "catch" or "concatenate"
\Bcat\B         Matches "cat" inside a word like "concatenate"

# Multiline mode (m flag)
^line           Matches "line" at start of each line
end$            Matches "end" at end of each line
```

---

## Groups & Capturing

Group patterns and capture matched text.

```text
(abc)       Capturing group: captures "abc"
(?:abc)     Non-capturing group: groups without capturing
(?<name>)   Named capturing group
\1          Backreference to group 1
\k<name>    Backreference to named group
```

```text
# Capturing group examples
(\d{4})-(\d{2})-(\d{2})
  Matches "2024-01-15", captures: group1="2024", group2="01", group3="15"

(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})
  Named groups: year="2024", month="01", day="15"

# Non-capturing group (grouping without capturing)
(?:https?|ftp)://\S+
  Matches URLs starting with http, https, or ftp

# Backreference (match repeated text)
(\w+)\s+\1
  Matches repeated words like "the the" or "hello hello"

# Alternation within group
(cat|dog|bird)
  Matches "cat", "dog", or "bird"
```

---

## Lookahead & Lookbehind

Assert context without consuming characters.

```text
(?=...)     Positive lookahead: followed by ...
(?!...)     Negative lookahead: NOT followed by ...
(?<=...)    Positive lookbehind: preceded by ...
(?<!...)    Negative lookbehind: NOT preceded by ...
```

```text
# Lookahead examples
\d+(?= dollars)
  Matches digits followed by " dollars": "100" in "100 dollars"

\d+(?! dollars)
  Matches digits NOT followed by " dollars"

# Lookbehind examples
(?<=\$)\d+
  Matches digits preceded by "$": "100" in "$100"

(?<!\$)\d+
  Matches digits NOT preceded by "$"

# Combined example: password validation
^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$
  Requires: uppercase, lowercase, digit, special char, min 8 chars
```

---

## Flags & Modifiers

Modify regex behavior.

```text
i   Case-insensitive: /hello/i matches "Hello", "HELLO", "hello"
g   Global: find all matches (not just first)
m   Multiline: ^ and $ match start/end of each line
s   Dotall: . matches newline characters too
u   Unicode: enable full Unicode support
y   Sticky: match only at lastIndex position
```

```text
# Flag examples (JavaScript syntax)
/hello/i        Case-insensitive match
/\d+/g          Find all digit sequences
/^line/m        Match "line" at start of each line
/foo.bar/s      . matches newline (dotall mode)

# Python syntax
import re
re.search(r"hello", text, re.IGNORECASE)
re.findall(r"\d+", text)
re.search(r"^line", text, re.MULTILINE)
re.search(r"foo.bar", text, re.DOTALL)
re.search(r"hello", text, re.IGNORECASE | re.MULTILINE)
```

---

## Common Patterns

Ready-to-use regex patterns for everyday tasks.

```text
# Email address (simplified)
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

# URL
https?://(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_+.~#?&/=]*

# IPv4 address
^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$

# Phone number (US, flexible)
^\+?1?\s?[\(]?\d{3}[\)]?[\s.\-]?\d{3}[\s.\-]?\d{4}$

# Date (YYYY-MM-DD)
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$

# Time (HH:MM or HH:MM:SS)
^([01]\d|2[0-3]):([0-5]\d)(?::([0-5]\d))?$

# ZIP code (US 5-digit or ZIP+4)
^\d{5}(?:-\d{4})?$

# Credit card (basic 16-digit)
^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$

# Hex color
^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$

# Slug (URL-friendly string)
^[a-z0-9]+(?:-[a-z0-9]+)*$

# Username (3-20 chars, alphanumeric + underscore)
^[a-zA-Z0-9_]{3,20}$

# Strong password (min 8 chars, upper, lower, digit, special)
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$

# HTML tag (basic)
<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>(.*?)</\1>

# Whitespace normalization
\s+   (replace with single space)

# Extract numbers from string
-?\d+(?:\.\d+)?
```

---

## Language Examples

Using regex in popular programming languages.

```python
# Python
import re

text = "Hello, my email is alice@example.com and bob@test.org"

# Search (first match)
match = re.search(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", text)
if match:
    print(match.group())  # alice@example.com

# Find all matches
emails = re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", text)
# ["alice@example.com", "bob@test.org"]

# Substitute
clean = re.sub(r"\s+", " ", "too   many   spaces")

# Split
parts = re.split(r"[,;]\s*", "a, b; c,d")

# Named groups
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "2024-01-15")
m.group("year")   # "2024"

# Compile for reuse
pattern = re.compile(r"\d+", re.IGNORECASE)
pattern.findall("abc 123 def 456")
```

```javascript
// JavaScript
const text = "Hello, my email is alice@example.com";

// Test (boolean)
/\d+/.test("abc123");  // true

// Match (first or all with g flag)
"abc123def456".match(/\d+/);   // ["123"]
"abc123def456".match(/\d+/g);  // ["123", "456"]

// Replace
"hello world".replace(/\b\w/g, c => c.toUpperCase());  // "Hello World"

// Split
"a, b; c".split(/[,;]\s*/);  // ["a", "b", "c"]

// Named groups
const m = "2024-01-15".match(/(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/);
m.groups.year;  // "2024"

// matchAll (all matches with groups)
const matches = [...text.matchAll(/(\w+)@(\w+)/g)];
```

```bash
# Bash (grep, sed, awk)

# grep with extended regex
grep -E "^\d{4}-\d{2}-\d{2}$" dates.txt

# grep with Perl-compatible regex
grep -P "\d{4}-\d{2}-\d{2}" log.txt

# sed substitution
sed 's/[0-9]\{4\}/XXXX/g' file.txt          # basic regex
sed -E 's/[0-9]{4}/XXXX/g' file.txt         # extended regex

# awk pattern matching
awk '/^ERROR/' app.log
awk '/\d{3}-\d{4}/ {print $0}' contacts.txt
```
