from pyowm import OWM, exceptions
from socket import gethostbyname, create_connection
from sys import path

path.append('..\\interface\\')
import window as w


def showWeather():
    try:
        create_connection((gethostbyname('www.google.com'), 80), 2).close()

        w.labelWeather['text'] = 'Обработка запроса...'
        w.root.update()

        city = w.entryPlace.get()
        weather = owm.weather_at_place(city).get_weather()
        forecast = owm.daily_forecast(city, limit=2) \
            .get_forecast().get_weathers()

        w.labelWeather['text'] = 'Температура: {0} °C' \
                                 '\nВетер: {1} м/с' \
                                 '\nПогода:\n{2}' \
                                 '\nЗавтра:\n{3}' \
                                 '\nПослезавтра:\n{4}'.format(
            weather.get_temperature('celsius')['temp'],
            weather.get_wind()['speed'],
            weather.get_detailed_status().capitalize(),
            forecast[0].get_detailed_status().capitalize(),
            forecast[1].get_detailed_status().capitalize()
        )
    except OSError:
        w.labelWeather['text'] = 'Произошла сетевая\nошибка!'
    except exceptions.api_response_error.NotFoundError:
        w.labelWeather['text'] = 'Вы ввели неверное\nназвание города!'
    except exceptions.api_call_error.APICallError:
        w.labelWeather['text'] = 'Произошла ошибка\nпри обработке запроса!'


owm = OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru')
