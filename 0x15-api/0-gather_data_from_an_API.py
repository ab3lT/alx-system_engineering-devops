#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    Employee_id = sys.argv[1]
    user = '{}users/{}'.format(url, Employee_id)
    json_obj = requests.get(user).json()

    todo = '{}todos?userId={}'.format(url, Employee_id)
    tasks = requests.get(todo).json()

    com_task = []
    for task in tasks:
        if task.get('completed') is True:
            com_task.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(json_obj.get('name'),
          len(com_task), len(tasks)))
    for com in com_task:
        print('\t', com)
