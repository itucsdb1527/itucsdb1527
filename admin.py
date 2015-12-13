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
    ,'galatasaray.jpg')"""
    cursor.execute(query)
    query = """INSERT INTO News (News_Title,News_Details,News_Picture) VALUES ('Fenerbahce',
    '
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempor ex eu condimentum varius. Nunc semper ex ut dapibus molestie. Integer risus ligula, laoreet id tortor sed, accumsan euismod justo. Nam a ipsum ut ex finibus fermentum quis vitae nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus non nulla id est elementum mattis. Donec in quam ex. Mauris sit amet dolor nec mi consectetur vestibulum. Ut dictum odio et sem faucibus tincidunt. Vivamus ac congue erat, nec euismod lectus.

        Ut eleifend nisl aliquet gravida finibus. Nulla porttitor ornare augue sodales vulputate. Cras condimentum luctus ante, at mattis augue tempor in. Quisque pulvinar dolor eros, nec bibendum velit imperdiet vel. Quisque dignissim odio velit, vitae finibus nunc facilisis eu. Maecenas at massa consequat magna suscipit hendrerit. In ultrices aliquam lorem, dictum aliquet est posuere ac. Phasellus nec luctus dolor, eu consequat nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In quis elementum ligula. Suspendisse potenti. Vivamus nulla neque, commodo et odio at, feugiat rhoncus velit. Ut id tincidunt massa.

        Pellentesque tincidunt tellus id turpis pharetra, quis commodo elit egestas. Aliquam aliquam semper accumsan. Vestibulum diam dui, ullamcorper a tempor et, dictum non ante. Duis sollicitudin mattis mauris, quis rutrum sapien tristique ut. Etiam facilisis urna quam, quis venenatis diam posuere interdum. Vivamus ligula risus, vulputate non odio nec, fringilla viverra libero. Aenean et metus lectus. Sed malesuada fringilla ultricies. Duis ultrices facilisis lectus a dapibus.

        Vivamus blandit sed elit tincidunt dictum. Phasellus lobortis, diam vitae feugiat placerat, tortor nibh cursus est, vitae interdum enim mauris non leo. Nullam tristique nisl libero, ut tincidunt eros sodales vel. Nulla molestie ex quis rhoncus posuere. Donec sem dolor, bibendum et tincidunt vitae, imperdiet sed urna. Praesent tellus dui, pulvinar et lobortis sit amet, volutpat in dui. Etiam varius eu diam sit amet tincidunt. Integer consectetur urna quam, vitae lobortis libero mattis sollicitudin. Fusce non pharetra justo. Nullam ultrices placerat magna, id tristique dui pellentesque eget. Nulla venenatis at neque sit amet dapibus. Morbi lacus magna, scelerisque at vestibulum ut, consequat quis orci. Vestibulum sed augue vulputate massa faucibus facilisis in sed libero. Curabitur tincidunt felis at maximus consectetur. Phasellus non enim iaculis purus vestibulum dapibus sit amet at sem. Etiam blandit metus a quam posuere, quis consectetur ante vulputate.

        Vestibulum sed maximus est. Donec vitae metus porttitor, feugiat purus nec, euismod leo. Vivamus lacus lectus, sollicitudin ac nisl vitae, placerat lobortis ipsum. In eu rutrum ante. Nunc sed convallis magna. Vivamus orci augue, dapibus id ante in, dictum luctus sapien. Integer posuere congue scelerisque.
    '
    ,'fenerbahce.jpg')"""
    cursor.execute(query)
    query = """INSERT INTO News (News_Title,News_Details,News_Picture) VALUES ('Besiktas',
    '
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempor ex eu condimentum varius. Nunc semper ex ut dapibus molestie. Integer risus ligula, laoreet id tortor sed, accumsan euismod justo. Nam a ipsum ut ex finibus fermentum quis vitae nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus non nulla id est elementum mattis. Donec in quam ex. Mauris sit amet dolor nec mi consectetur vestibulum. Ut dictum odio et sem faucibus tincidunt. Vivamus ac congue erat, nec euismod lectus.

        Ut eleifend nisl aliquet gravida finibus. Nulla porttitor ornare augue sodales vulputate. Cras condimentum luctus ante, at mattis augue tempor in. Quisque pulvinar dolor eros, nec bibendum velit imperdiet vel. Quisque dignissim odio velit, vitae finibus nunc facilisis eu. Maecenas at massa consequat magna suscipit hendrerit. In ultrices aliquam lorem, dictum aliquet est posuere ac. Phasellus nec luctus dolor, eu consequat nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In quis elementum ligula. Suspendisse potenti. Vivamus nulla neque, commodo et odio at, feugiat rhoncus velit. Ut id tincidunt massa.

        Pellentesque tincidunt tellus id turpis pharetra, quis commodo elit egestas. Aliquam aliquam semper accumsan. Vestibulum diam dui, ullamcorper a tempor et, dictum non ante. Duis sollicitudin mattis mauris, quis rutrum sapien tristique ut. Etiam facilisis urna quam, quis venenatis diam posuere interdum. Vivamus ligula risus, vulputate non odio nec, fringilla viverra libero. Aenean et metus lectus. Sed malesuada fringilla ultricies. Duis ultrices facilisis lectus a dapibus.

        Vivamus blandit sed elit tincidunt dictum. Phasellus lobortis, diam vitae feugiat placerat, tortor nibh cursus est, vitae interdum enim mauris non leo. Nullam tristique nisl libero, ut tincidunt eros sodales vel. Nulla molestie ex quis rhoncus posuere. Donec sem dolor, bibendum et tincidunt vitae, imperdiet sed urna. Praesent tellus dui, pulvinar et lobortis sit amet, volutpat in dui. Etiam varius eu diam sit amet tincidunt. Integer consectetur urna quam, vitae lobortis libero mattis sollicitudin. Fusce non pharetra justo. Nullam ultrices placerat magna, id tristique dui pellentesque eget. Nulla venenatis at neque sit amet dapibus. Morbi lacus magna, scelerisque at vestibulum ut, consequat quis orci. Vestibulum sed augue vulputate massa faucibus facilisis in sed libero. Curabitur tincidunt felis at maximus consectetur. Phasellus non enim iaculis purus vestibulum dapibus sit amet at sem. Etiam blandit metus a quam posuere, quis consectetur ante vulputate.

        Vestibulum sed maximus est. Donec vitae metus porttitor, feugiat purus nec, euismod leo. Vivamus lacus lectus, sollicitudin ac nisl vitae, placerat lobortis ipsum. In eu rutrum ante. Nunc sed convallis magna. Vivamus orci augue, dapibus id ante in, dictum luctus sapien. Integer posuere congue scelerisque.
    '
    ,'besiktas.jpg')"""
    cursor.execute(query)

    connection.commit()
    return redirect(url_for('admin_home_page'))


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
