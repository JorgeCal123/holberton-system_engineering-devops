#!/usr/bin/python3
import requests
from sys import argv


user = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1])
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
            tasks += '\t' + t['title'] + '\n'

msm = "Employee {} is done with tasks({}/{}):\n{}".format(
        user_dict['name'], done_task, all_task, tasks)
print(msm, end="")
