from flask import render_template, flash, redirect, url_for, request, abort, send_from_directory
from  werkzeug.debug import get_current_traceback
from app import app
from sentiment import *
from .forms import *
from secret import *
import twilio.twiml
import requests
from twilio.rest import TwilioRestClient
from collections import deque

client = TwilioRestClient(account_sid, auth_token)
phone_number = ''

@app.route('/', methods=['GET', 'POST'])
def index():
	form = StringForm()
	user_str = ''
	ratings_data = ''
	pos = ''
	neg = ''
	neutral = ''

	if form.validate_on_submit():
		user_str = str(form.textinput.data)
		ratings_data = get_ratings(user_str)
		pos = ratings_data['probability']['pos']
		neg = ratings_data['probability']['neg']
		neutral = ratings_data['probability']['neutral']

	return render_template('index.html', ratings_data=ratings_data, pos=pos, neg=neg, neutral=neutral, form=form)

@app.route("/message", methods=['GET', 'POST'])
def message():
	#body_mes = client.messages.Body
	resp = twilio.twiml.Response()
	resp.message("Thanks, expect a call soon!")
	messages = deque(client.messages.list())
	last_message = messages.popleft()
	last_text = last_message.body
	phone_number = last_message.from_
	f = open('phonenumber.txt', 'w')
	f.write(phone_number)
	list_of_tuples = get_sent_tuples(parse_string(str(last_text)))
	my_chords = analyze_tuples(list_of_tuples)
	return redirect("/makecall") 

@app.route("/makecall", methods=['GET', 'POST'])
def makecall():
	f = open('phonenumber.txt', 'r')
	phone_number = f.read()
	print "whats up"
	call = client.calls.create(url="http://twimlbin.com/23667f37ab8451dbb3223f51d2248f21",
		to=phone_number,
		from_="+16307556548")
	return "working"

if __name__ == "__main__":
    app.run(debug=True)
 
@app.errorhandler(500)
def internal_error(error):
  return "500 Internal Error"

@app.errorhandler(404)
def not_found(error):
	return "404 Error: Page not found", 404


