#!/usr/bin/python3
'''
given REST API for all employees
returns information about TODO list progress
'''
if __name__ == '__main__':
    import requests
    import json

    all_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos")

    all_users = requests.get("https://jsonplaceholder.typicode.com/users")

    todos = all_todos.json()
    users = all_users.json()

    todo_dict = {}

    for user in users:
        todo_list = []
        user_name = user.get('name')
        user_id = user.get('id')
        for todo in todos:
            if todo.get('userId') == user_id:
                tmp_dict = {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user_name}
                todo_list.append(tmp_dict)
                todo_dict[user_id] = todo_list

    final = json.dumps(todo_dict)

    with open("todo_all_employees.json",
              "w", newline='', encoding='utf-8') as jfile:
        jfile.write(final)
