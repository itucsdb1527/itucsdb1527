================================================
Players, Player Teams, Countries (Meral Korkmaz)
================================================
#######
Players
#######
****************
Class Definition
****************

One of the biggest concerns of sports fans are their favorite players. People can relate to other people--we suppose this is why people love sports players so much. This is why we decided to add a players table to our web application.
This way, users of our web application are able to access up to date, latest exciting information about their favorite volleyball players. We defined a player class such that it keeps the most important information about a player.
The first element in the player class is the player name. The next piece of information that the user can see is the nationality of a player. Additional important information includes the age of the number. Perhaps the most important
detail that users are interested in knowing about a player is the number of that player. Although we consider our name as our identifier, for most sports players, a number is a critical identifier. The next important piece of information
that users can see is the position of the player. We Figured that by knowing the strength of that player, fans can decide on their favorite players of same or different position specialties.

The class definiton of players is given below in the python code block. The query is written in SQL. Once the query is executed, the table is created.

.. code-block:: python
   :caption: admin.py
   :name: players class definition

   query = """DROP TABLE IF EXISTS PLAYERS CASCADE"""
   cursor.execute(query)
   query = """CREATE TABLE PLAYERS (
         ID SERIAL PRIMARY KEY,
         NAME VARCHAR NOT NULL,
         NATIONALITY_ID INTEGER NOT NULL,
         AGE INTEGER NOT NULL,
         NUMBER INTEGER NOT NULL,
         POSITION VARCHAR NOT NULL,
         FOREIGN KEY (NATIONALITY_ID)
         REFERENCES NATIONALITIES(ID)
         ON DELETE CASCADE ON UPDATE CASCADE)"""
         cursor.execute(query)

*******
Methods
*******

The players table has various methods. These methods allow the admin users to manage the database from the admin panel. There are additional methods that are written for the convenience of the user. The methods
that are written for the admin panel include initialize, insert, update and delete. The admin can manage the database by adding new players as they are discovered, updating information on a player that was unknown
before, or deleting a player that has retired. The initialize function is written to create the table and insert all of the initial players that are in our database system if the table doesn't already exist.
Also, visitors to the site are able to search for their favorite players by their names.

----
Init
----

The initialization function as stated creates the table if it doesn't already exist. It also adds values to the table. These values have been defined by the admin. The code block below illustrates the initialization function for
players. As stated above, the queries are written in the SQL language. The values inside the first parentheses, indicate the order of the attributes for each of the three tuples to be added. The values in the second set of parentheses
are the values to be inserted in the order indicated in the first set. After each query is entered, it is executed so that the command in the query is realized. With each line, a new player tuple is added to the players relation.

.. code-block:: python
   :caption: Players table initialize database.
   :name: admin.py (PLAYERS initDB)

    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES
    ('MERAL',1, 20, 8,'Right Side Hitter')"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES
    ('CEMAL',1, 24, 15,'Opposite')"""
    cursor.execute(query)
    query = """INSERT INTO PLAYERS (NAME,NATIONALITY_ID, AGE, NUMBER, POSITION) VALUES
    ('SEYMA',1, 21, 9,'Outside Hitter')"""
    cursor.execute(query)

.. Figure:: m1img/player/adminpage.png
   :width: 400pt

   The main page of the admin panel.

.. Figure:: m1img/player/playerinitdb.png
   :width: 400pt

   The players table after the database is initialized.

------
Insert
------

As mentioned, the insert operation for players takes place in the admin panel. We define a function that is capable of a get and post method. Simply speaking, the get method takes the information queried in the SQL statement from the database and
prints that information on the site. At the end of this process, we can see the players table on the administrator tab for players. As its name suggests, the post method takes the information given from a user and concatenates the information it takes
with the SQL query in the code. It then executes the query and a new player is then created using the information that the admin entered into the site. The get process can be seen in the code block in Listing 2.4. The post method can be seen in Listing 2.5.

Below is the definition for the players table function for the admin panel.

.. code-block:: python
   :caption: Function definition for the administrator panel players page.
   :name: admin.py (PLAYERS initDB)

   @app.route('/ADMIN/players', methods=['GET', 'POST'])
   def admin_players_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

.. code-block:: python
   :caption: The get method (to print Players table on the admin page).
   :name: admin.py (PLAYERS initDB)

    if request.method == 'GET':

        query = "SELECT PLAYERS.ID, NAME, NATIONALITY, AGE, NUMBER, POSITION
        FROM PLAYERS,NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID"

        cursor.execute(query)
        cursor2 = connection.cursor()
        query = "SELECT * FROM NATIONALITIES"
        cursor2.execute(query)
        return render_template('admin/players.html', players = cursor,
        nationalities = cursor2)

.. code-block:: python
   :caption: The post method (to add a new player to the Players relation).
   :name: admin.py (PLAYERS initDB)

    else:
        name_in = request.form['name']
        nationality_in = request.form['nationalityID']
        age_in = request.form['age']
        number_in = request.form['number']
        position_in = request.form['position']

        query = """INSERT INTO PLAYERS (NAME, NATIONALITY_ID, AGE, NUMBER, POSITION)
        VALUES ('"""+name_in+"', '"+nationality_in+"', '"+age_in+"', '"+number_in+"',
        '"+position_in+"')"

        cursor.execute(query)
        connection.commit()
        return redirect(url_for('admin_players_page'))

