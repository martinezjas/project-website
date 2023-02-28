from flask import Flask, render_template, url_for
from forms import hymn_form
from requests.exceptions import HTTPError
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd3f1fdf354bc63bc3c348ddf4abd39fe'


@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='images/favicon/favicon.ico')


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/himnario', methods=['POST', 'GET'])
def himnario():
    form = hymn_form()
    if form.validate_on_submit():
        hymn_number = form.number.data
        hymn_option = form.option.data
        try:
            response = requests.get(
                'https://sdah.my.to/hymn/' + str(hymn_number), timeout=15)
            response.raise_for_status()
            json_data = response.json()
            return render_template('himnario_play.html', hymn_data=json_data, option=hymn_option)
        except HTTPError as http_err:
            return render_template('error_handle.html', message='HTTP error occurred: ' + str(http_err))
        except Exception as err:
            return render_template('error_handle.html', message='Other error occurred: ' + str(err))
    else:
        return render_template('himnario_search.html', form=form)
