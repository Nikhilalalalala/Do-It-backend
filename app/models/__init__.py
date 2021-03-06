from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    userid = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    date_goal = db.Column(db.Date, nullable=True)
    isDone = db.Column(db.Boolean, nullable=False)

    #TODO ENSURE end_date > date_created

    def __init__(self, name: str, description: str, userid: str, date_goal: datetime = None, isDone: bool = False):
        self.id = uuid.uuid4()
        self.name = name
        self.description= description
        self.date_created = datetime.now()
        self.userid = userid
        self.date_goal = date_goal
        self.isDone = isDone
        
    def __repr__(self) -> str:
        return f'<Task: {self.__dict__} \n>'

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    hashed_password = db.Column(db.String(80), nullable=False)
    date_joined = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String(200), nullable=False)

    def __init__(self, username: str, email: str, hashed_password: str, bio: str = ''):
        self.id = uuid.uuid4()
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.date_joined = datetime.now()
        self.bio = bio

    def getId(self):
        return self.id

    def __repr__(self) -> str:
        return f'<ID: {self.id}\nNAME: {self.username}\n'
