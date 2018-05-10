import pyowm
import config


def get(city):
    owm = pyowm.OWM(API_key=config.api_key, language='en')

    obs = owm.weather_at_place(city)

    w = obs.get_weather()

    return w, obs.get_location().get_country()


def format_weather(weather):
    t = weather.get_temperature(unit='celsius')
    ans = dict()
    ans['Current temperature'] = t['temp']
    ans['Maximum temperature'] = t['temp_max']
    ans['Minimum temperature'] = t['temp_min']
    ans['Status'] = weather.get_detailed_status()
    ans['Sunrise'] = weather.get_sunrise_time('iso')
    ans['Sunset'] = weather.get_sunset_time('iso')
    ans['Humidity'] = weather.get_humidity()
    ans['Pressure'] = int(weather.get_pressure()['press'] / 1.3332239)
    ans['Wind'] = weather.get_wind()['speed']
    return ans


def info(city):
    t_city = city
    if city == 'Сочи':
        city = 'Sochi'

    raw_w, country = get(city)
    w = format_weather(raw_w)
    response = 'City: ' + str(t_city)
    if ',' not in t_city:
        response += ',' + country
    response += '\n'
    response += str(w['Status']) + '\n'
    response += 'Temperature: '
    if w['Current temperature'] > 0:
        response += '+'
    response += str(w['Current temperature']) + '\n'
    response += 'Wind: ' + str(w['Wind']) + ' m/s\n'
    response += 'Pressure: ' + str(w['Pressure']) + ' mmhg\n'
    response += 'Sunrise: ' + str(w['Sunrise']) + '\n'
    response += 'Sunset: ' + str(w['Sunset']) + '\n'
    return response, str(w['Status'])
