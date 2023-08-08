from flask import Blueprint

# Create a blueprint for tasks routes
tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

# Import routes defined in tasks.py to make them accessible
from . import tasks
