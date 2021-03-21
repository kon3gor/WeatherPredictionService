from app import app
from flask import request
from . import utils


@app.route('/')
def index():
    return "Hello world"

@app.route('/getPredictionForDay/<city>/<day>')
def getPredictionForDay(day, city):
    assert day == request.view_args['day']
    assert city == request.view_args['city']
    result = utils.predictForDay(day, city)
    return str(result)

@app.route('/getPredictionForMonth/<city>/<month>')
def getPredictionForMonth(month, city):
    assert month == request.view_args['month']
    assert city == request.view_args['city']
    result = utils.predictForMonth(month, city)
    return str(result)

@app.route('/getPredictionForYear/<city>/')
def getPredictionForYear(year, city):
    assert year == request.view_args['year']
    result = utils.predictForYear(city)
    return str(result)
