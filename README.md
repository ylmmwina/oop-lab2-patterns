# EduPattern Studio

EduPattern Studio is a desktop educational task management application created for Object-Oriented Design Laboratory Work 2.

The project demonstrates the use of classic GoF design patterns in a Python application with a graphical user interface, data persistence, unit tests, and code documentation.

## Laboratory Work

**Course:** Object-Oriented Design  
**Laboratory Work:** Lab 2 — Design and development of programs using design patterns  
**Implementation language:** Python  
**GUI framework:** CustomTkinter  
**Data storage:** SQLite  
**Testing framework:** pytest  

## Project Idea

The application is based on the topic of an educational task support system.

It allows the user to:

- create a sample educational test;
- store test information in a local SQLite database;
- view saved tests through the graphical interface;
- demonstrate different object-oriented design patterns in the project structure;
- test the core business logic with unit tests.

## Implemented Requirements

| Requirement | Status | Implementation |
|---|---|---|
| Graphical user interface | Done | `main.py`, CustomTkinter |
| Data persistence | Done | `core/db_manager.py`, SQLite |
| Unit tests | Done | `test_app.py`, pytest |
| Design patterns | Done | 10 GoF patterns implemented |
| Code documentation | In progress | Doxygen-style Python docstrings |
| Project documentation | Done | `README.md`, `docs/patterns.md`, `docs/architecture.md` |

## Implemented Design Patterns

The project currently demonstrates 10 GoF design patterns.

| Category | Pattern | Location |
|---|---|---|
| Creational | Singleton | `core/db_manager.py` |
| Creational | Factory Method | `core/questions.py` |
| Creational | Builder | `core/tests.py` |
| Structural | Facade | `core/facade.py` |
| Structural | Composite | `core/questions.py` |
| Structural | Decorator | `core/questions.py` |
| Behavioral | Strategy | `core/scoring.py` |
| Behavioral | Command | `core/command.py` |
| Behavioral | Memento | `core/memento.py` |
| Behavioral | Observer | `core/observer.py` |

The project includes patterns from all three GoF categories:

- creational patterns;
- structural patterns;
- behavioral patterns.

## Project Structure

```text
.
├── core/
│   ├── __init__.py
│   ├── command.py
│   ├── db_manager.py
│   ├── facade.py
│   ├── memento.py
│   ├── observer.py
│   ├── questions.py
│   ├── scoring.py
│   └── tests.py
├── docs/
│   ├── architecture.md
│   └── patterns.md
├── main.py
├── requirements.txt
├── test_app.py
└── README.md
```

## How to Run the Application

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the desktop application:

```bash
python main.py
```

The application window allows the user to:

1. create and save a sample educational test;
2. view all saved tests from the SQLite database.

## How to Run Tests

Run all unit tests:

```bash
python -m pytest
```

Expected result:

```text
9 passed
```

## Main Components

### GUI

The graphical interface is implemented in `main.py` using CustomTkinter.

The GUI does not directly create tests or work with the database. Instead, it uses `EduSystemFacade`.

### Core Logic

The core logic is located in the `core/` package.

It contains:

- database manager;
- question models;
- test builder;
- scoring strategies;
- commands;
- memento-based session state;
- observer-based progress tracking;
- facade for GUI interaction.

### Tests

The file `test_app.py` contains unit tests for the core patterns and logic.

The tests check:

- Singleton behavior;
- question factory creation;
- test builder behavior;
- strict and loyal scoring strategies;
- composite question sections;
- question decorators;
- command execution and undo;
- memento save and restore;
- observer notifications.

## Notes

Local SQLite database files are not committed to the repository.

Ignored local files include:

- `edu_system.db`;
- `test.db`;
- `.venv/`;
- `__pycache__/`;
- `.pytest_cache/`;
- `.idea/`.