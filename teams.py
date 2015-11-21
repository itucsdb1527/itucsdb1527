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
        query = "SELECT T.ID, T.Team_Name, L.League_Name, T.League_ID FROM TEAMS T LEFT JOIN LEAGUES L ON (T.League_ID = L.ID)"
        cursor.execute(query)
        return render_template('teams.html', teams = cursor)
    else:
        name = request.form['name']
        league_id = request.form['league_id']        
        query = """INSERT INTO TEAMS (Team_Name, League_ID)
        VALUES ('"""+name+"', '"+league_id+"')"
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
        
    query = """DROP TABLE IF EXISTS TEAMS CASCADE"""
    cursor.execute(query)
    
    query = """CREATE TABLE TEAMS(
    ID SERIAL PRIMARY KEY, 
    Team_Name VARCHAR NOT NULL, 
    League_ID INTEGER,
    FOREIGN KEY (League_ID) REFERENCES LEAGUES(ID) ON DELETE CASCADE
    )"""
    cursor.execute(query)
    
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Galatasaray', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Besiktas', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Fenerbahce', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Ziraat Bankasi', 1)"""
    cursor.execute(query)    
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Halkbank', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Istanbul B.S.B.', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Sahinbey Bld.', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Maliye Milli Piyango', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Tokat Bld. Plevne', 1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Inegol Bld.', 1)"""
    cursor.execute(query)        
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Arkas Spor', 1)"""
    cursor.execute(query)   
    query = """INSERT INTO TEAMS (Team_Name, League_ID) VALUES ('Bornova Anadolu Lisesi', 1)"""
    cursor.execute(query)   
        
    connection.commit()
    return redirect(url_for('teams_page'))    