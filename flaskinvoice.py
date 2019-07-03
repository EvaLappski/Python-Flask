import invoice
import json
from flask import Flask
app = Flask(__name__)
from flask import request, render_template
from flask_cors import CORS
CORS(app)

@app.route("/info/")
def info():
	return json.dumps(invoice.customer_list)



@app.route("/template/")
def template():
	with open("invoice.txt", "r") as f:
  	  content = f.read()
	return render_template("info.html", content=content)



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)