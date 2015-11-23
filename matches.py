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
        Team1name_in = request.form['Team1name']
        Team2name_in = request.form['Team2name']
        ArenaName_in = request.form['ArenaName']
        RefereeName_in = request.form['RefereeName']
        Season_in = request.form['Season']

        query = """INSERT INTO MATCHES (Team1name, Team2name, ArenaName, RefereeName, Season)
        VALUES ('"""+Team1name_in+"', '"+Team2name_in+"', '"+ArenaName_in+"', '"+RefereeName_in+"', '"+Season_in+"')"
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

@app.route('/matches/initdb')
def initialize_database_matches():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS MATCHES"""
    cursor.execute(query)
    query = """CREATE TABLE MATCHES (ID SERIAL PRIMARY KEY, Team1name VARCHAR NOT NULL, Team2name VARCHAR NOT NULL, ArenaName VARCHAR, RefereeName VARCHAR, Season INTEGER)"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1name,Team2name,ArenaName, RefereeName, Season) VALUES ('Besiktas', 'Galatasaray', 'Brad Aaberg','Akatlar', 2014)"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1name,Team2name,ArenaName, RefereeName, Season) VALUES ('Barcelona', 'Real Madrid', 'Cuneyt Cakir','Inonu', 2015)"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('matches_page'))

