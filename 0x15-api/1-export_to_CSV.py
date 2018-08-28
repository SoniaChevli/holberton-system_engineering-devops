#!/usr/bin/python3
'''
given REST API for given employee ID
returns information about TODO list progress
'''
if __name__ == '__main__':
    import requests
    import csv
    import sys

    employee_id = sys.argv[1]
    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))

    user_info = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                             .format(employee_id))

    all_tasks = user_data.json()
    user_name = user_info.json()[0].get('name')

    with open("{}.csv".
              format(employee_id), "w", newline='', encoding='utf-8') as cfile:

        f = csv.writer(cfile,  quoting=csv.QUOTE_ALL)

        for task in all_tasks:
            f.writerow([employee_id,
                        user_name,
                        task.get('completed'),
                        task.get('title')])
