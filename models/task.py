from datetime import datetime
from bson.objectid import ObjectId

class Task:
    def __init__(self, title, completed=False, created_at=None):
        self.title = title
        self.completed = completed
        self.created_at = created_at or datetime.now()

def create_task(db, title):
    task = Task(title)
    db.tasks.insert_one(task.__dict__)

def get_all_tasks(db):
    tasks = db.tasks.find()
    return [Task(**task) for task in tasks]

def toggle_task(db, task_id):
    task = db.tasks.find_one({'_id': ObjectId(task_id)})
    new_completed = not task['completed']
    db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'completed': new_completed}})

def delete_task(db, task_id):
    db.tasks.delete_one({'_id': ObjectId(task_id)})
