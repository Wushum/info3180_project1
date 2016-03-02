from . import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	userid = db.Column(db.String(10), unique=True)
	gender = db.Column(db.String(10))
	age =db.Column(db.Integer)
	image = db.Column(db.String(80))

	def __init__(self, first_name, last_name, userid, gender, age, image):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.userid = userid
		self.age = age
		self.image = image

	def __repr__(self):
		return '<User %r>' % self.userid
