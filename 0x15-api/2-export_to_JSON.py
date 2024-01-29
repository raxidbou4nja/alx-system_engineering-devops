#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
from sys import argv

def export_to_csv(user_id):
    # Define the URLs for user and todo data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    try:
        # Fetch user and todo data
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        # Prepare CSV data
        csv_data = [[user_data['id'], user_data['username'], task['completed'], task['title']] for task in todo_data]

        # Write CSV data to file
        with open(f"{user_id}.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        print(f'Data exported to {user_id}.csv')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
    else:
        export_to_csv(argv[1])
