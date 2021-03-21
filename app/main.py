from flask import Flask
from app import utils
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/getPredictionForDay/<city>/<day>')
def getPredictionForDay(city, day):
    assert day == request.view_args['day']
    assert city == request.view_args['city']
    city = int(city)
    day = int(day)
    if city < 0 or city >  12:
        return "Error"
    if day < 1 or day > 365:
        return "Error"
    result = utils.predictForDay(day, city)
    return json.dumps(result)

@app.route('/getPredictionForMonth/<city>/<month>')
def getPredictionForMonth(city, month):
    assert month == request.view_args['month']
    assert city == request.view_args['city']
    city = int(city)
    if city < 0 or city >  12:
        return "Error"
    if int(month) < 1 or int(month) > 12:
        return "Error"
    result = utils.predictForMonth(month, city)
    return json.dumps(result)

@app.route('/getPredictionForYear/<city>/')
def getPredictionForYear(city):
    assert city == request.view_args['city']
    city = int(city)
    if city < 0 or city >  12:
        return "Error"
    result = utils.predictForYear(city)
    return json.dumps(result)
