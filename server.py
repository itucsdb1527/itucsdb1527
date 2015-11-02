import datetime
import os

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/leagues')
def leagues_page():
    return render_template('leagues.html')

@app.route('/teams')
def teams_page():
    return render_template('teams.html')

@app.route('/matches')
def matches_page():
    return render_template('matches.html')

@app.route('/players')
def players_page():
    return render_template('players.html')

@app.route('/referees')
def referees_page():
    return render_template('referees.html')

@app.route('/arenas')
def arenas_page():
    return render_template('arenas.html')



if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)
