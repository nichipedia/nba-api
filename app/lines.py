from flask import abort
from flask import Blueprint
import TEAMS

bp = Blueprint('lines', __name__, url_prefix='/nba-api/rest/game')

@bp.route('/lines')
def getLeagueLines():
    return 'lines'

@bp.route('/lines/<team>')
def getTeamLines(team):
    team = team.upper()
    try:
        if TEAMS.teamsDict[team] is not None:
            return team
    except KeyError:
        app.logger.error('There was no team found at %s', team)
        abort(404)