from .. import utils

def testGetCityById():
    assert "Алмазный" == utils.getCityNameById(0)
    assert "Западный" == utils.getCityNameById(1)
    assert "Курортный" == utils.getCityNameById(2)

def testGetDayRange():
    assert range(1, 32) == utils.getDayRange("1")
    assert range(61, 93) == utils.getDayRange("4")
    assert range(251, 282)  == utils.getDayRange("9")
