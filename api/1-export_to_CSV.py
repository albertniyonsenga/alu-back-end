#!/usr/bin/python3
"""
Module: 1-export_to_CSV

This script exports all TODO tasks for a given employee ID
from the JSONPlaceholder REST API to a CSV file.

CSV Format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Usage:
    python3 1-export_to_CSV.py <employee_id>

Author: Albert Niyonsenga
"""

import csv
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


def export_to_csv(employee_id, username, todos):
    """Export tasks to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


def main():
    """Main script logic."""
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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
    export_to_csv(employee_id, employee.get("username"), todos)


if __name__ == "__main__":
    main()