.. Figure:: m1img/player/playeradded.png
   :width: 400pt

   The players table when the user attempts to add a new player.

.. Figure:: m1img/player/playeradded.png
   :width: 400pt

   The player table after the insertion of a new player.


------
Update
------

The update operation requires two functions. The first function selects the player tuple from the table with an ID identical to the
ID of the player that the user selected. It then redirects the user to the players_edit HTML page. In this page, the admin can see
a new table with only the tuple that needs updating. The updated values are entered into this table and the update button is clicked.
Once the button has been clicked, the user is redirected back into the admin panel for players with the updated table printed to the screen.

Listing 2.6 gives the update function that takes the value to be updated into a new web page. Listing 2.7 gives the update function that applies
the changes to the selected tuple.

.. code-block:: python
   :caption: The update function selects the player that is to be updated.
   :name: admin.py (PLAYERS UPDATE)

   @app.route('/ADMIN/players/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def admin_players_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("SELECT * FROM PLAYERS WHERE ID = %s", (int(UPDATEID),))
       cursor2 = connection.cursor()
       query = "SELECT * FROM NATIONALITIES"
       cursor2.execute(query)
       connection.commit()
       return render_template('admin/players_edit.html',
       players = cursor, nationalities = cursor2)


.. code-block:: python
   :caption: The update apply function takes new entries from a user and updates the selected player.
   :name: admin.py (PLAYERS UPDATE APPLY)

   @app.route('/ADMIN/players/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def admin_players_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       new_name = request.form['name']
       new_nationality = request.form['nationalityID']
       new_age = request.form['age']
       new_number = request.form['number']
       new_position = request.form['position']

       query = "UPDATE PLAYERS SET NAME = '%s', NATIONALITY_ID = %d, AGE = %d,
       NUMBER = %d, POSITION = '%s'  WHERE ID = %d"
       % (new_name,int(new_nationality),int(new_age), int(new_number), new_position,
       int(UPDATEID))

       cursor.execute(query)
       connection.commit()
       return redirect(url_for('admin_players_page'))

.. Figure:: m1img/player/playerupdate.png
   :width: 400pt

   The players table when the user selects a player to update.

.. Figure:: m1img/player/playerupdated.png
   :width: 400pt

   The player table after the update has taken place.

------
Delete
------

The admin also has the option to delete a player tuple from the relation. This is done by clicking the delete button next to the update button
at the end of each tuple on the admin panel for the players table. When the user clicks the delete button, the code block given in Listing 2.8 is called.
In this function, the ID of the selected player is taken as a parameter into the delete query. When the query is executed, the player is deleted from the
database.

.. code-block:: python
   :caption: The delete function deletes the player with ID identical to the selected player ID.
   :name: admin.py (PLAYERS UPDATE APPLY)

   @app.route('/ADMIN/players/DELETE/<int:DELETEID>', methods=['GET','POST'])
   def admin_players_page_delete(DELETEID):
       connection=dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("DELETE FROM PLAYERS WHERE ID = %s", (int(DELETEID),))
       connection.commit()
       return redirect(url_for('admin_players_page'))

------
Search
------

Unlike the other operations, the search operation is available in the user side of the webpage. In the players page, the players relation is
displayed to the user in a table. Above the table, there is a search box and a search button where the users can search for a player they are
interested about by name. When the user enters the name or the portion of the name of a player, the search key is sent to the function in Listing 2.9. The first part of the code after the if
statement displays the entire table to the user. This is the get part of the code. In the post part of the code however, a key named search is returned to the
function. This search is then inserted to the SQL query and the user is redirected to a page where he or she can see the results of this search query.  Figure 2.26 shows the database table before the user searches for a player. Figure 2.27 illustrates the results of a user's search.

.. code-block:: python
   :caption: The search function searches for players by name.
   :name: players.py

   @app.route('/players', methods=['GET', 'POST'])
   def players_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       if request.method == 'GET':
           query = "SELECT PLAYERS.ID, NAME,NATIONALITY, AGE, NUMBER, POSITION FROM
           PLAYERS, NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID"
           cursor.execute(query)
           cursor2 = connection.cursor()
           query = "SELECT * FROM NATIONALITIES"
           cursor2.execute(query)
           return render_template('players.html', players = cursor,
           nationalities = cursor2)
       else:
           search = request.form['search']
           query = "SELECT PLAYERS.ID, NAME, NATIONALITY, AGE, NUMBER, POSITION FROM
           PLAYERS, NATIONALITIES WHERE NATIONALITY_ID = NATIONALITIES.ID AND NAME LIKE
            '%"+ search +"%'"
           cursor.execute(query)
           connection.commit()
           return render_template('players.html', players = cursor)


.. Figure:: m1img/player/playerstable.png
   :width: 400pt

   The players table as the user sees in the players page of the website.

.. Figure:: m1img/player/playerstablesearch.png
   :width: 400pt

   The player table after the user performs a search operation.

*********
Relations
*********

As mentioned, each player has a nationality. These nationality ID's are obtained from the nationalities table. Thus, it can be said that the
NATIONALITY_ID of a player is a foreign key to the nationalities table. In the players table, we only keep the ID value of the nationality of a
player. However, if we are going to print the nationality of the player for the users to see, we need to include the entire nationality table
in our select statement so that we can use the name that corresponds to the ID.



############
Team Players
############

Another relation we thought would be very important for our web application was the team players relation. This relation gives us information
on which player plays on which team and which season. As this information is only relevant to the admin, we decided that this part would remain
in the admin panel of the web application.

****************
Class Definition
****************

In this class, we have three attributes. The first is a PlayerID that comes from the Players table. The next attribute is the TeamID which comes
from the Teams table. The last attribute is the SeasonID which is obtained from the seasons relation. Listing 2.10 gives the python code that
executes the SQL query to create the table.

.. code-block:: python
   :caption: This function creates the Team Players table if it doesn't already exist.
   :name: admin.py (Creates Team Players Table)

    query = """DROP TABLE IF EXISTS TEAMPLAYERS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE TEAMPLAYERS (
                    PLAYERID INTEGER NOT NULL,
                    TEAMID INTEGER NOT NULL,
                    SEASONID INTEGER NOT NULL,
                    FOREIGN KEY (PLAYERID) REFERENCES PLAYERS(ID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (TEAMID) REFERENCES TEAMS(ID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (SEASONID) REFERENCES SEASONS(ID)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    PRIMARY KEY (PLAYERID, TEAMID, SEASONID)
                    )"""
    cursor.execute(query)
    connection.commit()
    return redirect(url_for('admin_home_page'))

*******
Methods
*******
----
Init
----

In the initDB function, no tuples are added to the Team Players table because all of the values that are added must
already exist in the database. Inserting values directly may cause issues if the values we are trying to insert don't exist
in the database. This is why we chose to create the table as it is and insert after the table was created.

------
Insert
------

Only the admin can add new tuples to this relation. This is why this table is only visible to the admin panel. in order to
see the items that are already on the table, we have written a python function given in Listing 2.11. In this code, the entire table
is selected along with the tables that have the values of the foreign keys of this table (Team Players, Players, Teams, Seasons). These four
cursors are sent to the html page and the values are printed in a table for the admin to see. The resulting table on the web application is given in
Figure 2.28.

Another function was written in python to add new values to the Team Players table. This function takes the values from the HTML page and inserts them
as parameters to the SQL query that adds new values. The resulting query is then executed and the user is redirected to the admin team players panel.
Now the table is refreshed and the user can see the new value that was inserted. The code block in Listing 2.12.

.. code-block:: python
   :caption: This function prints all of the tuples of the Team Players relation to the players admin panel.
   :name: admin.py (Print Team Players Table)

   @app.route('/ADMIN/teamplayers', methods=['GET', 'POST'])
   def admin_team_players_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       if request.method == 'GET':
           query = "SELECT PLAYERS.ID, PLAYERS.NAME, SEASONS.ID, SEASONS.Season_Name,
           TEAMS.ID,TEAMS.Team_Name FROM TEAMPLAYERS, PLAYERS, SEASONS, TEAMS
           WHERE PLAYERID = PLAYERS.ID AND TEAMID = TEAMS.ID AND SEASONID = SEASONS.ID"
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
           return render_template('/ADMIN/teamplayers.html', teamplayers = cursor,
           players = cursor2, seasons = cursor3, teams = cursor4)

.. Figure:: m1img/player/teamplayers.png
   :width: 400pt

   The Team Players table from the admin panel for Team Players.

.. code-block:: python
   :caption: This function inserts a new Team Player item into the relation.
   :name: admin.py (Insert Team Player Item)

       else:
           playerid_in = request.form['playerid']
           seasonid_in = request.form['seasonid']
           teamid_in = request.form['teamid']
           query = """INSERT INTO TEAMPLAYERS (PLAYERID, SEASONID, TEAMID) VALUES
           (%d,%d,%d)""" % (int(playerid_in), int(seasonid_in), int(teamid_in))
           cursor.execute(query)
           connection.commit()
           return redirect(url_for('admin_team_players_page'))

------
Update
------

Similarly to the players relation, the update function for the Team Players relation consists of two parts. The first function given in Listing 2.13 allows the admin to select
a tuple that is to be deleted. The admin is then redirected to a site with only that tuple on display. The new information that the admin has entered is sent to the code block in Listing 2.14 is sent
as parameters to the Update SQL statement. The admin can then view the updated Team Players table. Figure 2.10 depicts the admin making changes to the table.


.. code-block:: python
   :caption: The update function selects the Team Player item that is to be updated.
   :name: admin.py (TEAM PLAYERS UPDATE)

   @app.route('/ADMIN/teamplayers/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def admin_team_players_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()
       query = "SELECT playerid, seasonid, teamid FROM TEAMPLAYERS WHERE
       PLAYERID = %d" % int(UPDATEID)
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
       return render_template('admin/teamplayers_edit.html',
       teamplayers = cursor, players = cursor2,
       seasons = cursor3, teams = cursor4)

.. code-block:: python
   :caption: The update apply function takes new entries from a user and updates the selected Team Player item.
   :name: admin.py (TEAM PLAYERS UPDATE APPLY)

   @app.route('/ADMIN/teamplayers/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def admin_team_players_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()
       new_playerid = request.form['playerid']
       new_seasonid = request.form['seasonid']
       new_teamid = request.form['teamid']
       query = "UPDATE TEAMPLAYERS SET PLAYERID = %d, SEASONID = %d, TEAMID = %d WHERE
        PLAYERID = %d"
       % (int(new_playerid), int(new_seasonid), int(new_teamid), int(UPDATEID))
       cursor.execute(query)
       connection.commit()
       return redirect(url_for('admin_team_players_page'))

.. Figure:: m1img/player/updateteamplayers.png
   :width: 400pt

   Updating the Team Players table from the admin panel for Team Players.

------
Delete
------

Listing 2.15 is the delete function for the Team Players table. This function takes an integer called DELETEID from the
tuple that was clicked on the website. This ID is put into the Delete SQL statement as a parameter. After the query is executed,
the item is deleted and the admin is redirected to see the refreshed table.

.. code-block:: python
   :caption: The update function deletes the selected Team Player item from the relation.
   :name: admin.py (TEAM PLAYERS DELETE)

   @app.route('/ADMIN/teamplayers/DELETE/<int:DELETEID>', methods=['GET','POST'])
   def admin_team_players_page_delete(DELETEID):
       connection=dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("DELETE FROM TEAMPLAYERS WHERE PLAYERID = %s", (int(DELETEID),))
       connection.commit()
       return redirect(url_for('admin_team_players_page'))

*********
Relations
*********

Since a player must exist to have a team and play in a season, we determined that the PlayerID must come from the players table. Similarly, for a player
to be on a team, that team must exist--thus, the TeamID comes from the teams page. To parallel with the previous two explanations, for a player to be in a
season, that season must exist. Therefore, the SeasonID is a foreign key to the ID attribute of the Seasons relation.


#########
Countries
#########

The countries table is again only visible to the admin because the information on it is only relevant to the admin. The countries table is a convenience for
other admins of the database to pull information from as foreign keys. Although the country information alone presents no significance to the overall database,
country information is used in various tables. This is why we saw it necessary to create a countries table.

****************
Class Definition
****************

The class for this relation is very simple. Each country has its own ID value and a name as attributes. The table for the relation only consists of 2 columns.
Listing 2.16 gives the definition of the class.

.. code-block:: python
   :caption: This function creates the countries table if it doesn't already exist.
   :name: admin.py (COUNTRIES CREATE TABLE)

    query = """DROP TABLE IF EXISTS COUNTRIES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE COUNTRIES (
                    ID SERIAL PRIMARY KEY,
                    NAME VARCHAR NOT NULL
                    )"""
    cursor.execute(query)

*******
Methods
*******
----
Init
----

The initialize database function inserts some default values into the database. These values are sent in diretly by SQL queries.
After each query is entered, it is executed and the tuple is entered into the relation. Listing 2.17 gives the code that initializes this relation.

.. code-block:: python
   :caption: The InitDB function for the countries table.
   :name: admin.py (COUNTRIES InitDB)

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


------
Insert
------

In Listing 2.18, the code block is the function to insert a new tuple to the countries. In the first part, for the get method,
the entire relation is selected and sent to the html file. There, it is printed for the admin to see the entire table of countries.
In the second part of the code block, the name_in part is the name information that is sent from the HTML file. This part is sent into
the SQL Statement as a parameter and the new name is added to the table of countries. Figure 2.11 shows the countries table as the
admin user sees it on the admin panel for countries page.

.. code-block:: python
   :caption: The insert function for the countries table.
   :name: admin.py (COUNTRIES INSERT)

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

.. Figure:: m1img/player/countries.png
   :width: 200pt

   The countries table as it appears after initializing database in the admin panel.

------
Update
------

As mentioned above, the update function works in two parts. The first part selects the tuple that the user wishes to update and redirects the user to a new
page to update the attributes of the tupele. This process is given in Listing 2.19. In this new page, the user can see the tuple to be updated and the new values
are sent into the python code. These values are taken in as the update SQL statement queries in Listing 2.20. Figure 2.12 illustrates the table after an update
operation.

.. code-block:: python
   :caption: The update function that selects the tuple to be updated.
   :name: admin.py (COUNTRIES UPDATE)

   @app.route('/ADMIN/countries/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def admin_countries_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("SELECT * FROM COUNTRIES WHERE ID = %s", (int(UPDATEID),))
       connection.commit()
       return render_template('admin/countries_edit.html', countries = cursor)

.. code-block:: python
   :caption: The update function that updates the selected tuple.
   :name: admin.py (COUNTRIES UPDATE)

   @app.route('/ADMIN/countries/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def admin_countries_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       new_name = request.form['name']
       query = """UPDATE COUNTRIES SET NAME = '%s' WHERE ID = %d""" % (new_name, int(UPDATEID))
       cursor.execute(query)
       connection.commit()
       return redirect(url_for('admin_countries_page'))

.. Figure:: m1img/player/countriesupdate.png
   :width: 200pt

   The countries table after the update operation.

------
Delete
------
Listing 2.21 is the code block for the deletion of a country tuple. This function takes the deleteID as a parameter into the delete SQL statement.
The statement is executed and the tuple is deleted. After the delete operation, the table looks as in Figure 2.13.

.. code-block:: python
   :caption: The delete function deletes a country tuple from the countries relation.
   :name: admin.py (COUNTRIES DELETE)

   @app.route('/ADMIN/countries/DELETE/<int:DELETEID>', methods=['GET','POST'])
   def admin_countries_page_delete(DELETEID):
       connection=dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("DELETE FROM COUNTRIES WHERE ID = %s", (int(DELETEID),))
       connection.commit()
       return redirect(url_for('admin_countries_page'))

.. Figure:: m1img/player/countriesupdate.png
   :width: 200pt

   The countries table after the delete operation.

*********
Relations
*********

This table is a table that many other tables are related to. It does not have any foreign keys to other tables. It's a simple standalone table.
