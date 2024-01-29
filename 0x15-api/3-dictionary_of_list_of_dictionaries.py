#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def get_user_todo_info(user_id):
    """Get to-do list information for a specific user."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_info = requests.get(user_url).json()
    todo_info = requests.get(f"https://jsonplaceholder.typicode.com/todos",
                             params={"userId": user_id}).json()
    return {
        user_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_info["username"]
            } for task in todo_info
        ]
    }


def export_to_json():
    """Export to JSON for all employees."""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    all_user_todo_info = {}
    for user in users:
        user_id = user["id"]
        user_todo_info = get_user_todo_info(user_id)
        all_user_todo_info.update(user_todo_info)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_user_todo_info, jsonfile)


if __name__ == "__main__":
    export_to_json()
