#This is a Command Line To-Do List Application built to manage tasks

"""
Import modules 
1. json: To save and load tasks in Json 
2. os: To check if the file already exists when you load it
3. datetime: to handle due dates
"""

import json
import os
from datetime import datetime, timedelta

#File to store the tasks
tasksFile = "tasks_file.json"

#Function to check if the task already exists before storing
def load():
    if os.path.exists(tasksFile):
        with open(tasksFile, 'r') as file:
            tasks_present = json.load(file)
        return tasks_present
    else:
        return {"tasks_present": []}
    
#Function to save a new task
def save(tasks_present):
    with open(tasksFile, 'w') as file:
        json.dump(tasks_present, file, indent=2)

#Fuction to add a new task
def add(tasks_present, task, priority, due_date):
    task_id = len(tasks_present["tasks_present"]) + 1
    new_task = {
        "id": task_id,
        "task" : task,
        "priority" : priority,
        "due_date": due_date.strftime('%d-%m-%Y') if due_date else None,
        "completed" : False,
    }
    tasks_present["tasks_present"].append(new_task)
    print(f"Task '{task}' added successfully!")

#Function to remove a task from the list
def remove(tasks_present, task_id):
    for task in tasks_present["tasks_present"]:
        if task["id"] == task_id:
            tasks_present["tasks_present"].remove(task)
            print(f"Task '{task['task']}' removed successfully!")
            return
    print("Task not found in the to-do list!")

#Function to monitor completion
def mark_completed(tasks_present, task_id):
    for task in tasks_present["tasks_present"]:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task {task['task']} marked as completed!")
            return
    print("Task not found in the to-do list!")

#Function to display all the tasks in the to-do list
def display(tasks_present):
    if not tasks_present["tasks_present"]:
        print("No tasks found on the list!")
    else:
        for task in tasks_present["tasks_present"]:
            print(f"ID: {task['id']},  Task: {task['task']},  Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}") 

#Main function
def main():
    tasks_present = load()

    while True:
        print("\n \n ==== To-Do List====")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Display all tasks")
        print("5. Exit")

        choice = input("\n \n How would you like to proceed? \n Enter a number from (1-5): ")
        
        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date_str = input("Enter due date for completion (DD-MM-YYYY): ")
            due_date = datetime.strptime(due_date_str, '%d-%m-%Y') if due_date_str else None
            add(tasks_present, task, priority, due_date)
        
        elif choice == '2':
            task_id = int(input("Enter ID of the task to be removed: "))
            remove(tasks_present, task_id)
        
        elif choice == '3':
            task_id = int(input("Enter ID of the task that has been completed: "))
            mark_completed(tasks_present, task_id) 
        
        elif choice == '4':
            display(tasks_present)
        
        elif choice == '5':
            save(tasks_present)
            print("Exiting the application, See you soon!")
            break
        
        else:
            print("Invalid choice. Enter a number between 1-5!") 

if __name__ == "__main__":
    main()              
