from task import Task
from storage import Storage
from datetime import datetime
from logger import logger

def add_task(tasks):
    task_id = len(tasks) + 1
    title = input("Enter the task title :- ")
    description = input("Enter the task Descriprion :- ")

    # due_date = input("Enter the Due Date (yyyy-mm-dd) :- ")
    while True:
        due_date = input("Enter the Due Date (yyyy-mm-dd) :- ")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")    

    task = Task(task_id, title, description, due_date)
    tasks.append(task)
    Storage.save_tasks(tasks)
    print("\nTask Added Successfully!")
    logger.info(f"Task added: {title}")

def view_overdue_tasks(tasks):
    overdue_tasks = [task for task in tasks if task.is_overdue()]

    if not overdue_tasks:
        print("No Overdue Task")
        return
    
    print("\nOverdue Tasks:")
    for task in overdue_tasks:
        print(task)
        

def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.")
        return
    
    print("\n Tasks List. ")
    for task in tasks:
        print(task)

def delete_task(tasks):
    if not tasks:
        print("\nNo task to delete.")
        return
    
    try:
        task_id = int(input("Enter The task Id to Delete. :- "))
    except ValueError:
        print("\nask ID must be a number.")
        return

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            Storage.save_tasks(tasks)
            print("\nTask Deleted Successfully!.")
            return
        
    print("Task Not Found")

def mark_task_complete(tasks):
    if not tasks:
        print("\nNo Task Available.")
        return
    
    try:
        task_id = int(input("Enter Task ID to mark complete. :- "))
    except ValueError:
        print("\nask ID must be a number.")

    for task in tasks:
        if task.id == task_id:
            task.status = "Completed"
            Storage.save_tasks(tasks)
            print("\nTask marked as Completed")
            return
        
    print("Task Not Found.")


def search_filter(tasks):
    keyword = input("Enter Keywords to search: ").lower()

    resusts = [task for task in tasks if keyword in task.title.lower()]

    if not resusts:
        print("Nor Match Found")
        return
    
    for task in resusts:
        print(task)


def filter_task_by_status(tasks):
    status = input("Enter Status (Pending/Completed): ").lower()

    filtered = [task for task in tasks if task.status == status]

    for task in filtered:
        print(task)
        