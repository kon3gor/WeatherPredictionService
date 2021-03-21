from flask import Flask
from app import utils
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/getPredictionForDay/<city>/<day>')
def getPredictionForDay(day, city):
    assert day == request.view_args['day']
    assert city == request.view_args['city']
    result = utils.predictForDay(day, city)
    return json.dumps(result)

@app.route('/getPredictionForMonth/<city>/<month>')
def getPredictionForMonth(month, city):
    assert month == request.view_args['month']
    assert city == request.view_args['city']
    result = utils.predictForMonth(month, city)
    return json.dumps(result)

@app.route('/getPredictionForYear/<city>/')
def getPredictionForYear(year, city):
    assert year == request.view_args['year']
    result = utils.predictForYear(city)
    return json.dumps(result)
