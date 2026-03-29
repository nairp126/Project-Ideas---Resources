# Tests

Property-based and unit tests that verify the structural correctness of this repository's content. Tests are written in Python using the `hypothesis` library.

## Test Files

| File | Description |
|------|-------------|
| [test_properties_14.py](./test_properties_14.py) | Property tests for content index completeness (Property 26) and directory README presence (Property 27) |

## Running Tests

Requires Python 3.10+ and the `hypothesis` and `pytest` packages:

```bash
pip install hypothesis pytest
pytest tests/
```

## Test Coverage

| Property | Description | Requirement |
|----------|-------------|-------------|
| 26 | Every markdown file has an entry in CONTENT_INDEX.md | 10.2 |
| 27 | Every directory contains a README.md | 10.3 |
