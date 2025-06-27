#!/usr/bin/python3
"""
Description:
   Exports all employees' TODO list data into a single JSON file.
   Format:
{
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    # etc
  ],
  # etc
}
"""

import json
import requests


def fetch_all_users():
    """Fetch all users from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_todos():
    """Fetch all TODO tasks from the API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    """Main function to fetch data and write JSON."""
    users = fetch_all_users()
    todos = fetch_todos()

    all_data = {}

    # Map userId to username
    user_map = {user["id"]: user["username"] for user in users}

    for task in todos:
        user_id = task["userId"]
        task_data = {
            "username": user_map[user_id],
            "task": task["title"],
            "completed": task["completed"]
        }
        all_data.setdefault(str(user_id), []).append(task_data)

    # Write to file
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f)


if __name__ == "__main__":
    main()
