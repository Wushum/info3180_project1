from app import app, db
from flask import render_template, request, url_for, redirect, send_from_directory, jsonify
from werkzeug import secure_filename
from app.models import User 
from app.forms import UserForm

import os
from random import randint

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/filefolder/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
	""" Render the home page """
	return render_template('home.html')

@app.route('/profile/', methods=['GET', 'POST'])
def new_profile():

	if request.method == 'GET':
		""" display user form here """
		form = UserForm()
		return render_template('add_profile.html', form=form)
	elif request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		gender = request.form['gender']
		userid = str(generate_id())
		age = request.form['age']
		image = request.files['image']

		filename = secure_filename(image.filename).lower()
		image.save(app.config['UPLOAD_FOLDER'] +  filename)
	
		user = User(first_name, last_name, userid, gender, 30, filename)

		db.session.add(user)
		db.session.commit()
		return redirect(url_for('all_profiles'))

@app.route('/profiles/', methods=['GET', 'POST'])
def all_profiles():
	""" List of all profiles """

	users = User.query.all()

	if request.method == 'GET':
		return render_template('profiles.html', users=users)
	elif request.method == 'POST' or ('Content-Type' in request.headers['Content-Type'] == 'application/json'):
		return transform_user(users=users)

@app.route('/profile/<int:id>', methods=['GET', 'POST'])
def show_profile(id):
	""" View a Profile """
	
	user = retreive_user(id)

	if request.method == 'GET':
		return render_template('profile.html', user=user)
	elif request.method == 'POST':
		return transform_user(user)

@app.route('/img/<path>')
def serve_file(path):
	dir = os.path.join(app.root_path, "../filefolder")
	return send_from_directory(dir, path)

@app.after_request
def add_header(response):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the render page for 10 minutes.
	"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public,max-age=600'
	return response

@app.errorhandler(404)
def page_not_found(error):
	""" Custom 404 page. """
	return "404"
	
"""
	Private helper functions
"""
def retreive_user(id):
	return User.query.filter(User.id == id).first()

def transform_user(user):
	return jsonify(user_id=user.userid,
			first_name=user.first_name,
			last_name=user.last_name,
			sex=user.gender,
			age=user.age,
			image=user.image)

def generate_id():
	return 620000000 + randint(0, 9999)

