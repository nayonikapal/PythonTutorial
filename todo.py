# Create a todo app in python

# CRUD

# Create
# Read
# Update
# Delete


# # Menu:
# 1. Add Task
# 2. View Tasks
# 3. Update Task(s)
# 4. Delete
# 5. Exit


# {
#     "Task 1": {
#         "id": 1,
#         "task": {
#             "name": "Task Name" | str,
#             "description": "task description",
#             "created_at": "time 20/3/2024",
#             "updated_at": "time 20/3/2024",
#         },
#     }
# }
import datetime
task_lst =[]


def add_task():
    tsk_name = input('Enter Task name : ')
    
    task_lst.append(tsk_name)
    id = task_lst.index(tsk_name)
    

def remove_task():
    pass

def view_task():
    pass

def update_task():
    pass

def start():
    print('''
            Menu:
             1. Add Task
             2. View Tasks
             3. Update Task(s)
             4. Delete
             5. Exit
          ''')
    num = int(input( "Choose the no. from 1 -5 : " ))
    if num== 1:
        add_task()
    elif  num== 2:
        view_task()
    elif  num== 3:
        update_task()
    elif  num== 4:
        remove_task()
    elif  num== 5:
        exit()
    else: 
        print("Oopsss ... !!!!, Choose from 1-5 : ")
        start()
    

if __name__ == '__main__':
    start()