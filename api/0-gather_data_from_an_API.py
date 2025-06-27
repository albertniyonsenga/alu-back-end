#!/usr/bin/python3

"""
Description:
    This script fetches and displays the TODO list progress of a given employee
    using the JSONPlaceholder REST API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Example:
    python3 0-gather_data_from_an_API.py 2

The script prints:
    - The employee’s name
    - The number of completed tasks out of the total tasks
    - The titles of completed tasks (each prefixed by a tab and space)

Author: Albert Niyonsenga
"""

import requests
import sys


def get_employee_info(employee_id):
    """
    Fetch employee information from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict or None: Employee data as a dictionary or None if not found.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def get_employee_todos(employee_id):
    """
    Fetch all TODO tasks associated with an employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of dictionaries representing tasks.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def display_todo_progress(employee_name, todos):
    """
    Display TODO task progress for the given employee.

    Args:
        employee_name (str): The full name of the employee.
        todos (list): A list of task dictionaries.
    """
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    num_done = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


def main():
    """
    Entry point for the script.
    Parses command-line input and coordinates data fetching and display.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    employee = get_employee_info(employee_id)
    if not employee:
        print("User not found.")
        sys.exit(1)

    todos = get_employee_todos(employee_id)
    display_todo_progress(employee.get("name"), todos)


if __name__ == "__main__":
    main()
