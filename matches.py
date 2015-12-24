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
        query = "SELECT MATCHES.ID, Team1.Team_Name, Team2.Team_Name, MATCHES.ArenaName, MATCHES.RefereeName FROM MATCHES INNER JOIN TEAMS AS TEAM1 ON MATCHES.TEAM1ID = TEAM1.ID INNER JOIN TEAMS AS TEAM2 ON MATCHES.TEAM2ID = TEAM2.ID"

        cursor.execute(query)
        return render_template('matches.html', matches = cursor)
    else:
        Team1Name_in = request.form['Team1ID']
        Team2Name_in = request.form['Team2ID']
        ArenaName_in = request.form['ArenaName']
        RefereeName_in = request.form['RefereeName']

        query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName)
        VALUES ('"""+Team1Name_in+"', '"+Team2Name_in+"', '"+ArenaName_in+"', '"+RefereeName_in+"')"
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
    cursor2 = connection.cursor()
    query = "SELECT ID, Team_Name FROM TEAMS"
    cursor2.execute(query)

    cursor.execute("""SELECT ID, Team1ID, Team2ID, ArenaName, RefereeName FROM MATCHES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('matches_edit.html', matches = cursor, teams = cursor2)

@app.route('/matches/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def matches_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name1 = request.form['Team1ID']
    new_name2 = request.form['Team2ID']
    new_arena = request.form['ArenaName']
    new_referee = request.form['RefereeName']
    query = """UPDATE MATCHES SET Team1ID = %d, Team2ID = %d, ArenaName = '%s', RefereeName = '%s' WHERE ID = %d""" % (int(new_name1), int(new_name2), new_arena, new_referee, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('matches_page'))


@app.route('/matches/initdb')
def initialize_database_matches():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS MATCHES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE MATCHES (ID SERIAL PRIMARY KEY, Team1ID INTEGER NOT NULL, Team2ID INTEGER NOT NULL, ArenaName VARCHAR, RefereeName VARCHAR,
            FOREIGN KEY (Team1ID) REFERENCES TEAMS(ID) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (Team2ID) REFERENCES TEAMS(ID) ON UPDATE CASCADE ON DELETE CASCADE
            )"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (1, 3, 'Sinan Erdem', 'Brad Aaberg')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (2, 11 , 'Abdi Ipekci', 'Stephen Arichea')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (8, 9 , 'FB Ulker', 'Rose Atkinson')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (13, 4 , 'Volkswagen Arena', 'Dan Apol')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (18, 1 , 'Burhan Felek', 'Mary Black')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (15, 7 , 'Pavilhao Rosa Mota', 'Fred Buchler')"""
    cursor.execute(query)


    connection.commit()
    return redirect(url_for('matches_page'))

