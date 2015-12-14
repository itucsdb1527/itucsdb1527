import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app


@app.route('/initdb')
def initialize_database():
    connection = dbapi2.connect(app.config['dsn'])
    cursor =connection.cursor()

# MAIN DB #
    query = """DROP TABLE IF EXISTS COUNTER"""
    cursor.execute(query)

# LEAGUES - CEMAL #
    query = """DROP TABLE IF EXISTS LEAGUES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE LEAGUES (
                    ID SERIAL PRIMARY KEY,
                    League_Name VARCHAR NOT NULL,
                    Country_ID INTEGER NOT NULL,
                    FOREIGN KEY (Country_ID) REFERENCES COUNTRIES(ID) ON DELETE CASCADE ON UPDATE CASCADE
                    )"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,Country_ID) VALUES ('Aroma Erkekler Voleybol Ligi',1)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,Country_ID) VALUES ('Premier Lig',2)"""
    cursor.execute(query)

# SEASONS - CEMAL #
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

# NEWS - CEMAL #
    query = """DROP TABLE IF EXISTS NEWS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE NEWS (
                    ID SERIAL PRIMARY KEY,
                    News_Title VARCHAR NOT NULL,
                    News_Details TEXT,
                    News_Picture VARCHAR NOT NULL
                    )"""
    cursor.execute(query)
    query = """INSERT INTO News (News_Title,News_Details,News_Picture) VALUES ('Galatasaray',
    '
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempor ex eu condimentum varius. Nunc semper ex ut dapibus molestie. Integer risus ligula, laoreet id tortor sed, accumsan euismod justo. Nam a ipsum ut ex finibus fermentum quis vitae nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus non nulla id est elementum mattis. Donec in quam ex. Mauris sit amet dolor nec mi consectetur vestibulum. Ut dictum odio et sem faucibus tincidunt. Vivamus ac congue erat, nec euismod lectus.

        Ut eleifend nisl aliquet gravida finibus. Nulla porttitor ornare augue sodales vulputate. Cras condimentum luctus ante, at mattis augue tempor in. Quisque pulvinar dolor eros, nec bibendum velit imperdiet vel. Quisque dignissim odio velit, vitae finibus nunc facilisis eu. Maecenas at massa consequat magna suscipit hendrerit. In ultrices aliquam lorem, dictum aliquet est posuere ac. Phasellus nec luctus dolor, eu consequat nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In quis elementum ligula. Suspendisse potenti. Vivamus nulla neque, commodo et odio at, feugiat rhoncus velit. Ut id tincidunt massa.

        Pellentesque tincidunt tellus id turpis pharetra, quis commodo elit egestas. Aliquam aliquam semper accumsan. Vestibulum diam dui, ullamcorper a tempor et, dictum non ante. Duis sollicitudin mattis mauris, quis rutrum sapien tristique ut. Etiam facilisis urna quam, quis venenatis diam posuere interdum. Vivamus ligula risus, vulputate non odio nec, fringilla viverra libero. Aenean et metus lectus. Sed malesuada fringilla ultricies. Duis ultrices facilisis lectus a dapibus.

        Vivamus blandit sed elit tincidunt dictum. Phasellus lobortis, diam vitae feugiat placerat, tortor nibh cursus est, vitae interdum enim mauris non leo. Nullam tristique nisl libero, ut tincidunt eros sodales vel. Nulla molestie ex quis rhoncus posuere. Donec sem dolor, bibendum et tincidunt vitae, imperdiet sed urna. Praesent tellus dui, pulvinar et lobortis sit amet, volutpat in dui. Etiam varius eu diam sit amet tincidunt. Integer consectetur urna quam, vitae lobortis libero mattis sollicitudin. Fusce non pharetra justo. Nullam ultrices placerat magna, id tristique dui pellentesque eget. Nulla venenatis at neque sit amet dapibus. Morbi lacus magna, scelerisque at vestibulum ut, consequat quis orci. Vestibulum sed augue vulputate massa faucibus facilisis in sed libero. Curabitur tincidunt felis at maximus consectetur. Phasellus non enim iaculis purus vestibulum dapibus sit amet at sem. Etiam blandit metus a quam posuere, quis consectetur ante vulputate.

        Vestibulum sed maximus est. Donec vitae metus porttitor, feugiat purus nec, euismod leo. Vivamus lacus lectus, sollicitudin ac nisl vitae, placerat lobortis ipsum. In eu rutrum ante. Nunc sed convallis magna. Vivamus orci augue, dapibus id ante in, dictum luctus sapien. Integer posuere congue scelerisque.
    '
    ,'galatasaray.png')"""
    cursor.execute(query)
    query = """INSERT INTO News (News_Title,News_Details,News_Picture) VALUES ('Fenerbahce',
    '
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempor ex eu condimentum varius. Nunc semper ex ut dapibus molestie. Integer risus ligula, laoreet id tortor sed, accumsan euismod justo. Nam a ipsum ut ex finibus fermentum quis vitae nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus non nulla id est elementum mattis. Donec in quam ex. Mauris sit amet dolor nec mi consectetur vestibulum. Ut dictum odio et sem faucibus tincidunt. Vivamus ac congue erat, nec euismod lectus.

        Ut eleifend nisl aliquet gravida finibus. Nulla porttitor ornare augue sodales vulputate. Cras condimentum luctus ante, at mattis augue tempor in. Quisque pulvinar dolor eros, nec bibendum velit imperdiet vel. Quisque dignissim odio velit, vitae finibus nunc facilisis eu. Maecenas at massa consequat magna suscipit hendrerit. In ultrices aliquam lorem, dictum aliquet est posuere ac. Phasellus nec luctus dolor, eu consequat nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In quis elementum ligula. Suspendisse potenti. Vivamus nulla neque, commodo et odio at, feugiat rhoncus velit. Ut id tincidunt massa.

        Pellentesque tincidunt tellus id turpis pharetra, quis commodo elit egestas. Aliquam aliquam semper accumsan. Vestibulum diam dui, ullamcorper a tempor et, dictum non ante. Duis sollicitudin mattis mauris, quis rutrum sapien tristique ut. Etiam facilisis urna quam, quis venenatis diam posuere interdum. Vivamus ligula risus, vulputate non odio nec, fringilla viverra libero. Aenean et metus lectus. Sed malesuada fringilla ultricies. Duis ultrices facilisis lectus a dapibus.

        Vivamus blandit sed elit tincidunt dictum. Phasellus lobortis, diam vitae feugiat placerat, tortor nibh cursus est, vitae interdum enim mauris non leo. Nullam tristique nisl libero, ut tincidunt eros sodales vel. Nulla molestie ex quis rhoncus posuere. Donec sem dolor, bibendum et tincidunt vitae, imperdiet sed urna. Praesent tellus dui, pulvinar et lobortis sit amet, volutpat in dui. Etiam varius eu diam sit amet tincidunt. Integer consectetur urna quam, vitae lobortis libero mattis sollicitudin. Fusce non pharetra justo. Nullam ultrices placerat magna, id tristique dui pellentesque eget. Nulla venenatis at neque sit amet dapibus. Morbi lacus magna, scelerisque at vestibulum ut, consequat quis orci. Vestibulum sed augue vulputate massa faucibus facilisis in sed libero. Curabitur tincidunt felis at maximus consectetur. Phasellus non enim iaculis purus vestibulum dapibus sit amet at sem. Etiam blandit metus a quam posuere, quis consectetur ante vulputate.

        Vestibulum sed maximus est. Donec vitae metus porttitor, feugiat purus nec, euismod leo. Vivamus lacus lectus, sollicitudin ac nisl vitae, placerat lobortis ipsum. In eu rutrum ante. Nunc sed convallis magna. Vivamus orci augue, dapibus id ante in, dictum luctus sapien. Integer posuere congue scelerisque.
    '
    ,'fenerbahce.png')"""
    cursor.execute(query)
    query = """INSERT INTO News (News_Title,News_Details,News_Picture) VALUES ('Besiktas',
    '
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempor ex eu condimentum varius. Nunc semper ex ut dapibus molestie. Integer risus ligula, laoreet id tortor sed, accumsan euismod justo. Nam a ipsum ut ex finibus fermentum quis vitae nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus non nulla id est elementum mattis. Donec in quam ex. Mauris sit amet dolor nec mi consectetur vestibulum. Ut dictum odio et sem faucibus tincidunt. Vivamus ac congue erat, nec euismod lectus.

        Ut eleifend nisl aliquet gravida finibus. Nulla porttitor ornare augue sodales vulputate. Cras condimentum luctus ante, at mattis augue tempor in. Quisque pulvinar dolor eros, nec bibendum velit imperdiet vel. Quisque dignissim odio velit, vitae finibus nunc facilisis eu. Maecenas at massa consequat magna suscipit hendrerit. In ultrices aliquam lorem, dictum aliquet est posuere ac. Phasellus nec luctus dolor, eu consequat nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In quis elementum ligula. Suspendisse potenti. Vivamus nulla neque, commodo et odio at, feugiat rhoncus velit. Ut id tincidunt massa.

        Pellentesque tincidunt tellus id turpis pharetra, quis commodo elit egestas. Aliquam aliquam semper accumsan. Vestibulum diam dui, ullamcorper a tempor et, dictum non ante. Duis sollicitudin mattis mauris, quis rutrum sapien tristique ut. Etiam facilisis urna quam, quis venenatis diam posuere interdum. Vivamus ligula risus, vulputate non odio nec, fringilla viverra libero. Aenean et metus lectus. Sed malesuada fringilla ultricies. Duis ultrices facilisis lectus a dapibus.

        Vivamus blandit sed elit tincidunt dictum. Phasellus lobortis, diam vitae feugiat placerat, tortor nibh cursus est, vitae interdum enim mauris non leo. Nullam tristique nisl libero, ut tincidunt eros sodales vel. Nulla molestie ex quis rhoncus posuere. Donec sem dolor, bibendum et tincidunt vitae, imperdiet sed urna. Praesent tellus dui, pulvinar et lobortis sit amet, volutpat in dui. Etiam varius eu diam sit amet tincidunt. Integer consectetur urna quam, vitae lobortis libero mattis sollicitudin. Fusce non pharetra justo. Nullam ultrices placerat magna, id tristique dui pellentesque eget. Nulla venenatis at neque sit amet dapibus. Morbi lacus magna, scelerisque at vestibulum ut, consequat quis orci. Vestibulum sed augue vulputate massa faucibus facilisis in sed libero. Curabitur tincidunt felis at maximus consectetur. Phasellus non enim iaculis purus vestibulum dapibus sit amet at sem. Etiam blandit metus a quam posuere, quis consectetur ante vulputate.

        Vestibulum sed maximus est. Donec vitae metus porttitor, feugiat purus nec, euismod leo. Vivamus lacus lectus, sollicitudin ac nisl vitae, placerat lobortis ipsum. In eu rutrum ante. Nunc sed convallis magna. Vivamus orci augue, dapibus id ante in, dictum luctus sapien. Integer posuere congue scelerisque.
    '
    ,'besiktas.png')"""
    cursor.execute(query)

