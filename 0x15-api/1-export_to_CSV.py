#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    BASE_URL = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    BASE_TODO = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"

    user = requests.get(BASE_URL)
    todo = requests.get(BASE_TODO)
    lis = []

    for i in todo.json():
        new = {'task': f"{i.get('title')}",
               'completed': i.get('completed'),
               'username': f"{user.json().get('username')}"}
        lis.append(new)

        dic = {f"{argv[1]}": lis}
        with open(f"{argv[1]}.csv", 'w') as file:
            json.dump(dic, file)
