from unittest.mock import patch
import unittest
import grabbingTheWeather
import requests

class TestWeather(unittest.TestCase):

    def test_weatherGrab(self):

        weather_API = 'http://api.openweathermap.org/data/2.5/weather?appid=3529ca8740c75206b4c62134c4344442&q=chicago&units=imperial'
        data = requests.get(weather_API).json()
        weather_data_test = data['main']['temp']
        expected_weather_data = weather_data_test

        with patch('builtins.input', side_effects=['chicago']):
            grabbingTheWeather.weatherGrab('chicago')
            print('Success')

if __name__ == '__main__':
    unittest.main()
