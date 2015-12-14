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

    if  request.method == 'GET':
        query = "SELECT REFEREES.ID, REFEREES.RefereeName, REFEREES.RefereeAge, NATIONALITIES.Nationality FROM REFEREES INNER JOIN NATIONALITIES ON REFEREES.RefereeNationality = NATIONALITIES.ID"
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
    cursor = connection.cursor()

    query = """DROP TABLE IF EXISTS REFEREES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE REFEREES (ID SERIAL PRIMARY KEY, RefereeName VARCHAR NOT NULL, RefereeAge INTEGER, RefereeNationality INTEGER NOT NULL,
    FOREIGN KEY (RefereeNationality) REFERENCES NATIONALITIES(ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Brad Aaberg',39,1)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Keith Aidun',40,2)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Cedric All Runner',40,9)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Dan Apol',35,4)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Mary Black',28,3)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Rose Atkinson',42,7)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Stephen Arichea',37,6)"""
    cursor.execute(query)
    query = """INSERT INTO REFEREES (RefereeName,RefereeAge,RefereeNationality) VALUES ('Fred Buchler',39,5)"""
    cursor.execute(query)


    connection.commit()
    return redirect(url_for('referees_page'))

@app.route('/referees/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def referees_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    query = "SELECT ID, Nationality FROM NATIONALITIES"
    cursor2.execute(query)
    cursor.execute("""SELECT ID, RefereeName, RefereeAge FROM REFEREES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('referees_edit.html', referees = cursor, nationalities = cursor2)

@app.route('/referees/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def referees_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_age = request.form['age']
    new_nationality = request.form['nationality']
    query = """UPDATE REFEREES SET RefereeName = '%s', RefereeAge = %d, RefereeNationality = %d WHERE ID = %d""" % (new_name, int(new_age), int(new_nationality), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('referees_page'))

@app.route('/referees/SEARCH/', methods=['GET', 'POST'])
def referees_page_search():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    connection.commit()
    return render_template('referees_search.html', referees = cursor)

@app.route('/referees/SEARCH/SEARCHAPPLY', methods=['GET', 'POST'])
def referees_page_searchapply():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    in_name = request.form['name']
    query = """SELECT * FROM REFEREES WHERE RefereeName = '%s'""" % (in_name)
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('referees_foundpage'))

@app.route('/referees/SEARCH/<RNAME>/FOUND', methods=['POST'])
def referees_found_page(RNAME):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    query = """SELECT RNAME FROM REFEREES WHERE RefereeName = '%s'"""
    cursor.execute(query)
    return render_template('referee_foundsearch.html', referees = cursor)
