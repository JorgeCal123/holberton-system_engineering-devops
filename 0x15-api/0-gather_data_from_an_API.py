#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv
import  json

url = 'https://jsonplaceholder.typicode.com/todos/'
with urlopen(url + argv[1]) as response:
    body = response.read()
todo_item = body.json()
print (todo_item)
