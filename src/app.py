from flask import g, request, session
import time
import datetime
from flask import Flask, request, Response
from estimator import estimator
from json import loads
from dicttoxml import dicttoxml


app = Flask(__name__)


@app.route('/api/v1/on-covid-19', methods=['POST'])
def form():
    req_data = request.get_json()
    res = estimator(req_data)

    return res


@app.route('/api/v1/on-covid-19/json', methods=['POST'])
def json_form():
    req_data = request.get_json()
    res = estimator(req_data)

    return res


@app.route('/api/v1/on-covid-19/xml', methods=['POST'])
def xml_form():
    req_data = request.get_json()
    res = estimator(req_data)
    xml = dicttoxml(res)
    return xml

@app.route('/')
def index():
    return "<h1>The index page</h1>"

@app.before_request
def start_timer():
    print("start")
    g.start = time.time()
    print(g.start)


@app.after_request
def log_request(Response):
    try:
        print("nothing")
        return
        # now = time.time()
        # duration = round(now - g.start, 2)
        # print(duration)
    except TypeError:
        print("An exception occured")
        return


if __name__ == '__main__':
    app.debug = True
    app.run()
