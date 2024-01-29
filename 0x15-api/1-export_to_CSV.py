#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
from requests import get
from sys import argv


def get_employee_info(employee_id):
    response = get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    return response.json()


def get_employee_todo_list(employee_id):
    r = get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    return r.json()


def export_to_csv(employee_id, employee_info, todo_list):
    filename = f'{employee_id}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        fieldn = ['USER_ID','USERNAME','TASK_COMPLETED_STATUS','TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldn)

        writer.writeheader()

        for task in todo_list:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_info['name'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    print(f'Data exported to {filename}')


def main():
    try:
        if len(argv) != 2:
            raise ValueError("Usage: {} <employee_id>".format(argv[0]))

        employee_id = int(argv[1])
        employee_info = get_employee_info(employee_id)
        todo_list = get_employee_todo_list(employee_id)

        completed_tasks = sum(task['completed'] for task in todo_list)
        total_tasks = len(todo_list)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_info['name'], completed_tasks, total_tasks))

        for task in todo_list:
            if task['completed']:
                print("\t{}".format(task['title']))

        export_to_csv(employee_id, employee_info, todo_list)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
