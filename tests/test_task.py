# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from task import Task
from smart_task_manager.task import Task
from datetime import date, timedelta

def test_task_overdue():
    past_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d") 
    task = Task(1, "Test", "Testing", past_date)

    assert task.is_overdue() is True

