import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/nationalities/initdb')
def initialize_database_nationalities():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS NATIONALITIES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE NATIONALITIES (ID SERIAL PRIMARY KEY, Nationality VARCHAR NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('North Country')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Northern California')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Sun Country')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Turkey')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('nationalities_page'))


@app.route('/nationalities', methods=['GET', 'POST'])
def nationalities_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM NATIONALITIES"
        cursor.execute(query)
        return render_template('nationalities.html', nationalities = cursor)
    else:
        nationality_in = request.form['nationality']
        query = """INSERT INTO NATIONALITIES (Nationality)
        VALUES ('"""+nationality_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('nationalities_page'))

@app.route('/nationalities/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def nationalities_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM NATIONALITIES WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('nationalities_page'))


@app.route('/s/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def nationalities_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Nationality FROM NATIONALITIES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('nationalities_edit.html', nationalities = cursor)

@app.route('/nationalities/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def nationalities_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_nationality = request.form['nationality']
    query = """UPDATE NATIONALITIES SET Nationality = '%s' WHERE ID = %d""" % (new_nationality, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('nationalities_page'))
