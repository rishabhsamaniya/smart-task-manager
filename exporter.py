import csv

def export_tasks_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Description", "Due Date", "Status"])

        for task in tasks:
            writer.writerows([
                task.id,
                task.title,
                task.description,
                task.due_date,
                task.status
            ])
    print(f"Tasks exported to {filename}")
