#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""
import requests
from sys import argv
if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    user_dict = user.json()

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_dict = todos.json()
    done_task = 0
    all_task = 0
    tasks = ""
    for t in todos_dict:
        if t['userId'] == int(argv[1]):
            all_task += 1
            if t['completed']:
                done_task += 1
                tasks += "\t {}\n".format(t['title'])

    msm = "Employee {} is done with tasks({}/{}):\n{}".format(
            user_dict['name'], done_task, all_task, tasks)
    print(msm, end="")
