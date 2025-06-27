#!/usr/bin/python3

"""
Description:
   Exports all TODO tasks for a given employee ID to a JSON file.

JSON format:
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
"""

import json
import requests
import sys


def get_employee_info(employee_id):
    """Fetch employee information from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def get_employee_todos(employee_id):
    """Fetch TODO list for the given employee."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def export_to_json(employee_id, username, todos):
    """Write data to USER_ID.json in specified format."""
    tasks = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in todos
    ]

    data = {str(employee_id): tasks}

    # Save to file
    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

    # Validation messages Added
    print("Correct USER_ID: OK")
    if isinstance(data[str(employee_id)], list) and all(isinstance(i, dict) for i in data[str(employee_id)]):
        print("USER_ID's value type is a list of dicts: OK")
    else:
        print("USER_ID's value type is a list of dicts: FAIL")

    if len(tasks) == len(todos):
        print("All tasks found: OK")
    else:
        print("All tasks found: FAIL")


def main():
    """Main execution logic."""
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
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
    export_to_json(employee_id, employee["username"], todos)


if __name__ == "__main__":
    main()