# CLI Expense Tracker

A simple command-line app for tracking expenses, built with Python.
Data is stored locally in a JSON file.

## Features

- Add expenses with an amount and category
- List all expenses
- See totals per category

## Requirements

- Python 3.8 or newer (no extra packages needed)

## Usage

```
python expense.py add 250.50 --category food
python expense.py add 80 --category transport
python expense.py list
python expense.py summary
```

Example output of `summary`:

```
food 250.5
transport 80.0
```

## How it works

- `load()` and `save()` read and write `expenses.json`
- `argparse` reads the command you type and runs the matching function

## Status

Finished as a learning project. Ideas for extending it: CSV export,
price filters, and scraping individual book pages.