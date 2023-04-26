#!/usr/bin/python3

import requests
import sys
import csv

if len(sys.argv) < 2:
    print("Usage: {} employee_id".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]
base_url = 'https://jsonplaceholder.typicode.com/'

# Fetch the user information
user_response = requests.get(base_url + 'users/{}'.format(employee_id))
user_data = user_response.json()
employee_name = user_data['username']

# Fetch the user's todo list
todo_response = requests.get(base_url + 'todos?userId={}'.format(employee_id))
todo_data = todo_response.json()

# Prepare the data for export
data = []
for task in todo_data:
    task_title = task['title']
    task_completed = task['completed']
    data.append([employee_id, employee_name, task_completed, task_title])

# Export the data in CSV format
filename = '{}.csv'.format(employee_id)
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
    for row in data:
        writer.writerow(row)
