from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False, default="Pendente")
    
    user_id =  db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("users", back_populates="tasks")


    def __init__(self, id, status, tittle, description, user_id):
        self.id = id
        self.status = status
        self.tittle = tittle
        self.description = description
        self.user_id = user_id

    