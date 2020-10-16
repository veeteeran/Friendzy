#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.interest import Interest
from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/interests_list', strict_slashes=False)
def interests_list():
    """ displays a HTML page with a list of interests """
    interests = storage.all(Interest).values()
    interests = sorted(interests, key=lambda k: k.id)
    test_list = []
    full_list = []
    i = 0
    while i < len(interests) - 1:
        if i % 3 == 0 and i != 0:
            full_list.append(test_list)
            test_list = []
        test_list.append(interests[i])
        i += 1
    return render_template("home.html", full_list=full_list)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
