import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/scores', methods=['GET', 'POST'])
def scores_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM SCORES"
        cursor.execute(query)
        return render_template('scores.html', scores = cursor)
    else:
        MatchID_in = request.form['MatchID']
        Team1Score_in = request.form['Team1Score']
        Team2Score_in = request.form['Team2Score']

        query = """INSERT INTO SCORES (MatchID ,Team1Score, Team2Score)
        VALUES ('"""+MatchID_in+"', '"+Team1Score_in+"', '"+Team2Score_in+"')"
        cursor.execute(query)

        connection.commit()
        return redirect(url_for('scores_page'))





    return render_template('scores.html')

@app.route('/scores/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def scores_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()

        cursor.execute("""DELETE FROM SCORES WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('scores_page'))


@app.route('/scores/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def scores_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, MatchID, Team1Score, Team2Score FROM SCORES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('scores_edit.html', scores = cursor)

@app.route('/scores/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def scores_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_match = request.form['MatchID']
    new_name1 = request.form['Team1Score']
    new_name2 = request.form['Team2Score']
    query = """UPDATE SCORES SET MatchID = '%d', Team1Score = '%s', Team2Score = '%s' WHERE ID = %d""" % (int(new_match), new_name1, new_name2, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('scores_page'))


@app.route('/scores/initdb')
def initialize_database_scores():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS SCORES"""
    cursor.execute(query)
    query = """CREATE TABLE SCORES (ID SERIAL PRIMARY KEY, MatchID INTEGER NOT NULL, Team1Score VARCHAR NOT NULL, Team2Score VARCHAR NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('12', '25', '23')"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('1', '23', '25')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('scores_page'))

