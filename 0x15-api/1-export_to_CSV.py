#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    user_dict = user.json()

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_dict = todos.json()

    dict_arr = []
    labels = ['userId', 'username', 'completed', 'title']

    for t in todos_dict:
        if t['userId'] == int(argv[1]):
            dict_format = {}
            dict_format['userId'] = t['userId']
            dict_format['username'] = user_dict['username']
            dict_format['completed'] = t['completed']
            dict_format['title'] = t['title']
            dict_arr.append(dict_format)

    try:
        name_file = argv[1] + ".csv"
        with open(name_file, 'w') as f:
            writer = csv.DictWriter(f, quoting=csv.QUOTE_ALL,
                                    fieldnames=labels)
            writer.writeheader()
            for elem in dict_arr:
                writer.writerow(elem)
    except IOError:
        print("I/O error")
