import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

# 

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	customer_name = db.Column(db.Text)
	contact = db.Column(db.Text)
	phone = db.Column(db.Text)

	def __init__(self, customer_name, contact, phone):
		self.customer_name = customer_name
		self.contact = contact
		self.phone = phone

	def __repr__(self):
		return f"Customer: {self.customer_name} Contact:{self.contact} Phone:{self.phone}"

@app.route("")
def project():
	return 


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
		