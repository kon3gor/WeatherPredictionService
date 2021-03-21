from app.main import app
from app/tests import unit

def runTests():
    unti.testGetCityById()
    unit.testGetDayRange()

if __name__ == "__main__":
        app.run()
        runTests
