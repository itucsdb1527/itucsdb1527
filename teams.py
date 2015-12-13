import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

@app.route('/teams/initdb')
def admin_initialize_database_teams():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

    #Teams Table
    query = """DROP TABLE IF EXISTS TEAMS CASCADE"""
    cursor.execute(query)

    query = """CREATE TABLE TEAMS(
    ID SERIAL PRIMARY KEY,
    Team_Name VARCHAR NOT NULL,
    Leagues_ID INTEGER,
    FOREIGN KEY (Leagues_ID) REFERENCES LEAGUES(ID) ON DELETE CASCADE ON UPDATE CASCADE
    )"""
    cursor.execute(query)

    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Galatasaray',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Besiktas',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Fenerbahce',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Ziraat Bankasi',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Halkbank',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Istanbul B.S.B.',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Sahinbey Bld.',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Maliye Milli Piyango',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Tokat Bld. Plevne',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Inegol Bld.',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Arkas Spor',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Bornova Anadolu Lisesi',1)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('IBB Polonia London',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Team Northumbria',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('London Docklands',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Wessex M1',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Sheffield Hallam',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('London Lynx 1',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Leeds VC',2)"""
    cursor.execute(query)
    query = """INSERT INTO TEAMS (Team_Name, Leagues_ID) VALUES ('Malory Eagles (London)',2)"""
    cursor.execute(query)


    #Season Team Table
    query = """DROP TABLE IF EXISTS SEASON_TEAM CASCADE"""
    cursor.execute(query)

    query = """CREATE TABLE SEASON_TEAM(
    ID SERIAL PRIMARY KEY,
    Season_ID INTEGER,
    Team_ID INTEGER,
    FOREIGN KEY (Season_ID) REFERENCES SEASONS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Team_ID) REFERENCES TEAMS(ID) ON DELETE CASCADE ON UPDATE CASCADE
    )"""
    cursor.execute(query)

    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 1)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 2)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 3)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 4)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 5)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 6)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 7)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 8)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 9)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 10)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 11)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 12)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 13)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 14)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 15)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 16)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 17)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 18)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 19)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (1, 20)"""
    cursor.execute(query)

    #Admin Table
    query = """DROP TABLE IF EXISTS SITE CASCADE"""
    cursor.execute(query)

    query = """CREATE TABLE SITE(
    ID SERIAL,
    Admin_Name VARCHAR NOT NULL,
    Admin_Password VARCHAR NOT NULL,
    Site_Name VARCHAR NOT NULL,
    Slogan VARCHAR NOT NULL,
    PRIMARY KEY(ID)
    )"""
    cursor.execute(query)

    query = """INSERT INTO SITE (Admin_Name, Admin_Password, Site_Name, Slogan) VALUES ('Meric','lolololo','itucsdb1527','Cimbombom')"""
    cursor.execute(query)
    query = """INSERT INTO SITE (Admin_Name, Admin_Password, Site_Name, Slogan) VALUES ('Volleybase','uyar','itucsdb1527','Cimbombom')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('admin_teams_page'))


@app.route('/teams', methods=['GET', 'POST'])
def teams_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT TEAMS.ID, TEAMS.Team_Name, LEAGUES.League_Name FROM TEAMS INNER JOIN LEAGUES ON TEAMS.Leagues_ID = LEAGUES.ID ORDER BY ID"
        cursor.execute(query)
        return render_template('teams.html', teams = cursor)
    else:
        search = request.form['search']
        query = "SELECT ID, Team_Name FROM TEAMS WHERE Team_Name LIKE '%" + search +"%'"
        cursor.execute(query)
        connection.commit()
        return render_template('teams.html', teams = cursor)



@app.route('/teams/season_team/<int:TEAMID>', methods=['GET', 'POST'])
def teams_season_team_page(TEAMID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT Season_Name, Team_Name FROM SEASON_TEAM INNER JOIN TEAMS ON SEASON_TEAM.Team_ID = TEAMS.ID INNER JOIN SEASONS ON SEASON_TEAM.Season_ID = SEASONS.ID WHERE Team_ID = %d" % int(TEAMID)
        cursor.execute(query)

        return render_template('season_team.html', season_team = cursor)
    else:
        search = request.form['search']
        query = "SELECT Season_Name, Team_Name FROM SEASON_TEAM INNER JOIN TEAMS ON SEASON_TEAM.Team_ID = TEAMS.ID INNER JOIN SEASONS ON SEASON_TEAM.Season_ID = SEASONS.ID WHERE Team_Name LIKE'%" + search + "%'"
        cursor.execute(query)
        connection.commit()
        return render_template('season_team.html', season_team = cursor)



@app.route('/ADMIN/teams', methods=['GET', 'POST'])
def admin_teams_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT TEAMS.ID, TEAMS.Team_Name, LEAGUES.League_Name FROM TEAMS INNER JOIN LEAGUES ON TEAMS.Leagues_ID = LEAGUES.ID ORDER BY ID"
        cursor.execute(query)
        return render_template('admin/teams.html', teams = cursor)
    else:

        name = request.form['name']
        query = """INSERT INTO TEAMS (Team_Name)
        VALUES ('"""+name+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_teams_page'))




