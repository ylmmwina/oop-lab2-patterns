# Code Documentation

This project uses Doxygen-style docstrings for Python code documentation.

## Purpose

The goal of code documentation is to explain the responsibilities of the main classes and methods used in the project.

The documentation is especially important because the project demonstrates GoF design patterns. Each major pattern-related class contains a docstring that explains its role.

## Documentation Style

Python classes and methods use docstrings with Doxygen tags.

Example:

```python
class Example:
    """
    @brief Short description of the class.

    Longer explanation of the class responsibility.

    Pattern: Example Pattern.
    """
```

Common tags used in the project:

| Tag | Meaning |
|---|---|
| `@brief` | Short description |
| `@param` | Function or method parameter |
| `@return` | Return value |
| `@throws` | Possible exception |

## Documented Source Files

| File | Documentation Focus |
|---|---|
| `main.py` | GUI application class |
| `core/db_manager.py` | SQLite database manager and Singleton |
| `core/questions.py` | Question model, Factory Method, Composite, Decorator |
| `core/tests.py` | Educational test model and Builder |
| `core/scoring.py` | Scoring strategies |
| `core/facade.py` | Facade for GUI interaction |
| `core/command.py` | Command pattern |
| `core/memento.py` | Memento pattern |
| `core/observer.py` | Observer pattern |
| `test_app.py` | Unit tests for core logic |

## How to Generate Documentation

Doxygen must be installed separately on the system.

To generate HTML documentation, run:

```bash
doxygen Doxyfile
```

Generated documentation will be placed in:

```text
docs/api/html/
```

The generated HTML files are not committed to the repository because they are build artifacts.

## Why Generated HTML Is Ignored

The repository contains:

- source code;
- Doxygen comments;
- `Doxyfile`.

This is enough to regenerate documentation.

The generated `docs/api/html/` directory is ignored to avoid committing large generated files.