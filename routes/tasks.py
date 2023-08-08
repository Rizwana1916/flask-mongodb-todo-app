from flask import Blueprint, redirect, url_for, request
from bson.objectid import ObjectId
from app import app, mongo
from models.task import create_task, get_all_tasks, toggle_task, delete_task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    create_task(mongo.db, title)
    return redirect(url_for('index'))

@tasks_bp.route('/toggle/<task_id>')
def toggle(task_id):
    toggle_task(mongo.db, task_id)
    return redirect(url_for('index'))

@tasks_bp.route('/delete/<task_id>')
def delete(task_id):
    delete_task(mongo.db, task_id)
    return redirect(url_for('index'))

app.register_blueprint(tasks_bp, url_prefix='/tasks')
