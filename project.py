import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
# from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Migrate(app,db)

class Customer(db.Model):
	__tablename__ = 'customer'
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

class Invoice(db.Model):
	__tablename__ = 'invoice'
	id = db.Column(db.Integer, primary_key = True)
	customer_id = db.Column(db.Integer)
	# , db.ForeignKey ('customer.id')
	date = db.Column(db.Date)

	def __init__(self, customer_id, date):
		self.customer_id = customer_id
		self.date = date

	def __repr__(self):
		return f" This is a test ,{self.customer_id}, {self.date}"

@app.route("/info/")
def build():
	customer_list_master = []
	customer_list = Customer.query.all()
	print(customer_list)
	for customer in customer_list:
		customer_list_dict = {
		'Name': customer.customer_name,
		'Contact' : customer.contact,
		'Phone' : customer.phone,
		}
		print(customer.customer_name)
		customer_list_master.append(customer_list_dict)
	return json.dumps(customer_list_master)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)



		