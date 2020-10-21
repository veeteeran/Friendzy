#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from flask.helpers import url_for
from models.interest import Interest
from models import storage
from models.user import User
from models.form import SignupForm
from flask import Flask, render_template, abort, jsonify, flash, redirect
import requests
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """
    Retrieves the list of all interest objects
    or a specific interest
    """
    form = SignupForm()
    return render_template(
        'register.html',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    email = form.email.data
    password = form.password.data
    all = storage.all(User)
    for user in all.values():
        if email == user.email:
            if user.check_password(password):
                return redirect("http://127.0.0.1:5000/interests_list")
    flash('invalid password or email')
    return render_template(
        'login.html',
        form=form
    )



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    new = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data
                )
    all = storage.all(User)
    for user in all.values():
        if new.email == user.email:
            flash('A user already exists with that email address.')
            return render_template(
                'register.html',
                form=form
                )
    new.save()
    return render_template(
        'login.html',
        form=form
    )

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001, debug=True)