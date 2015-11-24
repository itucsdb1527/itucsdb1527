import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/maillist', methods=['GET', 'POST'])
def maillist_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM MAILLIST"
        cursor.execute(query)
        return render_template('maillist.html', maillist = cursor)
    else:
        Mail_in = request.form['Mail']
        TeamID_in = request.form['TeamID']

        query = """INSERT INTO MAILLIST (Mail, TeamID)
        VALUES ('"""+Mail_in+"', '"+TeamID_in+"')"
        cursor.execute(query)

        connection.commit()
        return redirect(url_for('maillist_page'))

    return render_template('maillist.html')

@app.route('/maillist/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def maillist_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()

        cursor.execute("""DELETE FROM MAILLIST WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('maillist_page'))


@app.route('/maillist/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def maillist_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Mail, TeamID FROM MAILLIST WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('maillist_edit.html', maillist = cursor)

@app.route('/maillist/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def maillist_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_mail = request.form['Mail']
    new_teamID = request.form['TeamID']
    query = """UPDATE MAILLIST SET Mail = '%s', TeamID = '%s' WHERE ID = %d""" % (new_mail, new_teamID, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('maillist_page'))


@app.route('/maillist/initdb')
def initialize_database_maillist():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS MAILLIST"""
    cursor.execute(query)
    query = """CREATE TABLE MAILLIST (ID SERIAL PRIMARY KEY, Mail VARCHAR NOT NULL, TeamID VARCHAR NOT NULL)"""
    cursor.execute(query)
    query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('ozkalt@itu.edu.tr', 'itucsdb27')"""
    cursor.execute(query)
    query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('umutlus@itu.edu.tr','itucsdb27')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('maillist_page'))

