import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app

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
