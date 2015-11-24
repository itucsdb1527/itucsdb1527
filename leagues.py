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
        query = "SELECT COUNTRIES.ID, League_Name, COUNTRIES.Name FROM LEAGUES, COUNTRIES WHERE Country_ID = COUNTRIES.ID ORDER BY Country_ID, League_Name"
        cursor.execute(query)
        return render_template('leagues.html', leagues = cursor)
    else:
        search = request.form['search']
        query = "SELECT ID, League_Name, Country_ID FROM LEAGUES WHERE League_Name LIKE '%" + search +"%'"
        cursor.execute(query)
        connection.commit()
        return render_template('leagues.html', leagues = cursor)

@app.route('/leagues/season/<int:LEAGUEID>', methods=['GET', 'POST'])
def leagues_season_page(LEAGUEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT Season_Name, League_Name FROM SEASONS INNER JOIN LEAGUES ON SEASONS.LEAGUE_ID = LEAGUES.ID WHERE League_ID = %d" % int(LEAGUEID)
        cursor.execute(query)

        return render_template('season.html', seasons = cursor)
    else:
        search = request.form['search']
        query = "SELECT Season_Name, League_Name FROM SEASONS INNER JOIN LEAGUES ON SEASONS.LEAGUE_ID = LEAGUES.ID WHERE Season_Name LIKE '%" + search +"%'" #AND (League_ID = %d)" % LEAGUEID
        cursor.execute(query)
        connection.commit()
        return render_template('season.html', seasons = cursor)

@app.route('/ADMIN/leagues/initdb')
def admin_initialize_database_leagues():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    query = """DROP TABLE IF EXISTS LEAGUES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE LEAGUES (
                    ID SERIAL PRIMARY KEY,
                    League_Name VARCHAR NOT NULL,
                    Country_ID INTEGER NOT NULL,
                    FOREIGN KEY Country_ID REFERENCES COUNTRIES(ID) ON DELETE CASCADE ON UPDATE CASCADE
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

    query = """INSERT INTO SEASONS (Season_Name,League_ID) VALUES ('2016 Ligi',1)"""
    cursor.execute(query)

    query = """INSERT INTO SEASONS (League_ID,Season_Name) VALUES (1,'2018 Ligi')"""
    cursor.execute(query)
    query = """INSERT INTO SEASONS (League_ID,Season_Name) VALUES (2,'2017 Ligi')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('admin_leagues_page'))

# LEAGUE

@app.route('/ADMIN/leagues', methods=['GET', 'POST'])
def admin_leagues_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT ID, League_Name, Country_ID FROM LEAGUES ORDER BY Country_ID, League_Name"
        cursor.execute(query)
        return render_template('admin/leagues.html', leagues = cursor)
    else:
        name = request.form['name']
        country = request.form['country']
        query = """INSERT INTO LEAGUES (League_Name,Country_ID)
        VALUES ('"""+name+"','"+country+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_leagues_page'))

@app.route('/ADMIN/leagues/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def admin_leagues_page_delete(DELETEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM LEAGUES WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_leagues_page'))

@app.route('/ADMIN/leagues/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_leagues_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, League_Name, Country_ID FROM LEAGUES WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/leagues_edit.html', leagues = cursor)

@app.route('/ADMIN/leagues/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_leagues_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_country = request.form['country']
    query = """UPDATE LEAGUES SET League_Name = '%s', Country_ID = %d WHERE ID = %d""" % (new_name,int(new_country), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_leagues_page'))

# SEASON

@app.route('/ADMIN/leagues/season', methods=['GET', 'POST'])
def admin_seasons_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT  SEASONS.ID AS ID, Season_Name, League_Name FROM SEASONS, LEAGUES WHERE SEASONS.LEAGUE_ID = LEAGUES.ID ORDER BY League_Name"
        cursor.execute(query)

        cursor2 = connection.cursor()
        query = "SELECT ID, League_Name FROM LEAGUES ORDER BY League_Name"
        cursor2.execute(query)
        return render_template('admin/season.html', seasons = cursor, leagues = cursor2)
    else:
        name = request.form['name']
        League_ID = request.form['League_ID']
        query = """INSERT INTO SEASONS (Season_Name,League_ID) VALUES ('"""+name+"','"+League_ID+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_seasons_page'))

@app.route('/ADMIN/seasons/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def admin_seasons_page_delete(DELETEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM SEASONS WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_seasons_page'))

@app.route('/ADMIN/seasons/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_seasons_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Season_Name, League_ID FROM SEASONS WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    cursor2 = connection.cursor()
    query = "SELECT ID, League_Name FROM LEAGUES ORDER BY League_Name"
    cursor2.execute(query)
    return render_template('admin/seasons_edit.html', seasons = cursor, leagues = cursor2)

@app.route('/ADMIN/seasons/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_seasons_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_league_ID = request.form['League_ID']
    query = """UPDATE SEASONS SET Season_Name = '%s', League_ID = %d WHERE ID = %d""" % (new_name,int(new_league_ID), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_seasons_page'))
