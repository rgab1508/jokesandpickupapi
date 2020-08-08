import json
from flask import Flask

from api.jokes import get_joke_random, get_joke_top, get_joke_controversial, get_joke_rising, get_joke_new
from api.pickup import get_pickup_random, get_pickup_top, get_pickup_controversial, get_pickup_rising, get_pickup_new

app = Flask(__name__)

###### INDEX ROUTE ######
@app.route('/')
def index():
	return 'Hello from Joke & Pickup line API'


###########################
##      JOKES ROUTES     ##
###########################

@app.route('/joke/random')
def joke():
    j = get_joke_random()
    return json.dumps(j)

@app.route('/joke/new')
def joke_new():
    return json.dumps(get_joke_new())

@app.route('/joke/new/<int:limit>')
def joke_new_limit(limit):
    return json.dumps(get_joke_new(limit=limit))


@app.route('/joke/top/<string:time_filter>')
def joke_top(time_filter):
    return json.dumps(get_joke_top(time_filter))

@app.route('/joke/top/<string:time_filter>/<int:limit>')
def joke_top_limit(time_filter, limit):
    return json.dumps(get_joke_top(time_filter, limit=limit))


@app.route('/joke/controversial/<string:time_filter>')
def joke_controversial(time_filter):
    return json.dumps(get_joke_controversial(time_filter))


@app.route('/joke/controversial/<string:time_filter>/<int:limit>')
def joke_controversial_limit(time_filter, limit):
    return json.dumps(get_joke_controversial(time_filter, limit=limit))


@app.route('/joke/rising/<string:time_filter>')
def joke_rising(time_filter):
    return json.dumps(get_joke_rising(time_filter))


@app.route('/joke/rising/<string:time_filter>/<int:limit>')
def joke_rising_limit(time_filter, limit):
    return json.dumps( get_joke_rising(time_filter, limit=limit))


###########################
##  PICKUP_LINES ROUTES  ##
###########################

@app.route('/pickup/random')
def pickup():
    return json.dumps(get_pickup_random())
   

@app.route('/pickup/new')
def pickup_new():
    return json.dumps(get_pickup_new())

@app.route('/pickup/new/<int:limit>')
def pickup_new_limit(limit):
    return json.dumps(get_pickup_new(limit=limit))


@app.route('/pickup/top/<string:time_filter>')
def pickup_top(time_filter):
    return json.dumps(get_pickup_top(time_filter))

@app.route('/pickup/top/<string:time_filter>/<int:limit>')
def pickup_top_limit(time_filter, limit):
    return json.dumps(get_pickup_top(time_filter, limit=limit))


@app.route('/pickup/controversial/<string:time_filter>')
def pcikup_controversial(time_filter):
    return json.dumps(get_pickup_controversial(time_filter))


@app.route('/pickup/controversial/<string:time_filter>/<int:limit>')
def pickup_controversial_limit(time_filter, limit):
    return json.dumps(get_pickup_controversial(time_filter, limit=limit))
            


@app.route('/pickup/rising/<string:time_filter>')
def pickup_rising(time_filter):
    return json.dumps(get_pickup_rising(time_filter))


@app.route('/pickup/rising/<string:time_filter>/<int:limit>')
def pickup_rising_limit(time_filter, limit):
    return json.dumps(get_pickup_rising(time_filter, limit=limit))



app.run()
