from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'
# TODO: return dashboard page

@app.route('/speedtests/')
def speedtests():
    pass

@app.route('/servers/')
def servers():
    pass