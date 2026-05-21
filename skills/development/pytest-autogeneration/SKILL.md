---
name: pytest-autogeneration
description: 'Generate and maintain meaningful pytest coverage for Python code by detecting changes, adding missing tests, and validating real behavior.'
argument-hint: 'Paste the Python file or describe the module that needs pytest coverage'
---

# Pytest Auto-Generation & Maintenance

Automatically generate and maintain comprehensive pytest coverage for Python code. Detect code changes, update tests accordingly, and create test files from scratch when needed.

## Overview

This skill ensures the pytest suite stays in sync with the code by:
1. Detecting code changes (git-based with fallback to file inspection)
2. Identifying new or modified functions, classes, and methods
3. Writing or updating tests for:
   - **Happy path**: Normal usage and expected behavior
   - **Edge cases**: Boundary conditions, empty inputs, `None` values, limits
   - **Error cases**: Invalid inputs, exceptions, and error handling
4. Updating existing tests when the code changes
5. Creating a new test file from scratch if none exists
6. Running the relevant pytest command to verify the generated tests

## Core Testing Rules

- Write or update a **failing test first** when fixing behavior.
- Prefer assertions against **real behavior**, not mock-only placeholders.
- Mock only external boundaries you understand, such as network calls or third-party APIs.
- Keep tests independent, readable, and specific.
- Do not consider the work complete until `pytest` has been run successfully.

## 🚨 CRITICAL: Handling Test Failures

**When a test fails, ALWAYS determine the root cause:**

1. **If the test has a logical flaw** (wrong assertion, incorrect expectation):
   - ✅ Fix the test

