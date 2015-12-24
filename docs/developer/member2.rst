Parts Implemented by Meriç Turan
================================

General View
------------

|
In this part, there will be source codes and explanations for teams table, season_team table and site table.

Source codes and explanations are divided into "Creating Table", "Inserting Elements", "Listing and Inserting", "Searching", "Deleting" and "Updating" parts.

|

Teams
-----

**Creating Table**

.. code-block:: python

    @app.route('/initdb')
    def initialize_database():
       connection = dbapi2.connect(app.config['dsn'])
       cursor =connection.cursor()

       query = """DROP TABLE IF EXISTS TEAMS CASCADE"""
       cursor.execute(query)

       query = """CREATE TABLE TEAMS(
       ID SERIAL PRIMARY KEY,
       Team_Name VARCHAR NOT NULL,
       Leagues_ID INTEGER,
       FOREIGN KEY (Leagues_ID) REFERENCES LEAGUES(ID) ON DELETE CASCADE ON UPDATE CASCADE
       )"""
       cursor.execute(query)

|
Teams table is created as seen above. It is cascade on both update and delete. It has 3 columns which are ID, Team_Name and Leagues_ID. Leagues_ID is foreign key references to Leagues table's ID.

   ID is auto incremented, integer and primary key.

   Team_Name is varchar and cannot be NULL.

   Leagues_ID is integer and foreign key.
|

**Inserting Elements**

.. code-block:: python

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

|
Datas for teams table are added as seen above.

   ID is not added above because it is auto increment (by using SERIAL).

   Team_Name is added between quotes ('') because it is varchar.

   Leagues_ID is added by writing  an integer. There is no need to use quotes ('') while adding integer.
|

**Listing and Inserting**

.. code-block:: python

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

|
Listing occurs in the if condition using 'GET' method.

In the else part, Team_Name and Leagues_ID is taken from the user and inserted to teams table.

After execution, developer returns admin page for teams.

|

**Searching**

.. code-block:: python

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
           query = "SELECT TEAMS.ID, TEAMS.Team_Name, LEAGUES.League_Name FROM TEAMS INNER JOIN LEAGUES ON TEAMS.Leagues_ID = LEAGUES.ID WHERE TEAMS.Team_Name LIKE '%" + search +"%'"
           cursor.execute(query)
           connection.commit()
           return render_template('teams.html', teams = cursor)

|
In the if part, it lists all of the datas.

If user wants to search for any specific team name, searching occurs in the else part.

|

**Deleting**

.. code-block:: python

   @app.route('/ADMIN/teams/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def admin_teams_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()
           cursor.execute("""DELETE FROM TEAMS WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('admin_teams_page'))

|
When delete is encountered, selected data is deleted from the table using its ID.

After execution, developer returns admin page for teams.

|

**Updating**

.. code-block:: python

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

|
In the first @app.route, leagues table is opened because any team's league may also change while editing teams.

When any row's update button is clicked, clicked row's ID is taken as UPDATEID.

In the second @app.route, new team name and league name will be taken.

Finally, update occurs.

|

Season Team
-----------


**Creating Table**

.. code-block:: python

    @app.route('/initdb')
    def initialize_database():
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

|
Season team table is created as seen above. It is cascade on both update and delete. It has 3 columns which are ID, Season_ID and Team_ID. Both Season_ID and Team_ID is foreign key.

   ID is auto incremented, integer and primary key.

   Season_ID is integer and foreign key. It references to seasons table's ID.

   Team_ID is integer and foreign key. It references to teams table's ID.
|

**Inserting Elements**

.. code-block:: python

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

|
Datas for season team table are added as seen above.

   ID is not added above because it is auto increment (by using SERIAL).

   Season_ID is added by writing an integer which is ID of seasons table.

   Team_ID is added by writing  an integer which is ID of teams table.
|

**Listing and Inserting**

.. code-block:: python

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

|
Listing occurs in the if condition using 'GET' method.

In the if part, inner join occured in "query" between teams, seasons and season_team tables. Season_Name is taken from seasons table and Team_Name is taken from teams table using Season_ID and Team_ID. Seasons and teams tables are opened because they will be joined.

In the else part, Season_ID and Team_ID is taken from the user and inserted to season_team table.

After execution, developer returns admin page for season team.

|

**Searching**

.. code-block:: python

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

|
In the if part, it lists all of the datas.

If user wants to search for any specific team name, searching occurs in the else part.

|

**Deleting**

.. code-block:: python

   @app.route('/ADMIN/season_team/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def admin_season_team_page_delete(DELETEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()
       cursor.execute("DELETE FROM SEASON_TEAM WHERE ID = %s", (int(DELETEID),))
       connection.commit()
       return redirect(url_for('admin_season_team_page'))

|
When delete is encountered, selected data is deleted from the table using its ID.

After execution, developer returns admin page for season team.

|

**Updating**

.. code-block:: python

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

|
In the first @app.route, seasons and teams tables are opened because season team table takes datas from seasons and teams tables.

When any row's update button is clicked, clicked row's ID is taken as UPDATEID.

In the second @app.route, new season id and team id will be taken.

Finally, update occurs.

|


Admin Information
-----------------

**Creating Table**

.. code-block:: python

    @app.route('/initdb')
    def initialize_database():
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

|
Site table is created as seen above. It has 5 columns which are ID, Admin_Name, Admin_Password, Site_Name and Slogan.

   ID is auto incremented, integer and primary key.

   Admin_Name is varchar and cannot be NULL.

   Admin_Password is varchar and cannot be NULL.

   Site_Name is varchar and cannot be NULL.

   Slogan is varchar and cannot be NULL.

|

**Inserting Elements**

.. code-block:: python

    query = """INSERT INTO SITE (Admin_Name, Admin_Password, Site_Name, Slogan) VALUES ('Meric','lolololo','itucsdb1527','Cimbombom')"""
    cursor.execute(query)
    query = """INSERT INTO SITE (Admin_Name, Admin_Password, Site_Name, Slogan) VALUES ('Volleybase','uyar','itucsdb1527','Cimbombom')"""
    cursor.execute(query)

|
Datas for site table are added as seen above.

   ID is not added above because it is auto increment (by using SERIAL).

   Admin_Name is added between quotes ('') because it is varchar.

   Admin_Password is added between quotes ('') because it is varchar.

   Site_Name is added between quotes ('') because it is varchar.

   Slogan is added between quotes ('') because it is varchar.

|

**Listing and Inserting**

.. code-block:: python

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

|
Listing occurs in the if condition using 'GET' method.

In the if part, all columns of site table are selected and ordered by IDs.

In the else part, admin_name, admin_password, site_name and slogan are taken from the user and inserted to site table.

After execution, developer returns admin page for site table.

|

**Deleting**

.. code-block:: python

   @app.route('/ADMIN/admin/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def admin_admin_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()
           cursor.execute("""DELETE FROM SITE WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('admin_admin_page'))

|
When delete is encountered, selected data is deleted from the table using its ID.

After execution, developer returns admin page for site table.

|

**Updating**

.. code-block:: python

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

|
In the first @app.route, site table is opened.

When any row's update button is clicked, clicked row's ID is taken as UPDATEID.

In the second @app.route, new admin_name, new admin_password, new site_name and new slogan will be taken.

Finally, update occurs.

|
