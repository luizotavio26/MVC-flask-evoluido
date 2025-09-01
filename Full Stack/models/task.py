from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.user import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(100), nullable=False, default="Pendente")
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="tasks")  

    def __init__(self, title, description, user_id, status="Pendente"):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.status = status
