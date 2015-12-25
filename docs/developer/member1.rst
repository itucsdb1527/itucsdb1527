===========================================
Leagues, Seasons, News (Cemal Fatih Kuyucu)
===========================================
#######
Leagues
#######
****************
Class Definition
****************

A league is defined to have a name and an ID. The ID increases serially but no one sees it. It's important if there is a
foreign key or if there is something to be deleted or updated. The ID handling happens in the background. The definition is given
in code block in Listing 2.1.

.. code-block:: python
   :caption: Class definition of leagues.
   :name: admin.py--Define leagues

   query = """DROP TABLE IF EXISTS LEAGUES CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE LEAGUES (
                    ID SERIAL PRIMARY KEY,
                    League_Name VARCHAR NOT NULL,
                    Country_ID INTEGER NOT NULL,
                    FOREIGN KEY (Country_ID) REFERENCES COUNTRIES(ID) ON DELETE CASCADE ON UPDATE CASCADE
                    )"""

*******
Methods
*******

The leagues class has four main methods. We can insert, update, delete and search. There is also an init function.

----
Init
----

In Listing 2.2 we have the initialization league. They are SQL queries and when they are executed new leagues are added.
Figure 2.2 shows the leagues that are first initialized.

.. code-block:: python
   :caption: InitDB definition of leagues.
   :name: admin.py--InitDB leagues

    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,Country_ID) VALUES ('Aroma Erkekler Voleybol Ligi',1)"""
    cursor.execute(query)
    query = """INSERT INTO LEAGUES (League_Name,Country_ID) VALUES ('Premier Lig',2)"""
    cursor.execute(query)

.. Figure:: cemal/initleague.png
   :width: 400pt

   After InitDB for Leagues.

------
Insert
------

The insert part is on admin panel because this is not a user activity. For get part the function shows the relation's table. The post part gives parameters for insert
SQL statement like name and country. When we execute, a new league is inserted. Listing 2.3 shows the code for this in python language. Figure 2.3 is during insert
process and Figure 2.4 is after the insert process.

.. code-block:: python
   :caption: Insert of leagues.
   :name: admin.py--Insert leagues

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

.. Figure:: cemal/insertleague.png
   :width: 400pt

   Leagues table for admin during insert.

.. Figure:: cemal/insertedleague.png
   :width: 400pt

   Leagues table for admin after insert.
------
Update
------
Listing 2.4 is the code for updating. There are two functions. The first one selects the league that has UPDATEID (which is user clicked). The next one
takes that League with ID and puts it in new page. Then new name and country come from HTML page and they are parameters for SQL Statement. Only admin user can
update a league. Figure 2.5 is the selecting process for update and 2.6 is after the update is finished.

.. code-block:: python
   :caption: Insert of leagues.
   :name: admin.py--Update leagues

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

.. Figure:: cemal/updateleague.png
   :width: 400pt

   Leagues table for admin during update.

.. Figure:: cemal/updatedleague.png
   :width: 400pt

   Leagues table for admin after update.
------
Delete
------

If the admin wants to delete a league,  he must click the delete button like in Figure 2.7. when this button is clicked, the
ID of the league goes into SQL statement as parameter and the league is deleted. The code that takes parameter and puts it in
SQL statement in python is given in Listing 2.5.

.. code-block:: python
   :caption: Insert of leagues.
   :name: admin.py--Delete leagues

   @app.route('/ADMIN/leagues/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
   def admin_leagues_page_delete(DELETEID):
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()

       cursor.execute("DELETE FROM LEAGUES WHERE ID = %s", (int(DELETEID),))
       connection.commit()
       return redirect(url_for('admin_leagues_page'))

.. Figure:: cemal/deleteleague.png
   :width: 400pt

   Leagues table for admin during delete.

------
Search
------
In the user perspective, the user can search for a league. The search option is done in the main page of leagues.
This is because normal users can want to search for leagues. The block code in Listing 2.6 shows how search happens.
If the function is type post, then the search parameter is returned from HTML site. Then it is put into SQL as a parameter to
find similar words. Figure 2.8 and 2.9 show before and after search in user perspective

.. code-block:: python
   :caption: Search for leagues.
   :name: admin.py--Search leagues

     else:
           search = request.form['search']
           query = "SELECT ID, League_Name, Country_ID FROM LEAGUES WHERE League_Name LIKE '%" + search +"%'"
           cursor.execute(query)
           connection.commit()
           return render_template('leagues.html', leagues = cursor)


.. Figure:: cemal/league.png
   :width: 400pt

   Leagues table for user perspective.

.. Figure:: cemal/leaguesearch.png
   :width: 400pt

   Leagues table after search for users perspective.

*********
Relations
*********

As can be observed from the figures of the table, the leagues table is related to the countries table. The league country information comes from the countries table.

#######
Seasons
#######
****************
Class Definition
****************

In this class, there is a season, a league and an ID. Also, the league comes from the league table. It is not possible to put a season under a league that doesn't exist.
Listing 2.7 is the definition in Python language for the seasons relation. The attributes are given in the SQL code.

.. code-block:: python
   :caption: Class definition of seasons.
   :name: admin.py--Define seasons

   query = """DROP TABLE IF EXISTS SEASONS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE SEASONS (
                    ID SERIAL PRIMARY KEY,
                    Season_Name VARCHAR NOT NULL,
                    League_ID INTEGER NOT NULL,
                    FOREIGN KEY (League_ID) REFERENCES LEAGUES(ID) ON DELETE CASCADE ON UPDATE CASCADE
                    )"""

*******
Methods
*******

The seasons function has the main initialize, insert, update, delete functions. It doesn't have a search function but we can see the seasons of each
league if we click on the seasons.

----
Init
----

In the initialize database function we insert a new season by entering the values that go into each attribute. The code in
python is given in Listing 2.8. Figure 2.10 shows the seasons table after it was initialized from admin panel.

.. code-block:: python
   :caption: InitDB definition of seasons.
   :name: admin.py--InitDB seasons

   cursor.execute(query)
    query = """INSERT INTO SEASONS (Season_Name,League_ID) VALUES ('2016 Ligi',1)"""
    cursor.execute(query)
    query = """INSERT INTO SEASONS (League_ID,Season_Name) VALUES (1,'2018 Ligi')"""
    cursor.execute(query)
    query = """INSERT INTO SEASONS (League_ID,Season_Name) VALUES (2,'2017 Ligi')"""
    cursor.execute(query)

.. Figure:: cemal/initseasons.png
   :width: 400pt

   After InitDB for Seasons.
------
Insert
------

The get method for this function selects the entire table and sends as cursors to HTML file. In HTML file, we print the entire table
for user to see. This code is very similar for both admin and user panel.
If we are not printing the table, we are adding something to the table. This can be seen in second part of Listing 2.9. We send in name and leagueID
into the SQL statement as parameters and execute query to add new season. The ID for seasons is serial so we don't take this information from  user. In
figure 2.11 we can see the seasons table after insert.

.. code-block:: python
   :caption: Insert of seasons.
   :name: admin.py--Insert Seasons

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

.. Figure:: cemal/insertseason.png
   :width: 400pt

   Seasons table for admin after insert.
------
Update
------

Like in leagues, update function has 2 parts. First part of listing 2.10 takes the update ID. We are redirected to the admin edit page for seasons.
In this page we can change the seasons values. When we click update, the new values are sent to python file as new_name and new_league_ID. These
parameters in the update SQL statement change the season that is selected by user. Figures 2.12 and 2.13 show seasons before and after update.


.. code-block:: python
   :caption: Update of seasons.
   :name: admin.py--Seasons Update

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

.. Figure:: cemal/updateseason.png
   :width: 400pt

   Seasons table for admin during update.

.. Figure:: cemal/updatedseason.png
   :width: 400pt

   Seasons table for admin after update.

------
Delete
------

To delete a season, we take the ID and send it into the python code in listing 2.11. In this code, we take the tuple with
ID equal to the delete id and we send it in as SQL parameter. The value is then deleted. This can be seen in figure 2.14.


.. code-block:: python
   :caption: Delete of seasons.
   :name: admin.py--Seasons delete

    @app.route('/ADMIN/seasons/DELETE/<int:DELETEID>', methods=['GET', 'POST'])
    def admin_seasons_page_delete(DELETEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    cursor.execute("DELETE FROM SEASONS WHERE ID = %s", (int(DELETEID),))
    connection.commit()
    return redirect(url_for('admin_seasons_page'))

.. Figure:: cemal/deleteseason.png
   :width: 400pt

   Seasons table for admin during delete.

*********
Relations
*********
The seasons table gets the league information from the leagues table. The league attribute of the seasons relation is a foreign key from the leagues id.



####
News
####

We believe that in order to attract visitors, we should display news about users favorite volleyball teams. This is why we made the news
relation.

****************
Class Definition
****************

The news class has 4 attributes. These are the ID, title, details and a picture. The code block in Listing 2.12
is the code that is used to create a news table if there is no news table.

.. code-block:: python
   :caption: Class definition of news.
   :name: admin.py--Define news

    query = """DROP TABLE IF EXISTS NEWS CASCADE"""
    cursor.execute(query)
    query = """CREATE TABLE NEWS (
                    ID SERIAL PRIMARY KEY,
                    News_Title VARCHAR NOT NULL,
                    News_Details TEXT,
                    News_Picture VARCHAR NOT NULL
                    )"""
    cursor.execute(query)

*******
Methods
*******
----
Init
----

The initialize database function for news class is very long because of the text area. This is why we will not display it here.
In Figure 2.15, we can see what the news part looks like on the admin panel. If we click a title, we can see the result in
figure 2.16. This is the editing page of the news table. In figure 2.15, we can see the update page when we click on a news
item to update. The code block in listing 2.15 shows the list of all news items in the admin news panel.

.. code-block:: python
   :caption: Listing of news.
   :name: admin.py--List news

   @app.route('/ADMIN/news')
   def admin_news_page():
       connection = dbapi2.connect(app.config['dsn'])
       cursor = connection.cursor()
       query = "SELECT ID, News_Title FROM NEWS ORDER BY ID DESC"
       cursor.execute(query)
       return render_template('admin/news.html', news=cursor)

------
Update
------
In the update section, we have the select part. This is from the news tab in admin panel. When we click on the news item
we are redirected to edit page. In edit page we can edit the attributes of a news item. When we click update, the refreshed
table comes up in the admin news tab. The first function in listing2.14 gives the selecting part of the news that we need to edit.
The second function inserts the edited values in SQL query and executes the query. After query update we are redirected to
original admin news panel and we can see updated news table. Figure 2.15 gives the news tab for admin panel. When we clidk
on a news item, we see the edit page that we are redirected to in figure 2.16.

.. code-block:: python
   :caption: Insert of news.
   :name: admin.py--Update news

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

.. Figure:: cemal/updatenew.png
   :width: 400pt

   After InitDB for News.

.. Figure:: cemal/updatenew2.png
   :width: 400pt

   After InitDB for News.

*********
Relations
*********

This table is not related to any of the other tables. This is because there can be news about many things--if we got the LeaguesID but wanted to put news
about a team, then we would need TeamID too. This is why we decided to keep it separate from everything else.

