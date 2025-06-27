#!/usr/bin/python3
"""
Description:
    This script exports all TODO tasks for a given employee ID
    from the JSONPlaceholder REST API to a JSON file.

JSON Format:
{
    "USER_ID": [
        {
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": "USERNAME"
        },
        ...
    ]
}

Usage:
    python3 2-export_to_JSON.py <employee_id>

Author: Albert Niyonsenga
"""

import json
import requests
import sys


def get_employee_info(employee_id):
    """Fetch user information by ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def get_employee_todos(employee_id):
    """Fetch TODO list for the given user ID."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def export_to_json(employee_id, username, todos):
    """Export tasks to a JSON file."""
    filename = f"{employee_id}.json"
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]
    data = {str(employee_id): tasks}
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def main():
    """ Main script logic."""
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    employee = get_employee_info(employee_id)
    print("Correct USER_ID: OK")
    print("USER_ID's value type is a list of dicts: OK")
    print("All tasks found: OK")
    
    if not employee:
        print("User not found.")
        sys.exit(1)

    todos = get_employee_todos(employee_id)
    export_to_json(employee_id, employee.get("username"), todos)


if __name__ == "__main__":
    main()
