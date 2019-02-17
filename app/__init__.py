from flask import Flask
import sqlite3
from app import lines
from app import game_stats

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(lines.bp)
app.register_blueprint(game_stats.bp)
app.config.from_object('config')