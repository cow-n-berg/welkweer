import sys

# We use a custom location
sys.path.append("/usr/share/harbour-welkweer/python/")
import buienradar
import moon


def get_moon_phase():

    return moon.get_moon_phase()


def get_globaal_weerinfo():

    return buienradar.globaal_weer()


def get_lokaal_weerinfo(stationnr):

    return buienradar.lokaal_weer(stationnr)


def get_stations_weerinfo():

    return buienradar.get_stations()


def get_forecast_weer():

    return buienradar.forecast_weer()


def get_forecast_rain(latitude, longitude):

    return buienradar.forecast_rain(latitude, longitude)
