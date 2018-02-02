from flask import Flask
from flask import jsonify
from flask import render_template

from networkmonitor import speedtest

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('dashboard.html')
# TODO: return dashboard page

@app.route('/speedtests/')
def speedtests():
    results = speedtest.get_all_speedtest_results()
    return jsonify(results)


@app.route('/servers/')
def servers():
    pass