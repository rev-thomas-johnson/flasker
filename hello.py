from flask import Flask, render_template


# Create a Flask instance

app = Flask(__name__)

# Create a route decorator

@app.route('/')
def index():
	first_name = "John"
	stuff = "This is <strong>Bold</strong> text."
	fav_pizzas = ["Pepporoni", "Sausuage", "Cheese", 41]
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

