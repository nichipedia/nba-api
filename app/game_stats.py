from flask import abort
from flask import Blueprint
from flask import jsonify
import db_ops
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
            games = db_ops.get_team_stats(team)
            json = []
            for game in games:
                dictionary = {'TEAM_NAME': game[0]}
                json.append(dictionary)
            return jsonify(json)
    except KeyError:
        app.logger.error('There was no team found at %s', team)
        abort(404)