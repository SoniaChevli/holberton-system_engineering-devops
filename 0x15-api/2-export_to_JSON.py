#!/usr/bin/python3
'''
given REST API for given employee ID
returns information about TODO list progress
'''
if __name__ == '__main__':
    import sys
    import requests
    import json

    employee_id = sys.argv[1]
    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))

    user_info = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                             .format(employee_id))

    all_tasks = user_data.json()
    user_name = user_info.json()[0].get('name')

    task_array = []

    for task in all_tasks:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": user_name}
        task_array.append(task_dict)

    final = json.dumps({employee_id: task_array})

    with open("{}.json".
              format(employee_id), "w", newline='', encoding='utf-8') as jfile:
        jfile.write(final)
