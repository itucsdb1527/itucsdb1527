Parts Implemented by Seyma Umutlu
=================================

General View
------------

|
In this section, firstly the contents of the tables will be explained and later the details of the codes for database operation will be given.
|

Matches
-------

|
The contents of the matches table and the initialized version of tuples are shown below.
|

.. figure:: seyma/4.png
   :figclass: align-center

   figure 3.2.1

**Create Function**

.. code-block:: python

      @app.route('/matches/initdb')
      def initialize_database_matches():
          connection = dbapi2.connect(app.config['dsn'])
          cursor = connection.cursor()

          query = """DROP TABLE IF EXISTS MATCHES CASCADE"""
          cursor.execute(query)
          query = """CREATE TABLE MATCHES (ID SERIAL PRIMARY KEY, Team1ID INTEGER NOT NULL, Team2ID INTEGER NOT NULL, ArenaName VARCHAR, RefereeName VARCHAR,
                  FOREIGN KEY (Team1ID) REFERENCES TEAMS(ID) ON UPDATE CASCADE ON DELETE CASCADE,
                  FOREIGN KEY (Team2ID) REFERENCES TEAMS(ID) ON UPDATE CASCADE ON DELETE CASCADE
                  )"""
          cursor.execute(query)

|
The code above shows the create table function. Firstly it checks if there exists a matches table, if so it drops the table, then creates a new table.
When creating, primary key and foreign keys from team table are assigned. In order to keep tables coordinated, cascade operation is done on update and delete functions.
|

**Inserting Initialized Version**

.. code-block:: python

    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (1, 3, 'Sinan Erdem', 'Brad Aaberg')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (2, 11 , 'Abdi Ipekci', 'Stephen Arichea')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (8, 9 , 'FB Ulker', 'Rose Atkinson')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (13, 4 , 'Volkswagen Arena', 'Dan Apol')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (18, 1 , 'Burhan Felek', 'Mary Black')"""
    cursor.execute(query)
    query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (15, 12 , 'Pavilhao Rosa Mota', 'Fred Buchler')"""
    cursor.execute(query)

**List and Insert**

.. code-block:: python

   @app.route('/matches', methods=['GET', 'POST'])
   def matches_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       if request.method == 'GET':
           query = "SELECT MATCHES.ID, Team1.Team_Name, Team2.Team_Name, MATCHES.ArenaName, MATCHES.RefereeName FROM MATCHES INNER JOIN TEAMS AS TEAM1 ON MATCHES.TEAM1ID = TEAM1.ID INNER JOIN TEAMS AS TEAM2 ON MATCHES.TEAM2ID = TEAM2.ID"
           cursor.execute(query)
           return render_template('matches.html', matches = cursor)
       else:
           Team1Name_in = request.form['Team1ID']
           Team2Name_in = request.form['Team2ID']
           ArenaName_in = request.form['ArenaName']
           RefereeName_in = request.form['RefereeName']

           query = """INSERT INTO MATCHES (Team1ID, Team2ID, ArenaName, RefereeName)
           VALUES ('"""+Team1Name_in+"', '"+Team2Name_in+"', '"+ArenaName_in+"', '"+RefereeName_in+"')"
           cursor.execute(query)

           connection.commit()
           return redirect(url_for('matches_page'))

       return render_template('matches.html')
|
With the code above, the listing function is done using select command. Later inserting operation is done using the values which are gotten
from forms.
|

**Update Function**

