from datetime import datetime


class Task:
    def __init__(self, id, title, description, due_date, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        
        # self.due_date = due_date
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        
        self.status = status

    def is_overdue(self):
        return self.status != "Completed" and self.due_date < datetime.today().date()



    def __str__(self):         
        overdue_flag = " ⚠ OVERDUE" if self.is_overdue() else ""
        return f"""
Task Id : {self.id}
Title : {self.title}
Description : {self.description}
Due_date : {self.due_date}
Status : {self.status}
                """
        