# TEAMS - MERIC #
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


# SEASON TEAM - MERIC #
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
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 13)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 14)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 15)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 16)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 17)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 18)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 19)"""
    cursor.execute(query)
    query = """INSERT INTO SEASON_TEAM (Season_ID, Team_ID) VALUES (3, 20)"""
    cursor.execute(query)

# ADMIN - MERIC #
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

# PLAYERS - MERAL #
    query = """DROP TABLE IF EXISTS PLAYERS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE PLAYERS (
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR NOT NULL,
                    NATIONALITY_ID INTEGER NOT NULL,
                    AGE INTEGER NOT NULL,
                    NUMBER INTEGER NOT NULL,
                    POSITION VARCHAR NOT NULL,
                    FOREIGN KEY (NATIONALITY_ID) REFERENCES NATIONALITIES(ID) ON DELETE CASCADE ON UPDATE CASCADE
                    )"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('MERAL',1, 20, 8,'Right Side Hitter')"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('CEMAL',1, 24, 15,'Opposite')"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('SEYMA',1, 21, 9,'Outside Hitter')"""
    cursor.execute(query)


# COUNTRIES - MERAL #
    query = """DROP TABLE IF EXISTS COUNTRIES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE COUNTRIES (
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR NOT NULL
                    )"""
    cursor.execute(query)

    query = """INSERT INTO COUNTRIES (NAME) VALUES ('TURKEY')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('ENGLAND')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('USA')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('GERMANY')"""
    cursor.execute(query)
    query = """INSERT INTO COUNTRIES (NAME) VALUES ('FRANCE')"""
    cursor.execute(query)

