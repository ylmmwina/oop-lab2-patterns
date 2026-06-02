# Design Patterns Catalog

This document describes the GoF design patterns implemented in EduPattern Studio.

The project demonstrates design patterns in the context of an educational task management desktop application.

## Pattern Summary

| # | Pattern | Category | File | Purpose |
|---|---|---|---|---|
| 1 | Singleton | Creational | `core/db_manager.py` | Provides one shared database manager |
| 2 | Factory Method | Creational | `core/questions.py` | Creates questions by type |
| 3 | Builder | Creational | `core/tests.py` | Builds educational tests step by step |
| 4 | Facade | Structural | `core/facade.py` | Provides a simple interface for the GUI |
| 5 | Composite | Structural | `core/questions.py` | Represents questions and question sections uniformly |
| 6 | Decorator | Structural | `core/questions.py` | Adds extra behavior to questions |
| 7 | Strategy | Behavioral | `core/scoring.py` | Supports different scoring algorithms |
| 8 | Command | Behavioral | `core/command.py` | Encapsulates user answer actions |
| 9 | Memento | Behavioral | `core/memento.py` | Saves and restores test session state |
| 10 | Observer | Behavioral | `core/observer.py` | Notifies progress trackers about events |

## 1. Singleton

**Location:** `core/db_manager.py`

`DBManager` is implemented as a Singleton.

The application needs one shared object responsible for the SQLite connection. This avoids unnecessary duplicate database connections and gives other components a simple way to access persistence logic.

**Problem solved:**  
Without Singleton, different parts of the application could create multiple database managers and multiple database connections.

**Advantages:**

- one shared database access point;
- simple access from the facade;
- reduced duplication of database setup logic.

**Disadvantages:**

- global shared state should be used carefully;
- tests may require attention when database state is shared.

## 2. Factory Method

**Location:** `core/questions.py`

`QuestionFactory` creates question objects based on the question type.

Currently supported types:

- `choice`;
- `text`.

**Problem solved:**  
The client code does not need to know exact class names such as `ChoiceQuestion` or `TextQuestion`.

**Advantages:**

- easier creation of different question types;
- simpler extension with new question classes;
- reduced conditional logic in client code.

**Disadvantages:**

- the factory must be updated when new question types are added.

## 3. Builder

**Location:** `core/tests.py`

`EducationalTestBuilder` constructs an educational test step by step.

It allows setting:

- test title;
- choice questions;
- text questions;
- maximum score.

**Problem solved:**  
Creating a test object may require several steps. Builder keeps this process readable and organized.

**Advantages:**

- clear step-by-step object construction;
- readable chained calls;
- easier future extension.

**Disadvantages:**

- more classes than direct object construction.

## 4. Facade

**Location:** `core/facade.py`

`EduSystemFacade` provides a simplified interface for the GUI.

The GUI calls facade methods instead of directly using:

- database manager;
- test builder;
- question factory;
- internal domain objects.

**Problem solved:**  
Without Facade, the GUI would know too much about internal system structure.

**Advantages:**

- simpler GUI code;
- better separation between interface and core logic;
- easier future replacement of internal components.

**Disadvantages:**

- the facade can become too large if too many responsibilities are added.

## 5. Composite

**Location:** `core/questions.py`

`QuestionComponent` is the base abstraction for both individual questions and question sections.

`QuestionSection` can contain multiple question components.

**Problem solved:**  
The system can treat a single question and a group of questions in a uniform way.

**Advantages:**

- supports nested task structures;
- useful for tests with sections;
- allows common operations such as `display()`.

**Disadvantages:**

- may be unnecessary for very small tests without sections.

## 6. Decorator

**Location:** `core/questions.py`

`QuestionDecorator` wraps a question component.

`TimedQuestion` adds a time limit to an existing question without modifying the original question class.

**Problem solved:**  
Extra behavior can be added without changing existing question classes.

**Advantages:**

- flexible extension of question behavior;
- avoids subclass explosion;
- decorators can be combined later.

**Disadvantages:**

- decorated objects may be harder to inspect during debugging.

## 7. Strategy

**Location:** `core/scoring.py`

`ScoringStrategy` defines a common interface for scoring algorithms.

Implemented strategies:

- `StrictScoring`;
- `LoyalScoring`.

**Problem solved:**  
Different scoring rules can be changed without modifying the code that uses scoring.

**Advantages:**

- interchangeable algorithms;
- clear separation of scoring logic;
- easy to add new strategies.

**Disadvantages:**

- may be excessive if only one scoring rule is ever needed.

## 8. Command

**Location:** `core/command.py`

`AnswerCommand` represents the action of answering a question.

It supports:

- `execute()`;
- `undo()`.

**Problem solved:**  
User actions can be represented as objects and later undone.

**Advantages:**

- supports undo functionality;
- separates action logic from UI;
- can be extended to command history.

**Disadvantages:**

- small actions require additional classes.

## 9. Memento

**Location:** `core/memento.py`

`SessionMemento` stores a snapshot of the session state.

`ExamSession` can save and restore its state.

`SessionCaretaker` keeps saved snapshots.

**Problem solved:**  
The application can save and restore progress during a test session.

**Advantages:**

- state restoration without exposing internal details;
- useful for future autosave functionality;
- works well with command history.

**Disadvantages:**

- storing many snapshots can increase memory usage.

## 10. Observer

**Location:** `core/observer.py`

`Subject` notifies attached observers.

`ProgressTracker` receives progress messages.

**Problem solved:**  
Objects can react to events without being tightly coupled to the object that produces those events.

**Advantages:**

- loose coupling between event source and listeners;
- easy to add new observers;
- useful for progress logs and GUI updates.

**Disadvantages:**

- event flow can become harder to trace in larger systems.

## Conclusion

The current implementation includes 10 GoF design patterns from all three required categories:

- creational;
- structural;
- behavioral.

The selected patterns are connected to the actual application domain and are not isolated artificial examples.