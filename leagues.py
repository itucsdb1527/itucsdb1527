import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/leagues/initdb')
def initialize_database_leagues():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    query = """DROP TABLE IF EXISTS LEAGUES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE LEAGUES (
                    ID SERIAL PRIMARY KEY,
                    League_Name VARCHAR NOT NULL,
                    Country_ID INTEGER NOT NULL

                    )"""
    cursor.execute(query)
#/*FOREIGN KEY Country_ID INTEGER NOT NULL REFERENCES COUNTRIES(ID) ON DELETE CASCADE ON UPDATE CASCADE*/
    query = """INSERT INTO LEAGUES (League_Name,Country_ID) VALUES ('Aroma Erkekler Voleybol Ligi',1)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,Country_ID) VALUES ('Premier Lig',2)"""
    cursor.execute(query)

    # Seasons

    query = """DROP TABLE IF EXISTS SEASONS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE SEASONS (
                    ID SERIAL PRIMARY KEY,
                    Season_Name VARCHAR NOT NULL,
                    League_ID INTEGER NOT NULL,
                    FOREIGN KEY (League_ID) REFERENCES LEAGUES(ID) ON DELETE CASCADE ON UPDATE CASCADE
                    )"""
    cursor.execute(query)

    query = """INSERT INTO SEASONS (League_ID,Season_Name) VALUES (1,'2016 Ligi')"""
    cursor.execute(query)
    query = """INSERT INTO SEASONS (League_ID,Season_Name) VALUES (2,'2017 Ligi')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('leagues_page'))

@app.route('/leagues', methods=['GET', 'POST'])
def leagues_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT ID, League_Name, Country_ID FROM LEAGUES"
        cursor.execute(query)
        return render_template('leagues.html', leagues = cursor)
    else:
        name = request.form['name']
        country = request.form['country']
        query = """INSERT INTO LEAGUES (League_Name,Country_ID)
        VALUES ('"""+name+"','"+country+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('leagues_page'))

@app.route('/leagues/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def leagues_page_delete(DELETEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM LEAGUES WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('leagues_page'))

@app.route('/leagues/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def leagues_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, League_Name, Country_ID FROM LEAGUES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('leagues_edit.html', leagues = cursor)

@app.route('/leagues/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def leagues_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_country = request.form['country']
    query = """UPDATE LEAGUES SET League_Name = '%s', Country_ID = %d WHERE ID = %d""" % (new_name,int(new_country), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('leagues_page'))


