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
        query = "SELECT * FROM PLAYERS"
        cursor.execute(query)
        return render_template('players.html', players = cursor)
    else:
        name_in = request.form['name']
        number_in = request.form['number']
        team_in = request.form['teamID']
        country_in = request.form['countryID']
        age_in = request.form['age']
        query = """INSERT INTO PLAYERS (name,number,team,country,age) VALUES ('"""+name_in+"', '"+number_in+"', '"+team_in+"', '"+country_in+"' , '"+age_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('players_page'))
    
@app.route('/players/initdb')
def initialize_database_players():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()
        
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
    return redirect(url_for('players_page'))  