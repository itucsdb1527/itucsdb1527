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
        query = "SELECT * FROM PLAYERS WHERE Name LIKE '%" + search +"%'"
        cursor.execute(query)
        connection.commit()
        return render_template('players.html', players = cursor)

@app.route('/ADMIN/players', methods=['GET', 'POST'])
def admin_players_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT PLAYERS.ID, NAME, NATIONALITY, AGE, NUMBER, POSITION FROM PLAYERS, NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID"
        cursor.execute(query)
        cursor2 = connection.cursor()
        query = "SELECT * FROM NATIONALITIES"
        cursor2.execute(query)
        return render_template('admin/players.html', players = cursor, nationalities = cursor2)
    else:
        name_in = request.form['name']
        nationality_in = request.form['nationalityID']
        age_in = request.form['age']
        number_in = request.form['number']
        position_in = request.form['position']
        query = """INSERT INTO PLAYERS (NAME, NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('"""+name_in+"', '"+nationality_in+"', '"+age_in+"', '"+number_in+"', '"+position_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_players_page'))

@app.route('/ADMIN/players/initdb')
def admin_initialize_database_players():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    query = """DROP TABLE IF EXISTS PLAYERS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE PLAYERS (
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR NOT NULL,
                    NATIONALITY_ID INTEGER NOT NULL,
                    AGE INTEGER NOT NULL,
                    NUMBER INTEGER NOT NULL,
                    POSITION VARCHAR NOT NULL,
                    FOREIGN KEY (NATIONALITY_ID) REFERENCES NATIONALITIES(ID) ON DELETE CASCADE ON UPDATE CASCADE
                    )"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('MERAL',1, 20, 8,'SETTER')"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('CEMAL',1, 24, 15,'LIBERO')"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('SEYMA',1, 21, 9,'OPPOSITE')"""
    cursor.execute(query)


##### COUNTRIES #####
    query = """DROP TABLE IF EXISTS COUNTRIES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE COUNTRIES (
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR NOT NULL
                    )"""
    cursor.execute(query)

    query = """INSERT INTO COUNTRIES (NAME) VALUES ('TURKEY')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('ENGLAND')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('USA')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('GERMANY')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('FRANCE')"""
    cursor.execute(query)

##### TEAMPLAYERS #####
    query = """DROP TABLE IF EXISTS TEAMPLAYERS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE TEAMPLAYERS (
                    PLAYERID INTEGER NOT NULL,
                    TEAMID INTEGER NOT NULL,
                    SEASONID INTEGER NOT NULL,
                    FOREIGN KEY (PLAYERID) REFERENCES PLAYERS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (TEAMID) REFERENCES TEAMS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (SEASONID) REFERENCES SEASONS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    PRIMARY KEY (PLAYERID, TEAMID, SEASONID)
                    )"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('admin_players_page'))

@app.route('/ADMIN/players/DELETE/<int:DELETEID>', methods=['GET','POST'])
def admin_players_page_delete(DELETEID):
    connection=dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM PLAYERS WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_players_page'))

@app.route('/ADMIN/players/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_players_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM PLAYERS WHERE ID = %s", (int(UPDATEID),))
    cursor2 = connection.cursor()
    query = "SELECT * FROM NATIONALITIES"
    cursor2.execute(query)
    connection.commit()
    return render_template('admin/players_edit.html', players = cursor, nationalities = cursor2)

@app.route('/ADMIN/players/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_players_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_nationality = request.form['nationalityID']
    new_age = request.form['age']
    new_number = request.form['number']
    new_position = request.form['position']
    query = "UPDATE PLAYERS SET NAME = '%s', NATIONALITY_ID = %d, AGE = %d, NUMBER = %d, POSITION = '%s'  WHERE ID = %d" % (new_name,int(new_nationality),int(new_age), int(new_number), new_position, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_players_page'))

@app.route('/ADMIN/countries', methods=['GET', 'POST'])
def admin_countries_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM COUNTRIES"
        cursor.execute(query)
        return render_template('admin/countries.html', countries = cursor)
    else:
        name_in = request.form['name']
        query = """INSERT INTO COUNTRIES (name) VALUES ('"""+name_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_countries_page'))

@app.route('/ADMIN/countries/DELETE/<int:DELETEID>', methods=['GET','POST'])
def admin_countries_page_delete(DELETEID):
    connection=dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM COUNTRIES WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_countries_page'))

@app.route('/ADMIN/countries/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_countries_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM COUNTRIES WHERE ID = %s", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/countries_edit.html', countries = cursor)

@app.route('/ADMIN/countries/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_countries_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    query = """UPDATE COUNTRIES SET NAME = '%s' WHERE ID = %d""" % (new_name, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_countries_page'))

@app.route('/ADMIN/teamplayers', methods=['GET', 'POST'])
def admin_team_players_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT PLAYERS.ID, SEASONS.ID, TEAMS.ID FROM PLAYERS, SEASONS, TEAMS"
        cursor.execute(query)
        return render_template('/ADMIN/teamplayers', teamplayers = cursor)
    else:
        playerid_in = request.form['playerid']
        seasonid_in = request.form['seasonid']
        teamid_in = request.form['teamid']
        query = """INSERT INTO TEAMPLAYERS (PLAYERID, SEASONID, TEAMID) VALUES VALUES ('"""+playerid_in+"', '"+seasonid_in+"', '"+teamid_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_team_players_page'))

@app.route('/ADMIN/teamplayers/DELETE/<int:DELETEID>', methods=['GET','POST'])
def admin_team_players_page_delete(DELETEID):
    connection=dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM TEAMPLAYERS WHERE PLAYERID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_team_players_page'))

@app.route('/ADMIN/teamplayers/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_team_players_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM TEAMPLAYERS WHERE PLAYERID = %s", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/teamplayers_edit.html', teamplayers = cursor)

@app.route('/ADMIN/teamplayers/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_team_players_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_playerid = request.form['newPlayer']
    new_seasonid = request.form['newSeason']
    new_teamid = request.form['newTeam']
    query = "UPDATE TEAMPLAYERS SET PLAYERID = %d, SEASONID = %d, TEAMID = %d WHERE PLAYERID = %d" % (int(new_playerid), int(new_seasonid), int(new_teamid), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_team_players_page'))