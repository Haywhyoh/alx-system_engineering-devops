#!/usr/bin/python3
"""
gathers information about from api
about an employee by ID and returns
"""
import requests
import sys


def get_info():
    """the method to get info"""
    url = 'https://jsonplaceholder.typicode.com/'
    name_url = '{}users/{}'.format(url, sys.argv[1])
    name = requests.get(name_url).json().get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    complete = 0
    titles = []
    total = 0
    for task in tasks:
        if task['userId'] == int(sys.argv[1]):
            if task['completed'] is True:
                complete += 1
                titles.append(task['title'])
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, total))
    for title in titles:
        print('\t ', end="")
        print(title)


if __name__ == "__main__":
    get_info()
