from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_db'

mongo = PyMongo(app)

@app.route('/')
def index():
    tasks = mongo.db.tasks.find()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    mongo.db.tasks.insert_one({'title': title, 'completed': False})
    return redirect(url_for('index'))

@app.route('/toggle/<task_id>')
def toggle_task(task_id):
    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    mongo.db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'completed': not task['completed']}})
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
