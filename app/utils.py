import pickle
import os
import numpy as np

SRC = "/home/kon3gor/Documents/projects/temperatureLinearRegression/server/app/models/"

def getDayRange(month):
    if month == "1":
        return range(1, 32)
    elif month == "2":
        return range(32, 61)
    elif month == "3":
        return range(61, 93)
    elif month == "4":
        return range(93, 124)
    elif month == "5":
        return range(124, 156)
    elif month == "6":
        return range(156, 187)
    elif month == "7":
        return range(187, 219)
    elif month == "8":
        return range(219, 251)
    elif month == "9":
        return range(251, 282)
    elif month == "10":
        return range(282, 314)
    elif month == "11":
        return range(314, 345)
    elif month == "12":
        return range(345, 367)

def predictForDay(day, city):
    modelFile = city+"_model.sav"
    model = pickle.load(open(SRC + modelFile, "rb"))

    x = np.array([day])
    x = x.reshape(-1, 1)
    res = model.predict(x)
    return res

def predictForMonth(month, city):
    modelFile = city+"_model.sav"
    model = pickle.load(open(SRC + modelFile, "rb"))

    monthRange = list(getDayRange(month))

    x = np.array(monthRange)
    x = x.reshape(-1, 1)
    res = model.predict(x)
    return res

def predictForMonth(city):
    modelFile = city+"_model.sav"
    model = pickle.load(open(SRC + modelFile, "rb"))

    year = list(range(1, 367))

    x = np.array(year)
    x = x.reshape(-1, 1)
    res = model.predict(x)
    return res
