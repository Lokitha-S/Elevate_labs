# Python Developer Internship - Task Submissions 🚀

This repository contains the tasks completed during my Python Developer Internship, starting January 15, 2026.

---

## 📅 Task 1: Environment Setup & First Script
**File:** `hello_world.py`  
**Date:** 15/01/26

### Description
Setup of the Python development environment and creation of an interactive script to handle basic user identification.

### Key Objectives:
- **Variable Storage:** Storing user information in variables instead of hardcoding strings.
- **Dynamic Input:** Modified the script to accept `input()` from the terminal for Name and Role.
- **Execution Flow:** Learned to trigger scripts directly from the macOS terminal.
- **Readability:** Implemented line-by-line commenting to establish best practices.

---

## 🔢 Task 2: Data Types & Operations Demo
**File:** `datatypes_demo.py`
**Date:** 16/01/26

### Description
A deep dive into how Python manages memory and data through dynamic typing and mathematical operations.

### 🚀 Features
- **Variable Management:** Declaration and type checking for `int`, `float`, `str`, and `bool`.
- **Dynamic Typing:** Demonstration of how Python reassigns variable types at runtime.
- **Data Conversion:** Practical examples of casting string inputs into numeric types using `int()` and `float()`.
- **Arithmetic Logic:** Execution of Addition, Subtraction, Multiplication, and Division.
- **Concatenation:** Best practices for joining strings with numeric data using `str()` and f-strings.

## 📊 Task 3: Logical Operations & Grade Calculator
**File:** `grade_calculator.py` | **Date:** 19/01/26

### Description
Developed a multi-subject grade calculator that applies real-world business rules using conditional logic.

### 🚀 Features
- **Multi-Subject Input:** Collects marks for Math, Science, Social, and English.
- **Logical Operators:** Used `and` and `or` to define complex grading boundaries (e.g., `sum > 35 or sum == 40`).
- **Nested Conditions:** Implemented a "Just Pass" rule for specific total marks and a failure identification system.
- **Data Validation:** Included logic to ensure inputs are within valid numeric ranges (0-100).
- **Refactored Code:** Cleaned up logic for high readability and efficient execution.

## 🔁 Task 4: Loops & Control Flow
**File:** `loop_tasks.py`  | **Date:** 20/01/26

### Description
Explored the automation power of loops, transitioning from basic iteration to real-world simulation systems.

### 🚀 Features
- **Iterative Sequences:** Used `for` loops and `range(start, stop, step)` to handle fixed datasets.
- **Dynamic Conditions:** Implemented `while` loops for countdown timers and interactive menu systems.
- **Loop Control:** Applied `break` to exit loops upon meeting conditions and `continue` to filter/skip data.
- **Real-World Application:** Developed an **ATM Withdrawal System** that utilizes a `while True` loop for continuous input validation and a `for` loop to calculate currency denominations (500, 200, 100 notes).

## 🛠️ Task 5: Modular Programming with Functions
**File:** `calculator.py` | **Date:** 22/01/26

### Description
Transitioned from linear scripting to procedural programming by building a modular calculator.

### 🚀 Features
- **Functional Isolation:** Created independent functions for `add`, `subtract`, `multiply`, and `divide`.
- **Default Arguments:** Implemented default parameters to handle cases where a second input is missing.
- **Error Resilience:** Added specific logic to prevent "Division by Zero" crashes.
- **Documentation:** Used Python Docstrings to explain the purpose and parameters of every function.
- **Return Logic:** Used `return` values to separate calculation logic from user interface (display) logic.

## Task 6: Advanced Collection Management
**Status:** Completed ✅

- Successfully implemented List deduplication via Set casting.
- Conducted Set Theory analysis (Union, Intersection, Difference).
- Verified data integrity protocols using Immutable Tuples.

## 📁 Task 7: Data Serialization with JSON
**File:** `student_records.py`  
**Date:** 26/01/26

### 🚀 Key Implementations
* **Nested Dictionaries:** Structured complex student data using unique keys to represent a relational database format.
* **JSON Serialization:** Utilized the `json` library (`json.dump()` and `json.load()`) to achieve persistent storage.
* **File Handling:** Implemented robust file I/O operations to maintain data consistency in `student_records.json`.
* **Data Formatting:** Applied advanced f-string alignment techniques to generate professional, tabular terminal reports.


## 📁 Task 8: File I/O and Content Persistence
**Files:** `task8.py`, `fight_club_summary.txt`, `character_database.csv`
**Date:** 27/01/26


### 🚀 Key Implementations
* **Text Processing:** Successfully wrote and appended extensive string data to local text files.
* **Structured Data:** Leveraged the `csv` module to map character profiles into a tabular format.
* **Context Management:** Used the `with` keyword to ensure proper resource closing (Step 9 requirement).
* **Fault Tolerance:** Implemented a robust `try-except-finally` hierarchy to handle I/O failures.

