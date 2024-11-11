# Modern Todo List Application

A clean and modern Todo List application built with PySide6, featuring task management with categories.

![Todo List App Screenshot](screenshot.png)

## Features

- 📝 Create, edit, and delete tasks
- 📋 Categorize tasks (Work, Personal, Shopping, Other)
- 🔍 Filter tasks by category
- 🎨 Modern and clean user interface

## Requirements

- Python 3.x
- PySide6

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app

2. Create a virtual environment:
   bash
   On macOS/Linux
   python3 -m venv env
   source env/bin/activate

3. Install required packages:
   bash
   pip install PySide6

## Running the Application

1. Make sure your virtual environment is activated
2. Run the application:

bash
python todo.py

## How to Use

### Adding Tasks

1. Enter your task in the input field
2. Select a category (Work, Personal, Shopping, Other)
3. Click "Add Task"

### Managing Tasks

- **Edit**: Select a task and click "Edit"
- **Delete**: Select a task and click "Delete"
- **Clear All**: Remove all tasks with "Clear All"

### Filtering Tasks

Use the dropdown menus at the top to filter tasks by:

- Category (All Categories, Work, Personal, Shopping, Other)

## Project Structure

todo-app/
├── todo.py # Main application file
├── README.md # Documentation
└── env/ # Virtual environment directory
