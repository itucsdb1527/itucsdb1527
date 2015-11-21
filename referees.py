import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/referees', methods=['GET', 'POST'])
def referees_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM REFEREES"
        cursor.execute(query)
        return render_template('referees.html', referees = cursor)
    else:
        name_in = request.form['name']
        age_in = request.form['age']
        nationality_in = request.form['nationality']
        query = """INSERT INTO REFEREES (RefereeName, RefereeAge, RefereeNationality)
        VALUES ('"""+name_in+"', '"+age_in+"', '"+nationality_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('referees_page'))

@app.route('/referees/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def referees_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM REFEREES WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('referees_page'))
    
@app.route('/referees/initdb')
def initialize_database_referees():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()
        
    query = """DROP TABLE IF EXISTS REFEREES"""
    cursor.execute(query)
    query = """CREATE TABLE REFEREES (ID SERIAL PRIMARY KEY, RefereeName VARCHAR NOT NULL, RefereeAge INTEGER, RefereeNationality VARCHAR NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Cuneyt Cakir',39,'Turkiye')"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Felix Brych',40,'Deutchland')"""
    cursor.execute(query)
    
    connection.commit()
    return redirect(url_for('referees_page'))      
    