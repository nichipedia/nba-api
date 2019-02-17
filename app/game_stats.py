from flask import abort
from flask import Blueprint
import TEAMS

bp = Blueprint('stats', __name__, url_prefix='/nba-api/rest/game')

@bp.route('/stats')
def getAllTeamsStats():
    return "All the teams!"

@bp.route('/stats/<team>')
def getTeamStats(team):
    team = team.upper()
    try:
        if TEAMS.teamsDict[team] is not None:
            return team
    except KeyError:
        app.logger.error('There was no team found at %s', team)
        abort(404)