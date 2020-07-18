from app import app
from app.forms import WeatherForm
from flask import render_template, redirect, url_for, flash
import requests


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WeatherForm()
    if form.validate_on_submit():
        flash(f'You entered {form.city.data}')
        return redirect(url_for('index'))
    else:
        flash(f'{form.city.data} not valid')
    return render_template('index.html', title='test1', form=form)