@app.route('/ADMIN/teams/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def admin_teams_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM TEAMS WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('admin_teams_page'))


@app.route('/ADMIN/teams/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_teams_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Team_Name FROM TEAMS WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/teams_edit.html', teams = cursor)

@app.route('/ADMIN/teams/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_teams_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    query = """UPDATE TEAMS SET Team_Name = '%s' WHERE ID = %d""" % (new_name, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_teams_page'))


@app.route('/ADMIN/teams/season_team', methods=['GET', 'POST'])
def admin_season_team_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT SEASON_TEAM.ID AS ID , Season_Name, Team_Name FROM SEASON_TEAM INNER JOIN TEAMS ON SEASON_TEAM.Team_ID = TEAMS.ID INNER JOIN SEASONS ON SEASON_TEAM.Season_ID = SEASONS.ID ORDER BY Team_ID"
        cursor.execute(query)

        cursor3 = connection.cursor()
        query = "SELECT ID, Season_Name FROM SEASONS"
        cursor3.execute(query)

        cursor2 = connection.cursor()
        query = "SELECT ID, Team_Name FROM TEAMS ORDER BY ID"
        cursor2.execute(query)
        return render_template('admin/season_team.html', season_team = cursor,seasons = cursor3, teams = cursor2)
    else:
        Season_ID = request.form['Season_ID']
        Team_ID = request.form['Team_ID']
        query = """INSERT INTO SEASON_TEAM (Season_ID,Team_ID) VALUES ('"""+Season_ID+"','"+Team_ID+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_season_team_page'))

@app.route('/ADMIN/season_team/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def admin_season_team_page_delete(DELETEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM SEASON_TEAM WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_season_team_page'))

@app.route('/ADMIN/season_team/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_season_team_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Season_ID, Team_ID FROM SEASON_TEAM WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()

    cursor3 = connection.cursor()
    cursor3.execute("SELECT ID, Season_Name FROM SEASONS")

    cursor2 = connection.cursor()
    query = "SELECT ID, Team_Name FROM TEAMS ORDER BY ID"
    cursor2.execute(query)

    return render_template('admin/season_team_edit.html', season_team = cursor,seasons = cursor3, teams = cursor2)

@app.route('/ADMIN/season_team/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_season_team_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_season_ID = request.form['Season_ID']
    new_team_ID = request.form['Team_ID']
    query = """UPDATE SEASON_TEAM SET Season_ID = '%d', Team_ID = %d WHERE ID = %d""" % (int(new_season_ID),int(new_team_ID), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_season_team_page'))


@app.route('/ADMIN/admin', methods=['GET', 'POST'])
def admin_admin_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM SITE ORDER BY ID"
        cursor.execute(query)
        return render_template('admin/admin.html', site = cursor)
    else:

        name = request.form['name']
        password = request.form['password']
        site_name = request.form['site_name']
        slogan = request.form['slogan']
        query = """INSERT INTO SITE (Admin_Name, Admin_Password, Site_Name, Slogan)
        VALUES ('"""+name+"','"+password+"','"+site_name+"','"+slogan+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_admin_page'))




@app.route('/ADMIN/admin/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
def admin_admin_page_delete(DELETEID):
        connection = dbapi2.connect(app.config['dsn'])
        cursor = connection.cursor()


        cursor.execute("""DELETE FROM SITE WHERE ID = %s""", (int(DELETEID),))
        connection.commit()
        return redirect(url_for('admin_admin_page'))


@app.route('/ADMIN/admin/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_admin_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("""SELECT ID, Admin_Name, Admin_Password, Site_Name, Slogan FROM SITE WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/admin_edit.html', site = cursor)

@app.route('/ADMIN/admin/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_admin_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_password = request.form['password']
    new_site_name = request.form['site_name']
    new_slogan = request.form['slogan']

    query = """UPDATE SITE SET Admin_Name = '%s', Admin_Password = '%s', Site_Name = '%s', Slogan = '%s' WHERE ID = %d""" % (new_name, new_password, new_site_name, new_slogan, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_admin_page'))