### 🛠️ Technical Skills
* **File Stream Modes:** Applied `'w'` for initialization, `'a'` for metadata updates, and `'r'` for retrieval.
* **Data Parsing:** Iterated through CSV objects to generate human-readable terminal reports.

## Task 9: Error Handling and Logging
**File:** `error_handling.py`,`errors.log`,`Task9.png`
**Date:** 29/01/26


### What I did:
* **Try-Except:** Caught specific errors so the program doesn't crash.
* **Logging:** Saved errors to a file called `errors.log` instead of just printing them.
* **Else/Finally:** Used `else` for successful runs and `finally` for a clean finish.
* **Custom Messages:** Created easy-to-read error messages for the user.


## 📁 Task 10: Object-Oriented Programming (OOP)
**File:** `bank_account.py`
**Date:** 30/01/26
### 🚀 Key Implementations
* **Encapsulation:** Used private variables (`__balance`) to protect sensitive data from direct access.
* **Inheritance:** Created a specialized `Savings` class that inherits logic from a base `Bank` class.
* **Method Overriding:** Customised the `display` method in the child class to provide more specific data.
* **Abstraction:** Simulated real-world banking operations (deposit, withdraw) through method calls.

### 🛠️ Technical Skills
* **Constructors:** Used `__init__` for object initialization.
* **Super():** Utilized `super()` to call parent class constructors.
* **Object Mapping:** Managed multiple distinct objects with unique states.


## 📁 Task 11: Regex Validation System
**File:** `regex_validation.py`
**Date:** 03/02/26

A centralized Python utility for validating common user inputs using Regular Expressions (`re` module). This project demonstrates pattern matching, edge-case handling, and modular code design.

## 🚀 Features

- **Email Validation**: Ensures standard `user@domain.com` formatting.
- **Indian Mobile Validation**: Validates 10-digit numbers starting with 6-9, supporting optional `+91` or `0` prefixes.
- **Password Strength Check**: Enforces security rules (Length, Uppercase, Lowercase, Numbers, and Special Characters).
- **Dynamic Input**: Interactive CLI to test inputs in real-time.
- **Error Handling**: Provides specific feedback for empty strings or malformed patterns.

## 🛠️ Regex Patterns Used

| Data Type | Regex Pattern |
| :--- | :--- |
| **Email** | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$` |
| **Mobile** | `^(?:\+91|0)?[6789]\d{9}$` |
| **Password**| `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$` |
------

## Task 12: API Integration and Data Fetching
**Files:**`api_data_fetch.py`,`Task12.png`
**Date:** 03/02/26

### Key Implementations
- **HTTP Requests**: Utilized the `requests` library to perform GET operations on public REST APIs
- **JSON Parsing**: Decoded complex nested JSON structures into Python dictionaries for data extraction
- **Error Handling**: Implemented status code checks and `RequestException` traps for robust network communication
- **Data Persistence**: Automated the storage of live API responses into local text files for offline access

### Technical Skills Demonstrated
- **Status Codes**: Managed logic based on HTTP 200 (Success) and handled 4xx/5xx error states
- **Endpoint Configuration**: Worked with query parameters (Latitude/Longitude) to filter API results
- **File I/O**: Seamlessly integrated network data with local file system writing

---


## Task 13: Web Scraping Using BeautifulSoup
**Files:**`web_scraper.py`,`Task13.png`,`scraped_quotes.csv`
**Date:** 06/02/26

### Key Implementations
- **DOM Parsing**: Utilized BeautifulSoup to navigate HTML structures and target data within specific tags and classes.
- **Data Extraction**: Automated the retrieval of text, hyperlinks (href), and attributes from live web pages.
- **Defensive Scraping**: Implemented safety checks to handle missing tags safely, preventing AttributeError during runtime.
- **CSV Integration**: Converted unstructured HTML data into structured tabular formats for data analysis.

### Technical Skills Demonstrated
- **Tag Identification**: Proficiency in using .find() and .find_all() with complex CSS class selectors.
- **HTTP Communication**: Used requests to handle server-side responses and status verification.
- **Data Persistence**: Managed File I/O to write scraped datasets into local .csv files.

-----

# Task 14: Database Operations Using SQLite
**Files:**`database_app.py`,`Task14.png`,`my_application.db`
**Date:** 10/02/26

A simple Python application that demonstrates how to perform CRUD (Create, Read, Update, Delete) operations using the built-in `sqlite3` library. This project focuses on dynamic user input and secure database practices.

## Features
* **Dynamic Input:** Accepts Indian names and cities directly from the user.
* **Security:** Uses parameterized queries to prevent SQL Injection.
* **CRUD Logic:** Covers creating tables, inserting, fetching, updating, and deleting records.
* **Resource Management:** Ensures database connections are committed and closed properly.
