import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

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

@app.route('/leagues/initdb')
def initialize_database_leagues():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()
        
    query = """DROP TABLE IF EXISTS LEAGUES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE LEAGUES (ID SERIAL PRIMARY KEY, League_Name VARCHAR NOT NULL, League_Logo VARCHAR, League_Start_Date INTEGER, Country_ID INTEGER NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,League_Logo,Country_ID) VALUES ('Aroma Erkekler Voleybol Ligi','http://dwmdwmdk.com/img/logo1.jpg',1)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,League_Logo,Country_ID) VALUES ('Premier Lig','http://dwmdwmdk.com/img/logo1.jpg',2)"""
    cursor.execute(query)
    
    connection.commit()
    return redirect(url_for('leagues_page'))    