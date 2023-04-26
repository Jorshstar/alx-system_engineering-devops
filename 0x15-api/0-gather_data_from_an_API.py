#!/usr/bin/python3

import requests
import sys


if len(sys.argv) < 2:
    print("Usage: {} employee_id".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]
base_url = 'https://jsonplaceholder.typicode.com/'

# Script to Fetch  user information
user_response = requests.get(base_url + 'users/{}'.format(employee_id))
user_data = user_response.json()
employee_name = user_data['name']

# Script to Fetch  user's todo list
todo_response = requests.get(base_url + 'todos?userId={}'.format(employee_id))
todo_data = todo_response.json()

# Count the number of completed tasks and the total number of tasks
num_completed_tasks = 0
num_total_tasks = len(todo_data)
completed_tasks = []

for task in todo_data:
    if task['completed']:
        num_completed_tasks += 1
        completed_tasks.append(task['title'])

# Script to Print the output in the specified format
print("Employee {} is done with tasks({}/{}):"
        .format(employee_name, num_completed_tasks, num_total_tasks))
for task in completed_tasks:
    print("\t {}".format(task))
