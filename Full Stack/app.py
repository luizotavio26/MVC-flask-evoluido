import os
from flask import Flask
from config import Config 

from controllers.user_controller import UserController
from controllers.task_controller import TaskController

from models.user import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

db.init_app(app)


with app.app_context():
    db.create_all()

app.add_url_rule('/', 'index', UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['GET', 'POST'])

app.add_url_rule('/tasks', 'list_tasks', TaskController.list_tasks)
app.add_url_rule('/tasks/new', 'create_task', TaskController.create_task, methods=['GET', 'POST'])
app.add_url_rule('/tasks/update/<int:task_id>', 'update_task_status', TaskController.update_task_status, methods=['GET', 'POST'])
app.add_url_rule('/tasks/delete/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True, port=5002)