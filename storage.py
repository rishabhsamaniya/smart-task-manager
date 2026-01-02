import json
from task import Task

class Storage:

    @staticmethod
    def save_tasks(tasks, filename="tasts.json"):
        """
        Save list of Task object to a JSON file

        """
        task_list = []

        for task in tasks:
            task_list.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date.strftime("%Y-%m-%d"),
                "status": task.status
            })
        
        with open(filename, "w") as file:
            json.dump(task_list, file, indent=4)

    @staticmethod
    def load_tasks(filename="tasks.json"):
        """
        Load tasks from JSON file and return list of Task objects
        """
        try:
            with open(filename, "r") as file:
                task_list = json.load(file)

                tasks = []
                for t in task_list:
                    tasks.append(
                        Task(
                            t["id"],
                            t["title"],
                            t["description"],
                            t["due_date"],
                            t["status"]
                        )
                    )
                return tasks
        except FileNotFoundError:
            return []