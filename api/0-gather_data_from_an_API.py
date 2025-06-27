#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # URLs to access user and todos
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_done = len(done_tasks)

    # Print summary
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
