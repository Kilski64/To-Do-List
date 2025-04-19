# Simple To-Do List

## Overview
This project is a command-line to-do list application written in Python, designed to help users manage tasks with subjects and descriptions. It uses a list of dictionaries (`entries`) to store tasks, allowing users to add tasks with a subject and description, delete tasks by index, view the current task list, or exit the program with a confirmation prompt (`Y/N`).

## Features
- **Add Tasks**: Users can add a task by typing `Add` (or `add`), providing a subject and description, which are stored as a dictionary (e.g., `{'Subject': 'Meeting', 'Description': 'Prepare slides'}`).
- **Delete Tasks**: Users can remove tasks by typing `Delete` (or `delete`), viewing the list with numbered indices, and entering the number of the task to delete.
- **View Tasks**: Users can display the current task list with indices by typing `Show List` (or `show list`), showing each task’s subject and description.
- **Exit with Confirmation**: Users can exit by typing `Exit` (or `exit`), with a confirmation prompt (`Y/N`) to confirm or return to the main menu.

## Setup
1. **Prerequisites**:
   - Python 3.6 or later
2. **Clone the Repository**:
## Usage
1. **Run the Program**:
- Execute the script in your terminal or command prompt:
  ```
  python todo_list.py
  ```
2. **Interact with the To-Do List**:
- The program prompts: `Please type 'Add' to add a task; 'Delete' to remove a task; 'Show List' to view current list; 'Exit' to exit program:`
- **Add a Task**: Type `Add` (or `add`), then enter a subject (e.g., `Meeting`) and description (e.g., `Prepare slides`). The task is added to the list.
- **Delete a Task**: Type `Delete` (or `delete`), view the numbered list, and enter the number of the task to delete (e.g., `1` to delete the first task).
- **Show the List**: Type `Show List` (or `show list`) to view all tasks with their subjects and descriptions.
- **Exit**: Type `Exit` (or `exit`), then confirm by typing `Y` (or `y`) to quit, or `N` (or `n`) to return to the main menu.
3. **View Screenshots**:
- Screenshots of the program in action (e.g., adding a task, showing the list) are in the `screenshots/` folder.

## File Structure
- `todo_list.py`: Python script containing the to-do list application.
- `README.md`: This file.

## Limitations
- **Command-Line Only**: The application runs in the terminal with no graphical user interface (GUI).
- **Non-Persistent Storage**: Tasks are stored in memory and lost when the program exits (no file or database storage).
- **Case Sensitivity**: Commands are case-insensitive (e.g., `Add` or `add`), but users must follow prompts carefully to avoid errors (e.g., invalid numbers for deletion).
