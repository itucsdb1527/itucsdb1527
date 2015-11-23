import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/teams/initdb')
def initialize_database_teams():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    #Teams Table
    query = """DROP TABLE IF EXISTS TEAMS CASCADE"""
    cursor.execute(query)

    query = """CREATE TABLE TEAMS(
    ID SERIAL PRIMARY KEY,
    Team_Name VARCHAR NOT NULL
    )"""
    cursor.execute(query)

    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Galatasaray')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Besiktas')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Fenerbahce')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Ziraat Bankasi')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Halkbank')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Istanbul B.S.B.')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Sahinbey Bld.')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Maliye Milli Piyango')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Tokat Bld. Plevne')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Inegol Bld.')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Arkas Spor')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Bornova Anadolu Lisesi')"""
    cursor.execute(query)


    #Season Team Table
    query = """DROP TABLE IF EXISTS SEASON_TEAM CASCADE"""
    cursor.execute(query)

    query = """CREATE TABLE SEASON_TEAM(
    Season_ID INTEGER,
    Team_ID INTEGER,
    PRIMARY KEY(Season_ID, Team_ID),
    FOREIGN KEY (Season_ID) REFERENCES SEASONS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Team_ID) REFERENCES TEAMS(ID) ON DELETE CASCADE ON UPDATE CASCADE
    )"""
    cursor.execute(query)

    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 1)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 2)"""
    cursor.execute(query)


    #Admin Table
    query = """DROP TABLE IF EXISTS SITE CASCADE"""
    cursor.execute(query)

    query = """CREATE TABLE SITE(
    Admin_Name VARCHAR NOT NULL,
    Admin_Password VARCHAR NOT NULL,
    Site_Name VARCHAR NOT NULL,
    Slogan VARCHAR NOT NULL
    )"""
    cursor.execute(query)

    query = """INSERT INTO SITE (Admin_Name, Admin_Password, Site_Name, Slogan) VALUES ('Meric','lolololo','itucsdb1527','Cimbombom')"""
    cursor.execute(query)


    connection.commit()
    return redirect(url_for('teams_page'))


@app.route('/teams', methods=['GET', 'POST'])
def teams_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT ID, Team_Name FROM TEAMS ORDER BY ID"
        cursor.execute(query)
        return render_template('teams.html', teams = cursor)
    else:
        name = request.form['name']
        query = """INSERT INTO TEAMS (Team_Name)
        VALUES ('"""+name+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('teams_page'))

@app.route('/teams/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def teams_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM TEAMS WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('teams_page'))


@app.route('/teams/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def teams_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Team_Name FROM TEAMS WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('teams_edit.html', teams = cursor)

@app.route('/teams/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def teams_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    query = """UPDATE TEAMS SET Team_Name = '%s' WHERE ID = %d""" % (new_name, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('teams_page'))


