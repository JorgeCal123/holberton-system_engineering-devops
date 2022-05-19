#!/usr/bin/python3
"""using this REST API,
for a given employee ID,
return list progress"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    user_json = user.json()
    task = ""
    dicci = {}
    lista = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            dictio = {}
            dictio["task"] = t["title"]
            dictio["completed"] = t["completed"]
            dictio["username"] = user_json["username"]
            lista.append(dictio)
            dicci[t["userId"]] = lista
    filename = argv[1] + ".json"
    with open(filename, "w") as outfile:
        json.dump(dicci, outfile)
