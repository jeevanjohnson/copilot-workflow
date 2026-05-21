---
name: code-formatting
description: 'Format code to modern standards across languages by cleaning imports, standardizing style, and adding type information where appropriate.'
argument-hint: 'Paste the code or describe the file you want cleaned up and formatted'
---

# Code Formatting

Automatically format code to modern standards across multiple languages. Apply import cleanup, style standardization, type annotations, and whitespace fixes where appropriate.

## Overview

This skill ensures code follows current best practices by systematically:
1. Removing unused imports (language-specific)
2. Organizing/sorting remaining imports
3. Applying consistent code style (spacing, line length, indentation)
4. Adding type hints/annotations where applicable
5. Fixing trailing whitespace and line endings

**Languages Supported**: Python, TypeScript/JavaScript, Go, Rust, Java, C++, C#, and others.

---

## Workflow

### Step 1: Identify Language and File Type
- **How**: Check file extension (`.py`, `.ts`, `.go`, `.rs`, `.java`, `.cpp`, `.cs`, etc.)
- **Why**: Different languages have different formatting rules and tools

### Step 2: Remove and Organize Imports

#### Python
- **Tool**: Use Pylance's `source.unusedImports` refactoring or manual inspection
- **Process**:
  1. Identify unused imports (not referenced in code)
  2. Remove them
  3. Organize into groups: stdlib → third-party → local
  4. Sort alphabetically within each group
- **Example**:
  ```python
  # Before
  from typing import Optional, Dict, List
  import os
  from pathlib import Path
  from my_module import helper
  import sys
  
  # After
  import os
  import sys
  from pathlib import Path
  from typing import Dict, List
  
  from my_module import helper
  ```

#### TypeScript/JavaScript
- **Tool**: ESLint with import sorting plugins, or Prettier
- **Process**:
  1. Remove unused imports (auto-fix with ESLint)
  2. Sort: React/defaults → third-party → local → type imports
  3. Organize into logical groups with blank lines
- **Example**:
  ```ts
  // Before
  import React from 'react';
  import { unused } from './utils';
  import express from 'express';
  import { helper } from './local';
  
  // After
  import React from 'react';
  import express from 'express';
  
  import { helper } from './local';
  ```

#### Go
- **Tool**: `goimports` (built-in formatting)
- **Process**: `goimports` automatically removes unused and organizes imports
- **Command**: `goimports -w file.go`

#### Rust
- **Tool**: `cargo fmt` + `cargo clippy --fix`
- **Process**: Automatically sorts use statements and removes dead code
- **Command**: `cargo fmt && cargo clippy --fix --allow-dirty`

#### Java
- **Tool**: IDE formatter or `google-java-format`
- **Process**: Remove unused imports via IDE analysis, organize by package
- **Command**: `google-java-format --replace file.java`

