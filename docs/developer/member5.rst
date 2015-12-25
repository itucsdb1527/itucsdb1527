Parts Implemented by Tugba Ozkal
================================

General View
------------

|
Codes of database operations and contents of tables will be explained in this part.
|

Referees
--------

|
Attributes of the referee table and initialized records are shown in the figure 5.2.1.

|

.. figure:: tugba/1.png
   :figclass: align-center

   figure 5.2.1

**Create Function**


.. code-block:: python

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


|
In the code above, the table is created. If the table is already created, it will drop it and create it again. Also primary and foreign keys assigned.
Keeping the integrity stable, the cascade operations are applied on delete and update.
|

**Initilize Insert**


.. code-block:: python

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


**List and Insert**

.. code-block:: python

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


|
In this piece of code, the table is listed and values which comes from the users are inserted into the table.
|


**Update Function**

.. code-block:: python

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


|
In this code, inserted values before can be updated in the new opened page.
|

**Delete Function**

.. code-block:: python

   @app.route('/referees/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def referees_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()


           cursor.execute("""DELETE FROM REFEREES WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('referees_page'))

|
Here, a referee which is wanted to be removed can be remove.
|

Nationality
-----------

|
Attributes of the nationality table and initialized records are shown in the figure 5.2.2.
|

.. figure:: tugba/3.png
   :figclass: align-center

   figure 5.2.2

**Create Function**


.. code-block:: python

   @app.route('/nationalities/initdb')
   def initialize_database_nationalities():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       query = """DROP TABLE IF EXISTS NATIONALITIES CASCADE """
       cursor.execute(query)
       query = """CREATE TABLE NATIONALITIES (ID SERIAL PRIMARY KEY, Nationality VARCHAR NOT NULL
       )"""
       cursor.execute(query)


|
In the code above, the table is created. If the table is already created, it will drop it and create it again. Also primary and foreign keys assigned.
Keeping the integrity stable, the cascade operations are applied on delete and update.
|

**Initilize Insert**

.. code-block:: python

    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('North Country')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Northern California')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Sun Country')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Turkey')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('German')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('USA')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('UK')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Portuguese')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('Korea')"""
    cursor.execute(query)
    query = """INSERT INTO NATIONALITIES (Nationality)
    VALUES ('India')"""
    cursor.execute(query)


**List and Insert**


.. code-block:: python

   @app.route('/nationalities', methods=['GET', 'POST'])
   def nationalities_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       if request.method == 'GET':
           query = "SELECT * FROM NATIONALITIES"
           cursor.execute(query)
           return render_template('nationalities.html', nationalities = cursor)
       else:
           nationality_in = request.form['nationality']
           query = """INSERT INTO NATIONALITIES (Nationality)
           VALUES ('"""+nationality_in+"')"
           cursor.execute(query)
           connection.commit()
           return redirect(url_for('nationalities_page'))
|
In this piece of code, the table is listed and values which comes from the users are inserted into the table.
|

**Update Function**

.. code-block:: python

   @app.route('/s/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def nationalities_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("""SELECT ID, Nationality FROM NATIONALITIES WHERE ID = %s""", (int(UPDATEID),))
       connection.commit()
       return render_template('nationalities_edit.html', nationalities = cursor)

   @app.route('/nationalities/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def nationalities_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       new_nationality = request.form['nationality']
       query = """UPDATE NATIONALITIES SET Nationality = '%s' WHERE ID = %d""" % (new_nationality, int(UPDATEID))
       cursor.execute(query)
       connection.commit()
       return redirect(url_for('nationalities_page'))
|
In this code, inserted values before can be updated in the new opened page.
|

**Delete Function**

.. code-block:: python

   @app.route('/nationalities/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def nationalities_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()


           cursor.execute("""DELETE FROM NATIONALITIES WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('nationalities_page'))

|
Here, a nationality which is wanted to be removed can be remove.
|

Arena
-----

|
Attributes of the arena table and initialized records are shown in the figure 5.2.3.
|

.. figure:: tugba/2.png
   :figclass: align-center

   figure 5.2.3


**Create Function**

.. code-block:: python

   @app.route('/arenas/initdb')
   def initialize_database_arenas():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       query = """DROP TABLE IF EXISTS ARENAS"""
       cursor.execute(query)
       query = """CREATE TABLE ARENAS (ID SERIAL PRIMARY KEY, ArenaName VARCHAR NOT NULL, ArenaBuiltDate INTEGER, ArenaCity VARCHAR NOT NULL, ArenaCapacity INTEGER)"""
       cursor.execute(query)

|
In the code above, the table is created. If the table is already created, it will drop it and create it again. Also primary and foreign keys assigned.
Keeping the integrity stable, the cascade operations are applied on delete and update.
|

**Initilize Insert**

.. code-block:: python

    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Burhan Felek',2010,'Istanbul',7500)"""
    cursor.execute(query)
    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Memorial Coliseum',1976,'Kentucky',23000)"""
    cursor.execute(query)
    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Volkswagen Arena',1998,'Istanbul',8000)"""
    cursor.execute(query)
    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Sinan Erdem',2000,'Afyonkarahisar',25357)"""
    cursor.execute(query)
    query = """INSERT INTO ARENAS (ArenaName,ArenaBuiltDate,ArenaCity,ArenaCapacity) VALUES ('Pavilhao Rosa Mota',1991,'Porto',5400)"""
    cursor.execute(query)

**List and Insert**

.. code-block:: python

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
|
In this piece of code, the table is listed and values which comes from the users are inserted into the table.
|

**Update Function**

.. code-block:: python

   @app.route('/arenas/UPDATE/<int:UPDATEID>/', methods=['GET', 'POST'])
   def arenas_page_update(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("""SELECT ID, ArenaName, ArenaBuiltDate, ArenaCity, ArenaCapacity FROM ARENAS WHERE ID = %s""", (int(UPDATEID),))
       connection.commit()
       return render_template('arenas_edit.html', arenas = cursor)

   @app.route('/arenas/UPDATE/<int:UPDATEID>/APPLY', methods=['GET', 'POST'])
   def arenas_page_apply(UPDATEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       new_name = request.form['name']
       new_date = request.form['built-date']
       new_city = request.form['city']
       new_capacity = request.form['capacity']
       query = """UPDATE ARENAS SET ArenaName = '%s', ArenaBuiltDate = %d, ArenaCity = '%s', ArenaCapacity = %d WHERE ID = %d""" % (new_name, int(new_date), new_city, int(new_capacity), int(UPDATEID))
       cursor.execute(query)
       connection.commit()
       return redirect(url_for('arenas_page'))
|
In this code, inserted values before can be updated in the new opened page.
|

**Delete Function**


.. code-block:: python

   @app.route('/arenas/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def arenas_page_delete(DELETEID):
           connection = dbapi2.connect(app.config['dsn'])
           cursor = connection.cursor()


           cursor.execute("""DELETE FROM ARENAS WHERE ID = %s""", (int(DELETEID),))
           connection.commit()
           return redirect(url_for('arenas_page'))

|
Here, a arena which is wanted to be removed can be remove.
|
