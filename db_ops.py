from flask import g
import sqlite3

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if 'db' not in g:
        g.db = sqlite3.connect('app.db')
    return g.db

def get_team_stats(team):
    db = get_db()
    cur = db.cursor()
    t = (team,)
    cur.execute('SELECT (TEAM_NAME) FROM NBA_GAME_STATS WHERE TEAM_NAME = ?', t)
    return cur.fetchall()