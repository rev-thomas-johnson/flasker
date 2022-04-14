from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

# Create a Form Class
class NamerForm(FlaskForm):
	name = StringField("What's Your Name?", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a route decorator

@app.route('/')
def index():
	first_name = "John"
	stuff = "This is <strong>Bold</strong> text."
	fav_pizzas = ["Pepporoni", "Sausage", "Cheese", 41]
	return render_template("index.html", first_name=first_name,
		stuff=stuff, fav_pizzas=fav_pizzas)


@app.route('/user/<name>')
def user(name):
	return render_template("user.html", name=name)


# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500


# Create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	# Validate Form
	if form.validate_on_submit():
		name = form.name.data 
		form.name.data = ''

	return render_template("name.html",
		name = name,
		form = form)




# Filters
# safe - removes tags and uses them
# capitalize
# lower
# upper
# title
# trim - removes trailing whitespace
# striptags - removes tags without using them
