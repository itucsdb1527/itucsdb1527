import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

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

@app.route('/teams/initdb')
def initialize_database_teams():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()
        
    query = """DROP TABLE IF EXISTS TEAMS"""
    cursor.execute(query)
    query = """CREATE TABLE TEAMS (ID SERIAL PRIMARY KEY, Team_Name VARCHAR NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Galatasaray')"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name) VALUES ('Besiktas')"""
    cursor.execute(query)
    
    connection.commit()
    return redirect(url_for('teams_page'))    