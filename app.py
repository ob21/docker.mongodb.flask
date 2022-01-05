import os
from flask import Flask, redirect, url_for, request, render_template, abort
from pymongo import MongoClient

app = Flask(__name__)

def printlog(m):
  #Flush to print in docker container logs
  print("[app.py] " + str(m), flush=True)

# Addr of the mongo db is the name of the container eg 'mongodb' (from docker compose)
client = MongoClient("mongodb", 27017, username='root', password='example')
db = client.tododb

@app.before_request
def limit_remote_addr():
	#printlog("nginx addr : " + "nginx")
	printlog("request = " + str(request))
	printlog("Remote addr : " + request.remote_addr)
	if request.remote_addr != '172.22.0.3':
		printlog("Abort 403 because remote addr is not 172.22.0.3")
		#abort(403)  # Forbidden

@app.errorhandler(403)
def payme(e):
    return '403 Forbidden from flask app'

@app.route('/')
def todo():

	_items = db.tododb.find()
	items = [item for item in _items]

	return render_template('todo.html', items=items)

@app.route('/new', methods=['POST'])
def new():

	item_doc = {
		'name': request.form['name'],
		'description': request.form['description']
	}
	db.tododb.insert_one(item_doc)

	return redirect(url_for('todo'))

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)


