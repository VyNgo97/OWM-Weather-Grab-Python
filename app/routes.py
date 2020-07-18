from app import app
from app.forms import WeatherForm
from flask import render_template, request, redirect, url_for, flash
import requests


@app.route('/index')
def index():
    form = WeatherForm()
    if form.validate_on_submit():
        flash(f'You entered {form.city.data}')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


# @app.route('/weather')
# def weather():
    # def weatherGrab(city):
    #     try:
    #         weather_API = (
    #                 'http://api.openweathermap.org/data/2.5/weather?appid=3529ca8740c75206b4c62134c4344442&q=' + 'chicago' + '&units=imperial')

    #         data = requests.get(weather_API).json()
    #         weather_data = data['main']['temp']
    #         print('chicago' + ' Weather: \n' + str(weather_data))
    #         return str(weather_data)
    #     except KeyError as e:
    #         print("No data for {}.".format)
    # return 'temp'

