import os
from flask import Flask
from config import Config # importa as 

from controllers.user_controller import UserController
from controllers.task_controller import TaskController
#IMPORTAR CONTROLLER TASKS AQUI
#from controllers.

from models.user import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

# inicializa o banco de dados
db.init_app(app)

# cria tabelas

with app.app_context():
    db.create_all()

# forma alternativa de criar rotas, parâmetros: rota em si, endpoint interno do flask e função a ser executada quando a URL for acessada
app.add_url_rule('/', 'index',  UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['GET', 'POST'])

#app.add_url_rule('/', 'tasks', TaskController.list_tasks)
app.add_url_rule('/tasks', 'tasks', TaskController.list_tasks)

app.add_url_rule('/create_tasks', 'create_tasks', TaskController.create_task, methods=['GET', 'POST'])
#ROTAS DA TASM



if __name__ == '__main__':
    app.run(debug=True, port=5002)