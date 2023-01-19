#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    USER_ID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(USER_ID))
    USERNAME = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = USER_ID + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=' ', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('USER_ID') == int(USER_ID):
                writer.writerow([USER_ID, USERNAME, str(task.get('completed')),
                                 task.get('title')])
