import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json
from flask import request

# from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from flask_cors import CORS
CORS(app)
# Migrate(app,db)

class Student(db.Model):
	__tablename__ = 'student'
	student_id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	linkedIn = db.Column(db.Text)
	github = db.Column(db.Text)
	comp_id = db.Column(db.Integer)
	project_id = db.Column(db.Integer)
	 # db.ForeignKey('competency.id')

	def __init__(self, first_name, last_name, linkedIn, github, comp_id, project_id):
		self.first_name = first_name
		self.last_name = last_name
		self.linkedIn = linkedIn
		self.github = github
		self.comp_id = comp_id
		self.project_id = project_id

	def __repr__(self):
		return f"Student:{self.first_name}{self.last_name} Student ID: {self.student_id}"

class Competency(db.Model):
	__tablename__ = 'competency'
	comp_id = db.Column(db.Integer, primary_key = True)
	comp_name = db.Column(db.Text)
	comp_num = db.Column(db.Integer)
	unit_effort = db.Column(db.Integer)
	percent_complete = db.Column(db.Float)

	def __init__(self, comp_name, comp_num,unit_effort, percent_complete):	
		self.comp_name = comp_name
		self.comp_num = comp_num
		self.unit_effort = unit_effort
		self.percent_complete = percent_complete

	def __repr__(self):
		return f" This is a test ,{self.comp_name}, {self.comp_id}"

class Project(db.Model):
	__tablename__ = 'project'
	project_id = db.Column(db.Integer, primary_key = True)
	project_name = db.Column(db.Text)

	def __init__(self, project_name):
		self.project_name = project_name

	def __repr__(self):
		return f"{self.project_name}"



# @app.route("/student/")
# def build():
# 	student_list_master = []
# 	student_list = Student.query.all()
# 	print(student_list)
# 	for student in student_list:
# 		student_list_dict = {
# 		'Student_ID': student.student_id,
# 		'First_Name': student.first_name,
# 		'Last_Name' : student.last_name,
# 		'LinkedIn' : student.linkedIn,
# 		'GitHub' : student.github,
# 		'Competency' : student.comp_id,
# 		'Project': student.project_id
# 		}
# 		print(student.first_name, student.last_name)
# 		student_list_master.append(student_list_dict)
# 	return json.dumps(student_list_master)


# @app.route("/comp/")
# def comp():
# 	comp_list_master = []
# 	comp_list = Competency.query.all()
# 	print(comp_list)
# 	for comp in comp_list:
# 		comp_list_dict = {
# 		'Competency ID': comp.comp_id	,
# 		'Competency Number' : comp.comp_num,
# 		'Competency Name' : comp.comp_name,
# 		'Units Effort': comp.unit_effort,
# 		'Percent Complete': comp.percent_complete,
# 		}
# 		print(comp.comp_num, comp.comp_name)
# 		comp_list_master.append(comp_list_dict)
# 	return json.dumps(comp_list_master)



@app.route('/search/<first_name>/')
def search(first_name = None):
	print (first_name)
	# fname = request.args.get('first_name')
	student_master = []

	student_list = Student.query.filter_by(first_name = first_name)
	print(student_list)
	for student in student_list:
		student_dict = {
		'Student_ID': student.student_id,
		'First_Name': student.first_name,
		'Last_Name' : student.last_name,
		'LinkedIn' : student.linkedIn,
		'GitHub' : student.github,
		'Competency' : student.comp_id,
		'Project': student.project_id
		}
		print(student.first_name, student.last_name)
		student_master.append(student_dict)
	return json.dumps(student_master)

@app.route('/remove', methods = ['POST'])

def remove():
	body = request.get_json()
	print(body['name'])
	close_student = Student.query.filter_by(first_name = body['name']).first()
	print(close_student)
	db.session.delete(close_student)
	db.session.commit()

@app.route('/editcomp', methods = ['POST'])
def editcomp():
	body = request.get_json()
	print('comp',body['comp'])
	edit = Student.query.filter_by(first_name = body['name']).first()
	print('return',body['name'])
	print('edit', edit)
	edit.comp_id = body['comp']
	db.session.add(edit)
	db.session.commit()
	
@app.route('/comp/<comp_num>/')
def searchcomp(comp_num = None):
	comp_master = []

	comp_list = Competency.query.filter_by(comp_num = comp_num)
	print(comp_list)
	for comp in comp_list:
		comp_dict = {
		'comp_ID': comp.comp_id,
		'comp_num': comp.comp_num,
		'comp_name' : comp.comp_name,
		'unit_effort': comp.unit_effort,
		'percent_complete' :comp.percent_complete 
		}
		print(comp.comp_name, comp.comp_num)
		comp_master.append(comp_dict)
	return json.dumps(comp_master)

@app.route("/project/<project_id>")
def project(project_id = None):
	project_list_master = []
	project_list = Project.query.filter_by(project_id = project_id)
	for project in project_list:
		project_list_dict = {
		'Project_ID' : project.project_id,
		'Project_Name' : project.project_name
		}
		print (project.project_name)
		project_list_master.append(project_list_dict)
	return json.dumps(project_list_master)	

			
if __name__ == '__main__':
	app.run(debug=True)



		