import datetime
import os
import json
import re
import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/leagues', methods=['GET', 'POST'])
def leagues_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM LEAGUES"
        cursor.execute(query)
        return render_template('leagues.html', leagues = cursor)
    else:
        name = request.form['name']
        logo = request.form['logo']
        year = request.form['year']
        country = request.form['country']
        query = """INSERT INTO LEAGUES (League_Name,League_Logo,League_Start_Date,Country_ID)
        VALUES ('"""+name+"', '"+logo+"', '"+year+"' , '"+country+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('leagues_page'))

@app.route('/leagues/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def leagues_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM leagues WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('leagues_page'))


@app.route('/teams', methods=['GET', 'POST'])
def teams_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM TEAMS"
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


@app.route('/matches')
def matches_page():
    return render_template('matches.html')

@app.route('/players', methods=['GET', 'POST'])
def players_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM PLAYERS"
        cursor.execute(query)
        return render_template('players.html', players = cursor)
    else:
        name_in = request.form['name']
        number_in = request.form["number"]
        team_in = request.form["teamID"]
        country_in = request.form["countryID"]
        age_in = request.form["age"]
        query = """INSERT INTO PLAYERS (name,number,team,country,age) VALUES ('"""+name_in+"', '"+number_in+"', '"+country_in+"' , '"+age_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('players_page'))

@app.route('/referees')
def referees_page():
    return render_template('referees.html')

@app.route('/arenas')
def arenas_page():
    return render_template('arenas.html')

@app.route('/initdb')
def initialize_database():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    query = """DROP TABLE IF EXISTS COUNTER"""
    cursor.execute(query)
    query = """CREATE TABLE COUNTER (N INTEGER)"""
    cursor.execute(query)
    query = """INSERT INTO COUNTER(N) VALUES(0)"""
    cursor.execute(query)

    query = """DROP TABLE IF EXISTS LEAGUES"""
    cursor.execute(query)
    query = """CREATE TABLE LEAGUES (ID SERIAL PRIMARY KEY, League_Name VARCHAR NOT NULL, League_Logo VARCHAR, League_Start_Date INTEGER, Country_ID INTEGER NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,League_Logo,Country_ID) VALUES ('Super Lig','http://dwmdwmdk.com/img/logo1.jpg',1)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,League_Logo,Country_ID) VALUES ('Premier Lig','http://dwmdwmdk.com/img/logo1.jpg',2)"""
    cursor.execute(query)

    query = """DROP TABLE IF EXISTS TEAMS"""
    cursor.execute(query)
    query = """CREATE TABLE TEAMS (ID SERIAL PRIMARY KEY, Team_Name VARCHAR NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Galatasaray')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Besiktas')"""
    cursor.execute(query)

    query = """DROP TABLE IF EXISTS PLAYERS"""
    cursor.execute(query)
    query = """CREATE TABLE PLAYERS (ID SERIAL PRIMARY KEY, name VARCHAR NOT NULL, number INTEGER NOT NULL, team INTEGER, country INTEGER NOT NULL, age INTEGER NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (name,number,team,country,age) VALUES ('BabeRuth',3,4,1,24)"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (name,number,team,country,age) VALUES ('MEral',1,17,2,20)"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (name,number,team,country,age) VALUES ('Cemal',16,17,1,24)"""
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('home_page'))

@app.route('/count')
def counter_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = "UPDATE COUNTER SET N = N + 1"
    cursor.execute(query)
    connection.commit()

    query = "SELECT N FROM COUNTER"
    cursor.execute(query)
    count = cursor.fetchone()[0]

    return "This page was accessed %d times." % count


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='postgres' password='12345'
                               host='localhost' port=5432 dbname='itucsdb'"""
    app.run(host='0.0.0.0', port=port, debug=debug)
