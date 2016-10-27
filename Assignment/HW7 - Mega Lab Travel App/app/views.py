from flask import render_template, session, redirect, request, url_for, escape
from app import app, models, db
from .forms import TripForm
from models import *
# Access the models file to use SQL functions

@app.route('/')
@app.route('/index')
def index():
	username = ''
	if 'username' in session:
		username = escape(session['username'])
		return redirect('/display_trips')
	else:
		return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form.get("username")
        session['password'] = request.form.get("password")
        result = check_login(session['username'], session['password'])
        if len(result) == 0:
            print("invalid login. Try again")
            session.pop('username', None)
            session.pop('password', None)
        else:
            session['id'] = result[0][0]
            print("user id")
            print(session['id'])
    return redirect(url_for('index'))
    # return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('password', None)
	return redirect(url_for('index'))

@app.route('/display_trips')
def display_trips():
    username = escape(session['username'])
    user_id = escape(session['id'])
    trips = retrieve_trips(user_id)
    return render_template('trips.html', username = username, trips = trips)

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    form = TripForm()
    form.friend.choices = friend_choices(escape(session['username']))

    if form.validate_on_submit():
        name = form.name.data
        destination = form.destination.data
        friend_id = form.friend.data
        insert_trip(escape(session['id']), name, destination, friend_id)
        return redirect('/display_trips')
    print(form.errors)
    username = escape(session['username'])
    return render_template('create.html', username=username, form=form)

@app.route('/delete_trip/<value>', methods=['GET', 'POST'])
def delete_trip(value):
    remove_trip(value)
    return redirect('/display_trips')

@app.route('/ajax_delete', methods=['GET', 'POST'])
def ajax_delete():
    if request.method == 'POST':
        remove_trip(str(request.form['id']))
    return ('', 204)
