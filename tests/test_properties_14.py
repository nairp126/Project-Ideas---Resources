"""
Property tests for Task 14: Content index completeness and directory README presence.

Feature: project-enhancement
"""

import re
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

# Repository root is one level up from the tests/ directory
REPO_ROOT = Path(__file__).parent.parent

# Directories to exclude from all checks (tool/cache directories)
EXCLUDED_DIRS = {".git", ".github", ".kiro", ".pytest_cache", ".hypothesis", "__pycache__"}


def get_all_markdown_files():
    """Return all .md files in the repo, excluding internal tool directories."""
    md_files = []
    for path in REPO_ROOT.rglob("*.md"):
        parts = path.relative_to(REPO_ROOT).parts
        if not any(part in EXCLUDED_DIRS for part in parts):
            md_files.append(path)
    return md_files


def get_all_directories():
    """Return all directories in the repo, excluding .git, .github, .kiro internals."""
    dirs = []
    for path in REPO_ROOT.rglob("*"):
        if path.is_dir():
            parts = path.relative_to(REPO_ROOT).parts
            if not any(part in EXCLUDED_DIRS for part in parts):
                dirs.append(path)
    return dirs


def markdown_files_strategy():
    files = get_all_markdown_files()
    return st.sampled_from(files)


def directories_strategy():
    dirs = get_all_directories()
    return st.sampled_from(dirs)


# ---------------------------------------------------------------------------
# Property 26: Content index completeness
# Feature: project-enhancement, Property 26: Content index completeness
# For any valid state of the repository, every markdown file present in the
# repository shall have a corresponding entry in CONTENT_INDEX.md with a
# one-line description and a direct relative link.
# Validates: Requirements 10.2
# ---------------------------------------------------------------------------

CONTENT_INDEX_PATH = REPO_ROOT / "CONTENT_INDEX.md"


@given(md_file=markdown_files_strategy())
@settings(max_examples=len(get_all_markdown_files()))
def test_content_index_contains_every_markdown_file(md_file):
    """
    # Feature: project-enhancement, Property 26: Content index completeness
    Validates: Requirements 10.2
    """
    content_index = CONTENT_INDEX_PATH.read_text(encoding="utf-8")
    relative_path = md_file.relative_to(REPO_ROOT)

    # Normalise to forward slashes for link matching
    relative_str = relative_path.as_posix()

    # The CONTENT_INDEX.md itself is allowed to reference itself
    # Check that a markdown link to this file exists: [...](...relative_str...)
    link_pattern = re.compile(
        r"\[([^\]]+)\]\(" + re.escape(relative_str) + r"\)"
    )
    assert link_pattern.search(content_index), (
        f"CONTENT_INDEX.md is missing an entry for: {relative_str}"
    )


# ---------------------------------------------------------------------------
# Property 27: Directory README presence
# Feature: project-enhancement, Property 27: Directory README presence
# For any directory in the repository (excluding .git and .github internals),
# the directory shall contain a README.md file that describes its contents
# and links to all files within it.
# Validates: Requirements 10.3
# ---------------------------------------------------------------------------


@given(directory=directories_strategy())
@settings(max_examples=len(get_all_directories()))
def test_every_directory_has_readme(directory):
    """
    # Feature: project-enhancement, Property 27: Directory README presence
    Validates: Requirements 10.3
    """
    readme = directory / "README.md"
    assert readme.exists(), (
        f"Directory is missing a README.md: {directory.relative_to(REPO_ROOT)}"
    )