.. code-block:: python

   @app.route('/matches/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def matches_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()
       cursor2 = connection.cursor()
       query = "SELECT ID, Team_Name FROM TEAMS"
       cursor2.execute(query)

       cursor.execute("""SELECT ID, Team1ID, Team2ID, ArenaName, RefereeName FROM MATCHES WHERE ID = %s""", (int(UPDATEID),))
       connection.commit()
       return render_template('matches_edit.html', matches = cursor, teams = cursor2)

   @app.route('/matches/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def matches_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       new_name1 = request.form['Team1ID']
       new_name2 = request.form['Team2ID']
       new_arena = request.form['ArenaName']
       new_referee = request.form['RefereeName']
       query = """UPDATE MATCHES SET Team1ID = %d, Team2ID = %d, ArenaName = '%s', RefereeName = '%s' WHERE ID = %d""" % (int(new_name1), int(new_name2), new_arena, new_referee, int(UPDATEID))
       cursor.execute(query)
       connection.commit()
       return redirect(url_for('matches_page'))

|
The first part of the code, opens a new page when 'update' button is pushed. With the index gotten from the first page, the values which are
obtained from forms is updated to the tuple the user wants to update.
|

**Delete Function**

.. code-block:: python

    @app.route('/matches/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def matches_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()

           cursor.execute("""DELETE FROM MATCHES WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('matches_page'))
|
This code deletes the tuple that user wants to delete using delete operation of SQL and index which is obtained from the page.
|

Scores
------

|
The contents of the scores table and the initialized version of tuples are shown below.
|

.. figure:: seyma/5.png
   :figclass: align-center

   figure 3.2.2

**Create Function**

.. code-block:: python

    @app.route('/scores/initdb')
   def initialize_database_scores():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       query = """DROP TABLE IF EXISTS SCORES"""
       cursor.execute(query)
       query = """CREATE TABLE SCORES (ID SERIAL PRIMARY KEY, MatchID INTEGER NOT NULL, Team1Score VARCHAR NOT NULL, Team2Score VARCHAR NOT NULL)"""
       cursor.execute(query)

|
The code above shows the create table function. Firstly it checks if there exists a scores table, if so it drops the table, then creates a new table.
When creating, primary key is assigned.
|

**Inserting Initialized Version**

.. code-block:: python

    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('3001', '0', '3')"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('1012', '1', '3')"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('1104', '2', '3')"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('2003', '3', '0')"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('1705', '1', '3')"""
    cursor.execute(query)
    query = """INSERT INTO SCORES (MatchID, Team1Score, Team2Score) VALUES ('2705', '3', '0')"""
    cursor.execute(query)ES (Team1ID, Team2ID, ArenaName, RefereeName) VALUES (15, 12 , 'Pavilhao Rosa Mota', 'Fred Buchler')"""
    cursor.execute(query)

**List and Insert**

.. code-block:: python

   @app.route('/scores', methods=['GET', 'POST'])
   def scores_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       if request.method == 'GET':
           query = "SELECT * FROM SCORES"
           cursor.execute(query)
           return render_template('scores.html', scores = cursor)
       else:
           MatchID_in = request.form['MatchID']
           Team1Score_in = request.form['Team1Score']
           Team2Score_in = request.form['Team2Score']

           query = """INSERT INTO SCORES (MatchID ,Team1Score, Team2Score)
           VALUES ('"""+MatchID_in+"', '"+Team1Score_in+"', '"+Team2Score_in+"')"
           cursor.execute(query)

           connection.commit()
           return redirect(url_for('scores_page'))

       return render_template('scores.html')

|
With the code above, the listing function is done using select command. Later inserting operation is done using the values which are gotten
from forms.
|

**Update Function**

.. code-block:: python

   @app.route('/scores/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def scores_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("""SELECT ID, MatchID, Team1Score, Team2Score FROM SCORES WHERE ID = %s""", (int(UPDATEID),))
       connection.commit()
       return render_template('scores_edit.html', scores = cursor)

   @app.route('/scores/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def scores_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       new_match = request.form['MatchID']
       new_name1 = request.form['Team1Score']
       new_name2 = request.form['Team2Score']
       query = """UPDATE SCORES SET MatchID = '%d', Team1Score = '%s', Team2Score = '%s' WHERE ID = %d""" % (int(new_match), new_name1, new_name2, int(UPDATEID))
       cursor.execute(query)
       connection.commit()
       return redirect(url_for('scores_page'))

|
The first part of the code, opens a new page when 'update' button is pushed. With the index gotten from the first page, the values which are
obtained from forms is updated to the tuple the user wants to update.
|

**Delete Function**

.. code-block:: python

   @app.route('/scores/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def scores_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()

           cursor.execute("""DELETE FROM SCORES WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('scores_page'))
|
This code deletes the tuple that user wants to delete using delete operation of SQL and index which is obtained from the page.
|

Maillist
--------

|
The contents of the maillist table and the initialized version of tuples are shown below.
|

.. figure:: seyma/6.png
   :figclass: align-center

   figure 3.2.3

**Create Function**

.. code-block:: python

      @app.route('/maillist/initdb')
   def initialize_database_maillist():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       query = """DROP TABLE IF EXISTS MAILLIST"""
       cursor.execute(query)
       query = """CREATE TABLE MAILLIST (ID SERIAL PRIMARY KEY, Mail VARCHAR NOT NULL, TeamID VARCHAR NOT NULL)"""
       cursor.execute(query)

|
The code above shows the create table function. Firstly it checks if there exists a maillist table, if so it drops the table, then creates a new table.
When creating, primary key is assigned.
|

**Inserting Initialized Version**

.. code-block:: python

       query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('ozkalt@itu.edu.tr', 'itucsdb1527')"""
       cursor.execute(query)
       query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('umutlus@itu.edu.tr','itucsdb1527')"""
       cursor.execute(query)
       query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('turanmeri@itu.edu.tr','itucsdb1527')"""
       cursor.execute(query)
       query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('tugs@itu.edu.tr','itucsdb1516')"""
       cursor.execute(query)
       query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('korkmazmer@itu.edu.tr','itucsdb1527')"""
       cursor.execute(query)
       query = """INSERT INTO MAILLIST (Mail, TeamID) VALUES ('kuyucuc@itu.edu.tr','itucsdb1527')"""
       cursor.execute(query)

**List and Insert**

.. code-block:: python

   @app.route('/maillist', methods=['GET', 'POST'])
   def maillist_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       if request.method == 'GET':
           query = "SELECT * FROM MAILLIST order by ID"
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

|
With the code above, the listing function is done using select command. Later inserting operation is done using the values which are gotten
from forms.
|

**Update Function**

.. code-block:: python

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

|
The first part of the code, opens a new page when 'update' button is pushed. With the index gotten from the first page, the values which are
obtained from forms is updated to the tuple the user wants to update.
|

**Delete Function**

.. code-block:: python

   @app.route('/maillist/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def maillist_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()

           cursor.execute("""DELETE FROM MAILLIST WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('maillist_page'))
|
This code deletes the tuple that user wants to delete using delete operation of SQL and index which is obtained from the page.
|

