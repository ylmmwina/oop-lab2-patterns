# Architecture Overview

This document describes the current architecture of EduPattern Studio.

EduPattern Studio is a small desktop application for educational task management. The main purpose of the project is to demonstrate the use of GoF design patterns in a realistic Python application with GUI, persistence, tests, and documentation.

## System Purpose

The application supports basic work with educational tests.

The current version can:

- create a sample educational test;
- save test metadata to SQLite;
- show saved tests in the graphical interface;
- demonstrate 10 GoF design patterns;
- test the core business logic with pytest.

## High-Level Architecture

The project is divided into three main layers:

```text
GUI Layer
   |
   v
Facade Layer
   |
   v
Core Domain and Persistence Layer
```

## GUI Layer

**File:** `main.py`

The GUI layer is implemented with CustomTkinter.

Responsibilities:

- create the main application window;
- display buttons and text output;
- receive user actions;
- call the facade;
- show operation results.

The GUI does not directly create tests and does not directly execute SQL queries.

## Facade Layer

**File:** `core/facade.py`

The facade layer provides a simple API for the GUI.

Main class:

```text
EduSystemFacade
```

Responsibilities:

- coordinate test creation;
- use the test builder;
- save created tests;
- return saved tests to the GUI.

This layer hides internal implementation details from the graphical interface.

## Core Domain Layer

The domain layer contains educational task and test logic.

| File | Responsibility |
|---|---|
| `core/questions.py` | Question types, sections, decorators, and question factory |
| `core/tests.py` | Educational test model and test builder |
| `core/scoring.py` | Scoring algorithms |
| `core/command.py` | User action commands |
| `core/memento.py` | Session state saving and restoring |
| `core/observer.py` | Progress notification mechanism |

## Persistence Layer

**File:** `core/db_manager.py`

The persistence layer uses SQLite.

Responsibilities:

- create database tables;
- execute SQL queries;
- fetch saved tests.

The current database stores basic test metadata:

```text
id
title
max_score
```

Local database files are ignored by Git.

## Data Flow

### Creating a Test

```text
User clicks "Create and save test"
   |
   v
EduApp.create_test()
   |
   v
EduSystemFacade.create_and_save_test()
   |
   v
EducationalTestBuilder creates the test object
   |
   v
DBManager saves test metadata
   |
   v
GUI displays the result
```

### Showing Saved Tests

```text
User clicks "Show saved tests"
   |
   v
EduApp.show_saved_tests()
   |
   v
EduSystemFacade.get_saved_tests()
   |
   v
DBManager fetches rows from SQLite
   |
   v
GUI displays saved tests
```

## Testing Approach

The project uses unit tests for the core logic.

Test file:

```text
test_app.py
```

The tests check:

- Singleton behavior;
- Factory Method question creation;
- Builder test creation;
- Strategy scoring algorithms;
- Composite question sections;
- Decorator behavior;
- Command execution and undo;
- Memento save and restore;
- Observer notifications.

GUI tests are not included because the basic laboratory requirements focus on core logic tests.

## Design Principles

The project follows these principles:

- separation of GUI and business logic;
- simple layered architecture;
- single responsibility for core classes;
- encapsulation of object creation;
- interchangeable scoring algorithms;
- testable domain logic;
- local persistence through a small database manager.

## Current Limitations

The implementation is intentionally compact.

Current limitations:

- the GUI creates only a predefined sample test;
- the database stores only test metadata;
- full question data is not persisted yet;
- there is no real student account system;
- reports and exports are not implemented yet.

## Possible Future Improvements

Possible improvements:

- add GUI forms for creating custom questions;
- save full question structures to the database;
- add student answer sessions;
- add score calculation in the GUI;
- add export to CSV or PDF;
- add UML diagrams;
- generate HTML documentation with Doxygen.

## Conclusion

EduPattern Studio has a layered architecture suitable for a small educational desktop application.

The structure is simple enough for a laboratory project, but it still demonstrates realistic use of design patterns, persistence, GUI interaction, and unit testing.