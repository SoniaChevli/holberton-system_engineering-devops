#!/usr/bin/python3
'''
given REST API for given employee ID
returns information about TODO list progress
'''
if __name__ == '__main__':
    import requests
    import sys

    employee_id = sys.argv[1]
    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id))

    user_info = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                             .format(employee_id))

    all_tasks = user_data.json()
    user_name = user_info.json()[0].get('name')

    total_tasks = len(all_tasks)
    completed_tasks = 0
    completed_titles = []

    for task in all_tasks:
        if task.get('completed', None):
            completed_tasks += 1
            completed_titles.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, completed_tasks, total_tasks))

    for title in completed_titles:
        print("\t {}".format(title))
