#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    # Get user ID from command line argument
    user_id = sys.argv[1]

    # Set base URL for API requests
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information and to-do list
    user_response = requests.get(base_url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    todo_response = requests.get(base_url + "todos", params={"userId": user_id})
    todo_data = todo_response.json()

    # Export data to CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, t.get("completed"), t.get("title")])
         for t in todo_data]
