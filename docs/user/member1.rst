===========================================
Leagues, Seasons, News (Cemal Fatih Kuyucu)
===========================================

This section is for the user end only. Details on the admin panel will be given in the upcoming sections.

#######
Leagues
#######

The leagues table contains very relevant and important information to the user. When the user click on Leagues tab from
navigation panel on top, he can see latest version of the leagues table on the main block of the web page. If the user conducts
a search, the page is updated and the user can see the same table but with search results only this time.

Even though the country information of leagues page comes from the countries table only as an ID, it is printed for convenience
of user by selecting the names of the countries table as cursor also. Whenever we have a country ID, we find the name attribute of the
ID and we print that.

In Figure 1.9, we can see the leagues table before any search on the table. In Figure 1.10, we see the leagues table after there was a search on it with the search results.

.. Figure:: cemal/leaguesnosearch.png
   :width: 400pt

   Leagues table from users perspective before a search is conducted.

.. Figure:: cemal/leaguessearch.png
   :width: 400pt

   Leagues table from users perspective after a search is conducted.

#######
Seasons
#######

We thought that it was best for the database that users see the seasons of each league. To make our page more organized,
we arranged it so that when we hover on league, we see it is a link actually. Then when we click the link of league
we can see all of the seasons in that league. This is a very organized way to show since seasons have foreign key of league ID. Figure
1.11 shows the leagues table when the mouse is hovering. The text turns a different color. Figure 1.12 shows the result of the season after
the first league in the list is picked. We can have more than 1 season in a league.

.. Figure:: cemal/seasonnoclick.png
   :width: 400pt

   Leagues table with mouse hovering on top of league item. This item is a link to seasons table for that league.

.. Figure:: cemal/seasonclick.png
   :width: 400pt

   Seasons table that comes up when we click on the league item on Leagues relation.

####
News
####

The news section is one of the most important features of this web application. It can be accessed from many different parts of the
website. From the home page, user can either click on all news or click on one of the items that is scrolling on the main page.
The main page is shown in Figure 1.13. The user can click directly on an item or click on "ALL NEWS". The all news link leads to Figure 1.14.
From Figure 1.14, the user can select a news item. This will lead to Figure 1.15. Clicking on a  news item from Figure 1.13 will also lead to a
news item. In the news item in Figure 1.15, the user can see up to date news about his favorite teams. We think this will attract many viewers to our site.

.. Figure:: cemal/1.png
   :width: 400pt

   The news table that comes up on home page. The list scrolls and user can click items.

.. Figure:: cemal/2.png
   :width: 400pt

   When the user clicks on all news, user can see all of the news items.

.. Figure:: cemal/3.png
   :width: 400pt

   When user clicks a news item from the home page or from the all news items page.