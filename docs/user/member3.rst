Parts Implemented by Seyma Umutlu
=================================

General View
------------

|
In this part of the project, the main aim is to list the matches between teams and the scores of these matches.
As an addition, the information of the visitors is wanted to be obtained, so a list of these mails are kept.
|

Matches
-------

|
The matches table is to keep the track of the matches between teams. The table is made with the teams which are gotten from a different team table.
First of all, the matches table is shown the figure 3.1.1. The blank boxes under the table are for the purpose of adding a new record.
After filling the boxes, user can push the 'add new match' button and easily add a new match.
|

.. figure:: match_images/1.png
   :figclass: align-center

   figure 3.1.1

|
To delete a match, the 'delete' button at the very end of the row of the record (figure 3.1.1) that is wanted to be deleted should be clicked.

If a user wants to update a record, s/he needs to push the 'update' button at the end of the row of the record that s/he wants to change (as seen in the figure 3.1.1),
then the user will get the page in the figure 3.1.2 and when the blank boxes are filled or selected, the update operation will be done.
|

.. figure:: match_images/2.png
   :figclass: align-center

   figure 3.1.2

Scores
------

|
The scores table is to be created for keeping track of the results of the games.
This table has four attributes, two of which are the scores of first and second teams. One of the others is match ID and the last one
is a unique number that is designated by the system, ID.

Adding and deleting operations are basically the same with matches table and it can be seen in the figure 3.1.3.
|

.. figure:: scores_images/4.png
   :figclass: align-center

   figure 3.1.3

|
The update operation can be done by clicking the 'update' button which is shown in the figure 3.1.3. In the new opened page, user can enter
new scores of the matches as shown in the figure 3.1.4.
|

.. figure:: score_images/up_su.png
   :figclass: align-center

   figure 3.1.4

Maillist
--------

|
The maillist table consists of the attributes both mail and team of the visitors and assigned ID number.
The table is kept the contact information of viistors for future purposes.
Adding, deleting and updating are the same with the tables which are mentioned above and can be seen in the figures 3.1.5 and 3.1.6, respectively.
|

.. figure:: maillist_images/3.png
   :figclass: align-center

   figure 3.1.5

.. figure:: maillist_images/up_ml.png
   :figclass: align-center

   figure 3.1.6

