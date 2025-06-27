#!/usr/bin/python3

"""
Module: 0-gather_data_from_an_API

This script uses a public REST API (https://jsonplaceholder.typicode.com)
to retrieve the TODO list progress of a given employee by ID.

It prints the employee's name, the number of completed tasks out of the total,
and lists all completed task titles.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Example:
    python3 0-gather_data_from_an_API.py 2

Dependencies:
    - requests
    - sys

Author: Albert Niyonsenga
"""

import requests
import sys


def get_employee_info(employee_id):
    """
    Fetch employee information using the provided employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: JSON object with employee information (e.g., name, username).
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)

    if response.status_code != 200:
        return None
    return response.json()


def get_employee_todos(employee_id):
    """
    Fetch TODO list for a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of task dictionaries.
    """
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)

    if response.status_code != 200:
        return []
    return response.json()


def display_todo_progress(employee_name, todos):
    """
    Display the TODO list progress for an employee.

    Args:
        employee_name (str): Name of the employee.
        todos (list): List of task dictionaries.
    """
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    num_done = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    # Ensure a valid employee ID is provided via command-line argument
    try:
        employee_id = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Fetch employee info
    employee = get_employee_info(employee_id)
    if not employee:
        print("User not found.")
        sys.exit(1)

    # Fetch and display their TODO list progress
    todos = get_employee_todos(employee_id)
    display_todo_progress(employee.get("name"), todos)