# TEAMPLAYERS - MERAL #
    query = """DROP TABLE IF EXISTS TEAMPLAYERS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE TEAMPLAYERS (
                    PLAYERID INTEGER NOT NULL,
                    TEAMID INTEGER NOT NULL,
                    SEASONID INTEGER NOT NULL,
                    FOREIGN KEY (PLAYERID) REFERENCES PLAYERS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (TEAMID) REFERENCES TEAMS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (SEASONID) REFERENCES SEASONS(ID) ON DELETE CASCADE ON UPDATE CASCADE,
                    PRIMARY KEY (PLAYERID, TEAMID, SEASONID)
                    )"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('admin_home_page'))





################################### CEMAL #######################################################

# LEAGUE - CEMAL #

@app.route('/ADMIN/leagues', methods=['GET', 'POST'])
def admin_leagues_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT LEAGUES.ID, COUNTRIES.ID, League_Name, COUNTRIES.Name FROM LEAGUES, COUNTRIES WHERE Country_ID = COUNTRIES.ID ORDER BY Country_ID, League_Name"
        cursor.execute(query)

        cursor2 = connection.cursor()
        query = "SELECT ID, Name FROM Countries ORDER BY Name"
        cursor2.execute(query)
        return render_template('admin/leagues.html', leagues = cursor, countries = cursor2)
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
    cursor2 = connection.cursor()
    query = "SELECT ID, Name FROM Countries ORDER BY Name"
    cursor2.execute(query)
    connection.commit()
    return render_template('admin/leagues_edit.html', leagues = cursor, countries = cursor2)


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



# SEASON - CEMAL #

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



# NEWS - CEMAL #

@app.route('/ADMIN/news')
def admin_news_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()
    query = "SELECT ID, News_Title FROM NEWS ORDER BY ID DESC"
    cursor.execute(query)
    return render_template('admin/news.html', news=cursor)


@app.route('/ADMIN/news/UPDATE/<int:NEWSID>/', methods=['GET', 'POST'])
def admin_news_edit_page(NEWSID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()
    query = "SELECT ID,News_Title, News_Details, News_Picture FROM NEWS WHERE ID = %d" % int(NEWSID)
    cursor.execute(query)
    return render_template('admin/news_detail.html', news = cursor)


@app.route('/ADMIN/news/UPDATE/<int:NEWSID>/APPLY', methods=['GET', 'POST'])
def admin_news_edit_apply(NEWSID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    news_title = request.form['title']
    news_details = request.form['detail']
    news_picture = request.form['picture']
    news_ID = request.form['News_ID']
    query = """UPDATE NEWS SET News_Title = '%s', News_Details = '%s' , News_Picture = '%s' WHERE ID = %d""" % (news_title,news_details,news_picture, int(news_ID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_news_page'))









############################################# MERIC #########################################

# TEAMS - MERIC #

@app.route('/ADMIN/teams', methods=['GET', 'POST'])
def admin_teams_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT TEAMS.ID, TEAMS.Team_Name, LEAGUES.League_Name FROM TEAMS INNER JOIN LEAGUES ON TEAMS.Leagues_ID = LEAGUES.ID ORDER BY ID"
        cursor.execute(query)

        cursor2 = connection.cursor()
        query = "SELECT ID, League_Name FROM LEAGUES"
        cursor2.execute(query)

        return render_template('admin/teams.html', teams = cursor, leagues = cursor2)
    else:

        name = request.form['name']
        leagues_id = request.form['leagues_id']
        query = """INSERT INTO TEAMS (Team_Name, Leagues_ID)
        VALUES ('"""+name+"','"+leagues_id+"')"
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

    cursor2 = connection.cursor()
    query = "SELECT ID, League_Name FROM LEAGUES"
    cursor2.execute(query)

    cursor.execute("""SELECT ID, Team_Name FROM TEAMS WHERE ID = %s""", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/teams_edit.html', teams = cursor, leagues = cursor2)


@app.route('/ADMIN/teams/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_teams_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_leagues_id = request.form['leagues_id']
    query = """UPDATE TEAMS SET Team_Name = '%s', Leagues_ID = '%d' WHERE ID = %d""" % (new_name, int(new_leagues_id), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_teams_page'))



# SEASON TEAM - MERIC #

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



# ADMIN - MERIC #

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


################################### MERAL ################################

# PLAYERS - MERAL #

@app.route('/ADMIN/players', methods=['GET', 'POST'])
def admin_players_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT PLAYERS.ID, NAME, NATIONALITY, AGE, NUMBER, POSITION FROM PLAYERS, NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID"
        cursor.execute(query)
        cursor2 = connection.cursor()
        query = "SELECT * FROM NATIONALITIES"
        cursor2.execute(query)
        return render_template('admin/players.html', players = cursor, nationalities = cursor2)
    else:
        name_in = request.form['name']
        nationality_in = request.form['nationalityID']
        age_in = request.form['age']
        number_in = request.form['number']
        position_in = request.form['position']
        query = """INSERT INTO PLAYERS (NAME, NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES ('"""+name_in+"', '"+nationality_in+"', '"+age_in+"', '"+number_in+"', '"+position_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_players_page'))


@app.route('/ADMIN/players/DELETE/<int:DELETEID>', methods=['GET','POST'])
def admin_players_page_delete(DELETEID):
    connection=dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM PLAYERS WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_players_page'))


@app.route('/ADMIN/players/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_players_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM PLAYERS WHERE ID = %s", (int(UPDATEID),))
    cursor2 = connection.cursor()
    query = "SELECT * FROM NATIONALITIES"
    cursor2.execute(query)
    connection.commit()
    return render_template('admin/players_edit.html', players = cursor, nationalities = cursor2)


@app.route('/ADMIN/players/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_players_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    new_nationality = request.form['nationalityID']
    new_age = request.form['age']
    new_number = request.form['number']
    new_position = request.form['position']
    query = "UPDATE PLAYERS SET NAME = '%s', NATIONALITY_ID = %d, AGE = %d, NUMBER = %d, POSITION = '%s'  WHERE ID = %d" % (new_name,int(new_nationality),int(new_age), int(new_number), new_position, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_players_page'))



# COUNTRIES - MERAL #

@app.route('/ADMIN/countries', methods=['GET', 'POST'])
def admin_countries_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT * FROM COUNTRIES"
        cursor.execute(query)
        return render_template('admin/countries.html', countries = cursor)
    else:
        name_in = request.form['name']
        query = """INSERT INTO COUNTRIES (name) VALUES ('"""+name_in+"')"
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_countries_page'))


@app.route('/ADMIN/countries/DELETE/<int:DELETEID>', methods=['GET','POST'])
def admin_countries_page_delete(DELETEID):
    connection=dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM COUNTRIES WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_countries_page'))


@app.route('/ADMIN/countries/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_countries_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM COUNTRIES WHERE ID = %s", (int(UPDATEID),))
    connection.commit()
    return render_template('admin/countries_edit.html', countries = cursor)


@app.route('/ADMIN/countries/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_countries_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_name = request.form['name']
    query = """UPDATE COUNTRIES SET NAME = '%s' WHERE ID = %d""" % (new_name, int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_countries_page'))



# TEAMPLAYERS - MERAL #

@app.route('/ADMIN/teamplayers', methods=['GET', 'POST'])
def admin_team_players_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT PLAYERS.ID, PLAYERS.NAME, SEASONS.ID, SEASONS.Season_Name, TEAMS.ID, TEAMS.Team_Name FROM TEAMPLAYERS, PLAYERS, SEASONS, TEAMS WHERE PLAYERID = PLAYERS.ID AND TEAMID = TEAMS.ID AND SEASONID = SEASONS.ID"
        cursor.execute(query)

        cursor2 = connection.cursor()
        query = "SELECT ID, NAME FROM PLAYERS"
        cursor2.execute(query)

        cursor3 = connection.cursor()
        query = "SELECT ID, Season_Name FROM SEASONS"
        cursor3.execute(query)


        cursor4 = connection.cursor()
        query = "SELECT ID, Team_Name FROM TEAMS"
        cursor4.execute(query)

        return render_template('/ADMIN/teamplayers.html', teamplayers = cursor, players = cursor2, seasons = cursor3, teams = cursor4)
    else:
        playerid_in = request.form['playerid']
        seasonid_in = request.form['seasonid']
        teamid_in = request.form['teamid']
        query = """INSERT INTO TEAMPLAYERS (PLAYERID, SEASONID, TEAMID) VALUES (%d,%d,%d)""" % (int(playerid_in), int(seasonid_in), int(teamid_in))
        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_team_players_page'))


@app.route('/ADMIN/teamplayers/DELETE/<int:DELETEID>', methods=['GET','POST'])
def admin_team_players_page_delete(DELETEID):
    connection=dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM TEAMPLAYERS WHERE PLAYERID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_team_players_page'))


@app.route('/ADMIN/teamplayers/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
def admin_team_players_page_update(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])

    cursor = connection.cursor()
    query = "SELECT playerid, seasonid, teamid FROM TEAMPLAYERS WHERE PLAYERID = %d" % int(UPDATEID)
    cursor.execute(query)

    cursor2 = connection.cursor()
    query = "SELECT ID, NAME FROM PLAYERS"
    cursor2.execute(query)

    cursor3 = connection.cursor()
    query = "SELECT ID, Season_Name FROM SEASONS"
    cursor3.execute(query)

    cursor4 = connection.cursor()
    query = "SELECT ID, Team_Name FROM TEAMS"
    cursor4.execute(query)

    connection.commit()
    return render_template('admin/teamplayers_edit.html', teamplayers = cursor, players = cursor2, seasons = cursor3, teams = cursor4)


@app.route('/ADMIN/teamplayers/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
def admin_team_players_page_apply(UPDATEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    new_playerid = request.form['playerid']
    new_seasonid = request.form['seasonid']
    new_teamid = request.form['teamid']
    query = "UPDATE TEAMPLAYERS SET PLAYERID = %d, SEASONID = %d, TEAMID = %d WHERE PLAYERID = %d" % (int(new_playerid), int(new_seasonid), int(new_teamid), int(UPDATEID))
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_team_players_page'))

