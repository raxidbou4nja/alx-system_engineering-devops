#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1]))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    with open(sys.argv[1] + '.csv', mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(sys.argv[1]):
                writer.writerow([sys.argv[1], name, str(task.get('completed')),
                                 task.get('title')])
