# AI/ML 2026

## Objective

Build strong foundations in Python, Git, GitHub, and AI/ML engineering.

## Setup

Create and activate the Python virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate

What I Learned Today
Installed and verified Git
Configured Git username and email
Created a structured AI/ML workspace
Created a Python virtual environment
Initialized a Git repository
Created a .gitignore
## Day 10 — Student Performance Analyzer

### Objective

Build a small command-line Python application that combines the Phase 1 fundamentals.

### Features

- Load student records from JSON
- Show all students
- Calculate class average
- Find highest performer
- Find lowest performer
- Calculate pass/fail statistics
- Calculate attendance statistics
- Search student by name or ID
- Handle invalid input safely
- Use functions instead of one giant script
- Use classes where they improve structure
- Include basic assert-based tests

### Project Structure

```text
phase-01-python/
│
├── src/
│   ├── main.py
│   ├── analyzer.py
│   └── models.py
│
├── data/
│   └── students.json
│
├── tests/
│   └── test_analyzer.py
│
├── README.md
├── .gitignore
└── requirements.txt