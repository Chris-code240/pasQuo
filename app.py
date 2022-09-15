
import os
from flask import Flask,request,abort,json,jsonify,render_template,url_for


app = Flask(__name__)

current_years = ["2021","2020","2019","2018","2017"]
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,'static','questions')

@app.route('/')
def home():
    return render_template('pages/home.html',nav=True,title='Home',help=False,FAQ=True,start_btn=True,year_selection=False)

@app.route('/user-select')
def user_select():
    return render_template('pages/library.html',nav=True,title='Library || User select',help=False,FAQ=True,start_btn=False,year_selection=False)

@app.route('/select-question')
def user_select_question():
    return render_template('pages/select-paper.html',nav=True,title="Select question",HELP=True,start_btn=False,year_selection=True,year="2019",years=current_years)

@app.route('/questions')
def get_questions():
    return render_template('pages/get_questions.html',nav=True,title="Questions",FAQ=True,year_selection=True,year="2019",years=current_years,data={'course_title':'Advanced Database',"questions":[]})


@app.route('/questions/selected/<string:doc_name>')
def get_selected(doc_name):
    document_name = doc_name.split('.')[0]
    return render_template('pages/selected.html',nav=False,document='questions/{}'.format(document_name) + '.pdf',title=document_name)


@app.route('/upload')
def new_question():
    return render_template('pages/upload.html',title='Upload',HELP=True,start_btn=True)

@app.route('/questions',methods=['POST'])

def post_question():
    # file = request.files['question-paper']
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'logo.png')
    # file.save(full_filename)
    print(request.content_type)
    # print(request.get_data())
    print(request.files)
    return jsonify({})




