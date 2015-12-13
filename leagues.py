import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app


@app.route('/leagues', methods=['GET', 'POST'])
def leagues_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT COUNTRIES.ID, League_Name, COUNTRIES.Name FROM LEAGUES, COUNTRIES WHERE Country_ID = COUNTRIES.ID ORDER BY Countries.Name, League_Name"
        cursor.execute(query)
        return render_template('leagues.html', leagues = cursor)
    else:
        search = request.form['search']
        query = "SELECT ID, League_Name, Country_ID FROM LEAGUES WHERE League_Name LIKE '%" + search +"%'"
        cursor.execute(query)
        connection.commit()
        return render_template('leagues.html', leagues = cursor)

@app.route('/leagues/season/<int:LEAGUEID>', methods=['GET', 'POST'])
def leagues_season_page(LEAGUEID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT SEASONS.ID, Season_Name, League_Name FROM SEASONS INNER JOIN LEAGUES ON SEASONS.LEAGUE_ID = LEAGUES.ID WHERE League_ID = %d" % int(LEAGUEID)
        cursor.execute(query)

        return render_template('season.html', seasons = cursor)
    else:
        search = request.form['search']
        query = "SELECT Season_Name, League_Name FROM SEASONS INNER JOIN LEAGUES ON SEASONS.LEAGUE_ID = LEAGUES.ID WHERE Season_Name LIKE '%" + search +"%'" #AND (League_ID = %d)" % LEAGUEID
        cursor.execute(query)
        connection.commit()
        return render_template('season.html', seasons = cursor)

@app.route('/leagues/season/<int:SEASONID>/teams', methods=['GET', 'POST'])
def list_season_team_page(SEASONID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()

    if request.method == 'GET':
        query = "SELECT Season_Name, Team_Name FROM SEASON_TEAM INNER JOIN TEAMS ON SEASON_TEAM.Team_ID = TEAMS.ID INNER JOIN SEASONS ON SEASON_TEAM.Season_ID = SEASONS.ID WHERE Season_ID = %d" % int(SEASONID)
        cursor.execute(query)

        return render_template('season_team.html', season_team = cursor)
    else:
        search = request.form['search']
        query = "SELECT Season_Name, Team_Name FROM SEASON_TEAM INNER JOIN TEAMS ON SEASON_TEAM.Team_ID = TEAMS.ID INNER JOIN SEASONS ON SEASON_TEAM.Season_ID = SEASONS.ID WHERE Team_Name LIKE'%" + search + "%'"
        cursor.execute(query)
        connection.commit()
        return render_template('season_team.html', season_team = cursor)
