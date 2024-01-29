#!/usr/bin/python3

"""
Python script that exports data in the CSV format.
"""

import csv
from requests import get
from sys import argv


def get_user_info(user_id):
    response = get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    return response.json()


def get_todo_list(user_id):
    r = get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    return r.json()


def export_to_csv(user_id, user_info, todo_list):
    filename = f'{user_id}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        f = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=f)

        writer.writeheader()

        for task in todo_list:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user_info['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


def main():
    try:
        if len(argv) != 2:
            raise ValueError("Usage: {} <user_id>".format(argv[0]))

        user_id = int(argv[1])
        user_info = get_user_info(user_id)
        todo_list = get_todo_list(user_id)

        export_to_csv(user_id, user_info, todo_list)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
