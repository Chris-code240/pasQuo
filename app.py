from io import BytesIO
import os
from flask import Flask,request,abort,json,jsonify,render_template,url_for,flash,send_file,Response
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm

import wtforms
from models import *



app = Flask(__name__)
app.config.from_object('config')

current_years = ["2022","2021","2020","2019","2018","2017"]
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(APP_ROOT,'static','questions')

UPLOAD_FOLDER = 'static/questions'
SECRETE_KEY = 'somekey'

app.config['SECRETE_KEY'] = SECRETE_KEY
app.secret_key = SECRETE_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

setuDb(app)
# Run Once
# delete_all_create_all()

@app.route('/')
def home():
    return render_template('pages/home.html',nav=True,title='Home',help=False,FAQ=True,start_btn=True,year_selection=False)

@app.route('/user-select')
def user_select():
    return render_template('pages/library.html',nav=True,title='Library',help=False,FAQ=True,start_btn=False,year_selection=False)

@app.route('/select-question')
def user_select_question():
    return render_template('pages/select-paper.html',nav=True,title="Select question",HELP=True,start_btn=False,year_selection=True,year="2022",years=current_years)

@app.route('/upload')
def new_question():
    return render_template('pages/upload.html',title='Upload',HELP=True,start_btn=True)




@app.route('/questions')
@app.route('/question')
def get_questions():
    try:
        req = request.args
        program = req['program']
        level = req['level']
        course = req['course']
        year = req['year']
        questions = [
                {"id":ques.id,"file":send_file(BytesIO(ques.file),download_name=ques.file_name,as_attachment=False),"semester":ques.semester,"file_name":ques.file_name} for ques in Question.query.filter(Question.year == year,Question.program == program, Question.course_name == course, Question.level == level).all()
                ]
        return render_template('pages/get_questions.html',nav=True,title="Questions",FAQ=True,year_selection=True,year=year,years=current_years,data={'course_title':course,"questions":questions,"total":len(questions)})
        # return questions[0]['file']
    except:
        abort(422)

        
"""Add new question to the database"""  
@app.route('/questions',methods=['POST'])
@app.route('/question',methods=['POST'])
def post_question():
    try:
        file = request.files['file'].read()
        form = request.form
        year = form['year']
        program = form['program']
        course = form['course']
        file_name = request.files['file'].filename
        level = form['level']
        semester = form['semester']

        question = Question(course,year,program,file,file_name,level,semester)
        question.insert()
        res = {"success":True,"message":"Question uploaded successfully"}
        # return render_template('pages/upload.html',title='Upload',HELP=True,start_btn=True)
        return jsonify(res)
    except:
        return jsonify({"success":False})
        # abort(422)

"""Serve document to a view"""
@app.route('/show-question/<int:ques_id>')
def show(ques_id):
    question = Question.query.filter(Question.id == ques_id).one_or_none()
    print(question.course_name)
    if question != None:
        return send_file(BytesIO(question.file),download_name=question.file_name,as_attachment=False)
    abort(404)

"""View selected document"""
@app.route('/selected/<int:ques_id>')
def get_selected(ques_id):
    question = Question.query.filter(Question.id == ques_id).one_or_none()
    if question != None:
        return render_template('pages/selected.html',course_title=question.course_name,id=question.id,title=question.course_name)
    abort(404)


@app.route('/test-post',methods=['POST'])
def test():
    print(request.form['year'])
    print(not request.files['file'])
    return jsonify({"success":True})


