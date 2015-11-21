import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/matches')
def matches_page():
    return render_template('matches.html')


@app.route('/matches/initdb')
def initialize_database_matches():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()
    
    connection.commit()
    return redirect(url_for('matches_page'))   