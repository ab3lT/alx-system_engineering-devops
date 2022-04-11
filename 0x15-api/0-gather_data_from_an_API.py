#!/usr/bin/python3
"""getting data from an api
"""

import requests
import sys

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com"
    id = sys.argv[2]
    userId = sys.argv[1]
    user = requests.get(endpoint + "users/{}".
                        format(userId), verify=False).json()
    name = user.json().get('name')
    todo = requests.get(endpoint + "todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