#### C++ / C#
- **Tool**: clang-format (C++) or dotnet format (C#)
- **Process**: Follow standard formatting, organize includes
- **Commands**: `clang-format -i file.cpp` or `dotnet format file.cs`

### Step 3: Apply Code Style Standards

#### Line Length & Indentation
- **Python**: 88 chars (Black standard), 4-space indent
- **TypeScript/JavaScript**: 100 chars, 2-space indent
- **Go**: 80 chars, tab indent
- **Rust**: 100 chars, 4-space indent
- **Java**: 120 chars, 4-space indent
- **C++**: 100 chars, 2/4-space indent
- **C#**: 120 chars, 4-space indent

#### Spacing Rules
- Remove trailing whitespace
- Use Unix line endings (`\n`, not `\r\n`)
- Single blank line between methods/functions
- Double blank line between classes

#### Consistent Formatting
- Consistent quote style (single vs double)
- Bracket placement (same line vs next line)
- Comment formatting

### Step 4: Add Type Annotations (Where Applicable)

#### Python
- Add type hints to function signatures and variables
- Use modern syntax: `str | None` instead of `Optional[str]` (Python 3.10+)
- **Tool**: Pylance's `source.addTypeAnnotation` refactoring
- **Example**:
  ```python
  # Before
  def process_data(data):
      result = {}
      return result
  
  # After
  def process_data(data: dict[str, Any]) -> dict[str, Any]:
      result: dict[str, Any] = {}
      return result
  ```

#### TypeScript/JavaScript
- Ensure all function parameters have types
- Use strict null checking
- **Example**:
  ```ts
  // Before
  function greet(name) { return `Hello, ${name}`; }
  
  // After
  function greet(name: string): string { return `Hello, ${name}`; }
  ```

#### Other Languages
- Go: Usually enforced by compiler
- Rust: Usually enforced by compiler (very strict)
- Java: Already statically typed
- C++: Add std types where helpful
- C#: Already statically typed

### Step 4.5: Handle `# type: ignore` Comments

**Important**: `# type: ignore` comments are intentional workarounds and should **NEVER be removed** during formatting.

#### Preservation Policy
- **Do NOT** remove or modify `# type: ignore` comments
- **Do NOT** assume they're unnecessary
- **Assume** they exist for valid reasons (e.g., third-party library type stubs, legitimate type system workarounds)

#### Flagging for Review
When formatting code that contains `# type: ignore` comments:
1. **Identify** all lines with `# type: ignore`
2. **Document** them in a separate list for manual review
3. **Flag** them with context:
   - Line number
   - The line of code
   - Reason if commented

**Example**:
```python
# Line 42: x = library.function()  # type: ignore
# ^ Third-party library has incomplete type stubs

# Line 87: result = cast(MyType, data)  # type: ignore
# ^ Intentional workaround for mypy limitation with generics
```

#### When to Question `# type: ignore`
Only suggest revisiting a `# type: ignore` if:
- The code has been significantly refactored since it was added
- A dependency update includes better type stubs
- The code can now be properly typed without the ignore

Otherwise: **preserve it as-is**.

### Step 5: Verify and Validate

**Quality Checks**:
- ✅ No unused imports
- ✅ Consistent indentation and spacing
- ✅ Code still compiles/passes syntax check
- ✅ No duplicate imports
- ✅ Organized import groups with blank lines
- ✅ Type annotations present where applicable
- ✅ Line length within limits
- ✅ No trailing whitespace
- 🚩 **Flag and document** all `# type: ignore` comments found (do not remove)
- 🚩 **List** locations of `# type: ignore` for manual review

**Validation**:
- Run linter (eslint, pylint, clippy, etc.)
- Run type checker if available
- Ensure existing tests still pass

---

## Quick Command Reference

| Language | Format Command | Import Tool | Type Checker |
|----------|---|---|---|
| Python | `black file.py` | `isort file.py` | `mypy file.py` |
| TypeScript | `prettier --write file.ts` | ESLint auto-fix | `tsc --noEmit` |
| JavaScript | `prettier --write file.js` | ESLint auto-fix | N/A |
| Go | `go fmt ./...` | `goimports -w file.go` | `go vet ./...` |
| Rust | `cargo fmt` | Built-in | `cargo check` |
| Java | `google-java-format -i file.java` | IDE | `javac -d /tmp file.java` |
| C++ | `clang-format -i file.cpp` | Manual | `clang-check file.cpp` |
| C# | `dotnet format file.cs` | IDE | `dotnet build` |

---

## When to Use This Skill

✅ **Use when**:
- Code has accumulated unused imports
- Mixed or inconsistent formatting
- Type hints are missing (Python)
- Onboarding code to a new project
- Preparing code for review
- Refactoring large files

❌ **Skip when**:
- Code is auto-formatted by CI/CD already
- Working on someone else's intentionally styled code
- Code is in pre-commit hooks (already automated)

---

## Integration Points

### IDE Integrations
- **VS Code**: Set up formatters in `.vscode/settings.json`:
  ```json
  {
    "[python]": { "editor.defaultFormatter": "ms-python.black-formatter" },
    "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
    "[go]": { "editor.defaultFormatter": "golang.go" }
  }
  ```

### Pre-commit Hooks
- Automate formatting before commits
- Example `.pre-commit-config.yaml`:
  ```yaml
  repos:
    - repo: https://github.com/psf/black
      rev: 23.1.0
      hooks:
        - id: black
    - repo: https://github.com/PyCQA/isort
      rev: 5.12.0
      hooks:
        - id: isort
  ```

### CI/CD
- Run formatters in CI pipeline
- Fail if code doesn't match standards
- Auto-commit fixes or reject PR

---

## Example Workflow: Python File

**Before**:
```python
from typing import Optional
import os
import sys
from pathlib import Path
import json
from my_app import config
from my_app import utils
from datetime import datetime

def process_file(filename):
    data = open(filename).read()
    processed = config.process(data)
    return processed
```

**After** (applying skill):
```python
from my_app import config


def process_file(filename: str) -> str:
    """Process a file and return the formatted result."""
    with open(filename, encoding="utf-8") as file_handle:
        data = file_handle.read()
    return config.process(data)
```

**Changes**:
1. ✅ Removed unused imports and kept only the required dependency
2. ✅ Simplified the import section for clarity
3. ✅ Added type hints: `filename: str`, `-> str`
4. ✅ Added a concise docstring
5. ✅ Improved file handling with a context manager
6. ✅ Fixed spacing and layout

---

## How to Invoke This Skill

Use when asked:
- "Format this code to modern standards"
- "Clean up imports and fix style"
- "Add type hints and organize this file"
- "Make this code production-ready"
- "Apply consistent formatting"

**Prompt example**:
```
Format this Python file to modern standards. Remove unused imports, 
organize remaining ones, add type hints, and fix spacing. Make it 
production-ready.
```

---

## Related Skills to Combine

- **Testing**: Ensure formatted code still passes tests
- **Documentation**: Update docstrings after formatting
- **Performance Optimization**: Sometimes formatting reveals inefficiencies
- **Linting**: Run linters after formatting for additional improvements