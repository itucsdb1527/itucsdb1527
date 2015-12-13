import psycopg2 as dbapi2

from flask import render_template
from flask import redirect
from flask import request
from flask.helpers import url_for
from config import app


@app.route('/news')
def news_page():
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()
    query = "SELECT ID, News_Title FROM NEWS ORDER BY ID DESC"
    cursor.execute(query)
    return render_template('news.html', news=cursor)

@app.route('/news/<int:NEWSID>', methods=['GET', 'POST'])
def news_details_page(NEWSID):
    connection = dbapi2.connect(app.config['dsn'])
    cursor = connection.cursor()
    query = "SELECT News_Title, News_Details, News_Picture FROM NEWS WHERE ID = %d" % int(NEWSID)
    cursor.execute(query)
    return render_template('news_detail.html', news = cursor)
