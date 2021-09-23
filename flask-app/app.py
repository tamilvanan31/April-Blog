from flask import Flask, render_template, url_for, flash, redirect 
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '00a95c64804aedcf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post

posts = [
	{
		'author': 'Tamilvanan',
		'title': 'Blog Post 1',
		'content': 'Welcome to my flask blog',
		'date_posted': 'April 2, 2021'
	},
	{
		'author': 'Mathivanan',
		'title': 'Blog Post 2',
		'content': 'Welcome to my flask blog',
		'date_posted': 'April 25, 2021'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)	


if __name__ == '__main__':
	app.run(debug = True)
