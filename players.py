import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/players', methods=['GET', 'POST'])
def players_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT PLAYERS.ID, NAME,NATIONALITY, AGE, NUMBER, POSITION FROM PLAYERS, NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID"
        cursor.execute(query)
        cursor2 = connection.cursor()
        query = "SELECT * FROM NATIONALITIES"
        cursor2.execute(query)
        return render_template('players.html', players = cursor, nationalities = cursor2)
    else:
        search = request.form['search']
        query = "SELECT PLAYERS.ID, NAME, NATIONALITY, AGE, NUMBER, POSITION FROM PLAYERS, NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID AND NAME LIKE '%" + search +"%'"
        cursor.execute(query)
        connection.commit()
        return render_template('players.html', players = cursor)
