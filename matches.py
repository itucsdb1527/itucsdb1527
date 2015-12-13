import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/matches', methods=['GET', 'POST'])
def matches_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM MATCHES"
        cursor.execute(query)
        return render_template('matches.html', matches = cursor)
    else:
        Team1Name_in = request.form['Team1Name']
        Team2Name_in = request.form['Team2Name']
        ArenaName_in = request.form['ArenaName']
        RefereeName_in = request.form['RefereeName']
        Season_in = request.form['Season']

        query = """INSERT INTO MATCHES (Team1Name, Team2Name, ArenaName, RefereeName, Season)
        VALUES ('"""+Team1Name_in+"', '"+Team2Name_in+"', '"+ArenaName_in+"', '"+RefereeName_in+"', '"+Season_in+"')"
        cursor.execute(query)

        connection.commit()
        return redirect(url_for('matches_page'))

    return render_template('matches.html')

@app.route('/matches/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def matches_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()

        cursor.execute("""DELETE FROM MATCHES WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('matches_page'))


@app.route('/matches/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def matches_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Team1Name, Team2Name, ArenaName, RefereeName, Season FROM MATCHES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('matches_edit.html', matches = cursor)

@app.route('/matches/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def matches_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name1 = request.form['Team1Name']
    new_name2 = request.form['Team2Name']
    new_arena = request.form['ArenaName']
    new_referee = request.form['RefereeName']
    new_season = request.form['Season']
    query = """UPDATE MATCHES SET Team1Name = '%s', Team2Name = '%s', ArenaName = '%s', RefereeName = '%s', Season = %d WHERE ID = %d""" % (new_name1, new_name2, new_arena, new_referee ,int(new_season), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('matches_page'))


@app.route('/matches/initdb')
def initialize_database_matches():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS MATCHES"""
    cursor.execute(query)
    query = """CREATE TABLE MATCHES (ID SERIAL PRIMARY KEY, Team1Name VARCHAR NOT NULL, Team2Name VARCHAR NOT NULL, ArenaName VARCHAR, RefereeName VARCHAR, Season INTEGER)"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1Name, Team2Name, ArenaName, RefereeName, Season) VALUES ('Besiktas', 'Galatasaray', 'Brad Aaberg','Akatlar', 2014)"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1Name, Team2Name, ArenaName, RefereeName, Season) VALUES ('Barcelona', 'Real Madrid', 'Cuneyt Cakir','Inonu', 2015)"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('matches_page'))

