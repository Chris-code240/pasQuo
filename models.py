from flask import Flask,json,jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def setuDb(app):
    db.app = app
    db.init_app(app)

def delete_all_create_all():
    db.drop_all()
    db.create_all()

  


class Question(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True)
    course_name = db.Column(db.String(),nullable=False)
    year = db.Column(db.String(),nullable=False)
    program = db.Column(db.String(),nullable=False)
    file_name = db.Column(db.String(),nullable=False)
    file = db.Column(db.LargeBinary,nullable=False)
    level = db.Column(db.String(),nullable=False)
    semester = db.Column(db.String(),nullable=False)

    def __init__(self,course_name,year,program,file,file_name,level,semester):
        self.course_name = course_name
        self.year = year
        self.program = program
        self.file = file
        self.file_name = file_name
        self.level = level
        self.semester = semester

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def question_format(self):
        return {"course":self.course_name,"year":self.year,"program":self.program,"level":self.level,"semester":self.semester}
        
