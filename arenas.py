import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/arenas', methods=['GET', 'POST'])
def arenas_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM ARENAS"
        cursor.execute(query)
        return render_template('arenas.html', arenas = cursor)
    else:
        name_in = request.form['name']
        builtDate_in = request.form['built-date']
        city_in = request.form['city']
        capacity_in = request.form['capacity']
        query = """INSERT INTO ARENAS (ArenaName, ArenaBuiltDate, ArenaCity, ArenaCapacity)
        VALUES ('"""+name_in+"', '"+builtDate_in+"', '"+city_in+"', '"+capacity_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('arenas_page'))

@app.route('/arenas/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def arenas_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM ARENAS WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('arenas_page'))

@app.route('/arenas/initdb')
def initialize_database_arenas():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    query = """DROP TABLE IF EXISTS ARENAS"""
    cursor.execute(query)
    query = """CREATE TABLE ARENAS (ID SERIAL PRIMARY KEY, ArenaName VARCHAR NOT NULL, ArenaBuiltDate INTEGER, ArenaCity VARCHAR NOT NULL, ArenaCapacity INTEGER)"""
    cursor.execute(query)
    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Burhan Felek',2010,'Istanbul',7500)"""
    cursor.execute(query)
    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Memorial Coliseum',1976,'Kentucky',23000)"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('arenas_page'))