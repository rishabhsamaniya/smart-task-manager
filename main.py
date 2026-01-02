from task import Task
from user import User
from storage import Storage
from utils import (
     add_task,
     view_tasks,
     delete_task,
     mark_task_complete,
     view_overdue_tasks)


####### User ##############

user1 = User(1, "neo", "neo@example.com")

print(user1)

#Try setters
user1.set_username("nr")
user1.set_email("wrongemail")

user1.set_username("neoRish")
user1.set_email("neorish@gamil.com")

# print(user1)

##### Task ######

tasks = [
            Task(1, "Learn Python", "OOP + File Handling", "2025-12-25"),
            Task(2, "Build Project", "Smart Task Manager", "2025-12-27"), 
            Task(3, "Learn Python", "OOP + File Handling", "2025-12-28")
        ]   

# Save Tasks
Storage.save_tasks(tasks)

# Load tasks
loaded_task = Storage.load_tasks()
print("Loaded Tasks :")

for task in loaded_task:
    print(task)



# task1 = Task(
#     id = 1,
#     title = "Learn Python OPP",
#     description = "Understand classes and objects",
#     due_date="2025-01-01"
# )

# print(task1)

def main():
    task = Storage.load_tasks()

    while True:
        print("""
========= Smart Task Manager =========
1. Add Task
2. View Tasks
3. Delete Task
4. Mark As Completeed
5. Overdue Tasks              
6. Exit
""")
        try:
            choise = input("Please Enter Your Choise :- ")
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue


        if choise == "1":
            add_task(tasks)
        elif choise == "2":
            view_tasks(tasks)
        elif choise == "3":
            delete_task(tasks)
        elif choise == "4":
            mark_task_complete(tasks)
        elif choise == "5":
            view_overdue_tasks(tasks)
        elif choise == "6":
            print("👋 Exiting... Bye!")
            break
        else:
            print("Invalid Choise - Try Again !")

if __name__ == "__main__":
    main()