2. **If the test is catching real code behavior** (code doesn't match test expectations):
   - ❌ **DO NOT automatically modify the test to make it pass**
   - ✅ **NOTIFY the user and ASK for permission to fix**
   - Explain what the code does vs what the test expects
   - Let the user decide if this is a bug to fix or intended behavior

3. **Never silently replace/remove a failing test**:
   - Always investigate why it failed
   - Always report findings to the user
   - Always ask before making changes to production code

**Example**:
```
Test failure detected in test_empty_string_key
- Test expects: File created as ".json" when key is empty string
- Actual behavior: File not created with empty string key
- This appears to be catching real code behavior, not a test flaw

Options:
1. Fix the code to handle empty string keys properly
2. Update the test to reflect intended behavior
3. Remove the test if empty strings are intentionally unsupported

Which would you prefer?
```

---

## Workflow

### Step 1: Detect Code Changes

#### Method 1: Git-Based Detection (Primary)

**Prerequisites**: Project must have git initialized and files committed

**Process**:
1. Run `git diff --name-only` to find changed files
2. Run `git diff <file>` to see what changed
3. Identify added/removed/modified functions/classes/methods
4. Skip unchanged files

**Command Reference**:
```bash
# See which files changed since last commit
git diff --name-only

# See exact changes in a file
git diff src/module.py

# Compare against specific commit
git diff HEAD~1 src/module.py

# Check unstaged changes only
git diff --unstaged
```

**Benefits**: Precise, shows exact line numbers and changes

#### Method 2: Fallback - Manual File Inspection

**When to use**: No git, files not committed, or git unavailable

**Process**:
1. Compare current test file with code file
2. Identify functions/classes in code that have no tests
3. Identify removed functions that have orphan tests
4. Look for TODOs or incomplete tests in existing test file

**What to check**:
- Does every public function have a test class/function?
- Are all parameters tested (different types, values)?
- Are error cases covered?
- Are edge cases present?

---

### Step 2: Analyze Code Structure

**For each changed/new item**:

#### Functions
Extract:
- Function name: `def foo(x: int, y: str) -> dict:`
- Parameters: types, defaults, annotations
- Return type
- Docstring (if exists)
- What it does (from code inspection)

#### Classes
Extract:
- Class name
- `__init__` signature and parameters
- Public methods
- Properties
- Class variables

#### Methods
Extract:
- Method name and type (instance, class, static)
- Parameters
- Return type
- What it modifies (instance state, etc.)

**Example**:
```python
# Code
def calculate_discount(price: float, discount_percent: int = 10) -> float:
    """Calculate discounted price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be 0-100")
    return price * (1 - discount_percent / 100)

# Analysis
- Name: calculate_discount
- Params: price (float), discount_percent (int, default=10)
- Return: float
- Exceptions: ValueError (2 cases)
- Happy path: Normal calculation
- Edge cases: discount_percent = 0, 100, boundary values
- Error cases: negative price, invalid discount
```

---

### Step 3: Generate Test Cases

#### Test Structure
```python
class Test<FunctionName>:
    """Test suite for <function_name>."""
    
    def test_happy_path_basic(self):
        """Normal usage with typical inputs."""
        
    def test_happy_path_variants(self):
        """Test different valid input combinations."""
        
    def test_edge_case_<case_name>(self):
        """Test boundary/edge case: <description>."""
        
    def test_error_case_<error_name>(self):
        """Test error handling for <error type>."""
```

#### Happy Path Tests
Test normal, expected behavior:
```python
def test_happy_path_basic(self):
    """Calculate discount with default percent."""
    result = calculate_discount(100)
    assert result == 90
    assert isinstance(result, float)

def test_happy_path_custom_discount(self):
    """Calculate discount with custom percent."""
    result = calculate_discount(100, 25)
    assert result == 75
```

#### Edge Case Tests
Test boundary conditions, empty values, limits:
```python
def test_edge_case_zero_discount(self):
    """No discount applied."""
    result = calculate_discount(100, 0)
    assert result == 100

def test_edge_case_max_discount(self):
    """Maximum discount (100%)."""
    result = calculate_discount(100, 100)
    assert result == 0

def test_edge_case_small_price(self):
    """Very small price value."""
    result = calculate_discount(0.01, 50)
    assert abs(result - 0.005) < 0.0001  # Float precision

def test_edge_case_zero_price(self):
    """Zero price."""
    result = calculate_discount(0, 50)
    assert result == 0
```

#### Error Case Tests
Test exception handling and invalid inputs:
```python
def test_error_case_negative_price(self):
    """Negative price raises ValueError."""
    with pytest.raises(ValueError, match="cannot be negative"):
        calculate_discount(-10, 10)

def test_error_case_discount_too_low(self):
    """Discount below 0 raises ValueError."""
    with pytest.raises(ValueError, match="0-100"):
        calculate_discount(100, -5)

def test_error_case_discount_too_high(self):
    """Discount above 100 raises ValueError."""
    with pytest.raises(ValueError, match="0-100"):
        calculate_discount(100, 150)
```

#### Class/Method Tests
For classes, test initialization and methods:
```python
class TestMyClass:
    """Test MyClass."""
    
    def test_init_with_defaults(self):
        """Initialize with default values."""
        obj = MyClass()
        assert obj.name == "default"
        assert obj.count == 0
    
    def test_init_with_custom_values(self):
        """Initialize with custom values."""
        obj = MyClass(name="custom", count=5)
        assert obj.name == "custom"
        assert obj.count == 5
    
    def test_method_happy_path(self):
        """Method works with normal inputs."""
        obj = MyClass(name="test")
        result = obj.process()
        assert result is not None
    
    def test_method_modifies_state(self):
        """Method correctly modifies instance state."""
        obj = MyClass(count=0)
        obj.increment()
        assert obj.count == 1
```

---

### Step 4: Update/Create Test File

#### If test file exists:
1. Parse existing test file
2. Find tests for changed functions
3. Update test cases (keep passing tests, update failing ones)
4. Add new test cases for new functions
5. Remove tests for deleted functions (if applicable)
6. Preserve any custom test logic/assertions

#### If test file doesn't exist:
1. Create new file: `tests/test_<module_name>.py`
2. Add imports: `import pytest`, necessary fixtures
3. Generate all test classes/functions
4. Add docstrings and comments

**File template**:
```python
"""Tests for <module_name> module."""

import pytest
from <package> import <function_or_class>

class Test<FunctionName>:
    """Test suite for <function_name>."""
    
    def test_<scenario>(self):
        """<Description of what is being tested>."""
        # Arrange
        # Act
        # Assert
```

---

### Step 5: Verify & Validate Tests

**Quality checks**:
- ✅ Tests run without errors (`pytest tests/`)
- ✅ Tests have meaningful names (describe what they test)
- ✅ Each test has a docstring explaining the scenario
- ✅ Assertions are specific (not just checking truthy/falsy)
- ✅ No test interdependencies (each test can run independently)
- ✅ Edge cases actually test boundaries
- ✅ Error tests use `pytest.raises()` correctly
- ✅ Fixtures are used for repeated setup when needed

**Run validation**:
```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest -v tests/

# Run specific test file
pytest tests/test_<module>.py

# Check coverage
pytest --cov=src tests/
```

---

## Quick Reference: Test Naming Patterns

| Scenario | Test Name Pattern | Example |
|----------|---|---|
| Normal usage | `test_happy_path_<variant>` | `test_happy_path_basic`, `test_happy_path_with_custom_values` |
| Edge case | `test_edge_case_<case_name>` | `test_edge_case_zero_value`, `test_edge_case_empty_list` |
| Error case | `test_error_case_<error_type>` | `test_error_case_invalid_input`, `test_error_case_negative_value` |
| Initialization | `test_init_<variant>` | `test_init_with_defaults`, `test_init_with_custom_values` |
| State change | `test_<method>_modifies_state` | `test_increment_modifies_state` |
| Type checking | `test_<method>_returns_correct_type` | `test_process_returns_dict` |

---

## Example: Complete Workflow

### Original Code
```python
# src/calculator.py
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

### Step 1: Detect Change
```bash
git diff src/calculator.py
# Shows: new function `add(a, b)`
```

### Step 2: Analyze
- Function: `add`
- Params: `a: int`, `b: int`
- Return: `int`
- Expected behavior: Sum two integers

### Step 3: Generate Tests
```python
class TestAdd:
    """Test suite for add function."""
    
    def test_happy_path_positive_numbers(self):
        """Add two positive integers."""
        result = add(2, 3)
        assert result == 5
        assert isinstance(result, int)
    
    def test_happy_path_negative_numbers(self):
        """Add negative integers."""
        result = add(-2, -3)
        assert result == -5
    
    def test_happy_path_mixed_signs(self):
        """Add mixed positive and negative."""
        result = add(5, -3)
        assert result == 2
    
    def test_edge_case_zero(self):
        """Add with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_edge_case_large_numbers(self):
        """Add very large integers."""
        result = add(999999999, 1)
        assert result == 1000000000
```

### Step 4: Create Test File
```bash
tests/test_calculator.py  # Created with all tests above
```

### Step 5: Validate
```bash
pytest tests/test_calculator.py -v
# All tests pass ✓
```

---

## When to Use This Skill

✅ **Use when**:
- New feature is implemented (function, class, method)
- Existing code is modified significantly
- Creating tests from scratch for new module
- Need to ensure test coverage stays up-to-date
- Refactoring code (tests ensure behavior didn't change)
- Before committing changes (validate with tests)

❌ **Skip when**:
- Tests already exist and cover all scenarios
- Code change is trivial (docstring only, comment only)
- Tests are auto-generated by CI already

---

## Integration Points

### Pre-commit Hook
Automatically run this before commits:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest-autogen
        name: Auto-generate/update tests
        entry: python scripts/autogen_tests.py
        language: python
        stages: [commit]
```

### CI/CD Pipeline
Run in CI to ensure tests exist for all code:
```yaml
# .github/workflows/test.yml
- name: Generate/Update Tests
  run: python scripts/autogen_tests.py

- name: Run Tests
  run: pytest tests/ -v --cov
```

### IDE Integration
Create VS Code task to auto-generate tests:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Generate Tests",
      "type": "shell",
      "command": "python scripts/autogen_tests.py",
      "group": "test"
    }
  ]
}
```

---

## Example Prompts

1. **"Generate pytest tests for this function and update if code changes"**
2. **"Create comprehensive tests for my new module, check git for changes"**
3. **"Detect code changes and auto-update the pytest file accordingly"**
4. **"Generate tests from scratch for this class with edge cases and error handling"**
5. **"Compare my code to tests and fill in missing test cases"**

---

## Related Skills to Combine

- **Code Formatting**: Format generated tests to match project standards
- **Documentation**: Add comprehensive docstrings to test functions
- **Coverage Analysis**: Check what % of code is tested and generate tests for uncovered lines
- **Performance Testing**: Generate performance/benchmark tests for critical functions