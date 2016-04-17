from flask import render_template, flash, redirect, url_for, request, abort
from  werkzeug.debug import get_current_traceback
from app import app
from sentiment import *
from .forms import *
import twilio.twiml
from twilio.rest import TwilioRestClient
from collections import deque

ACCOUNT_SID = "AC01fe30b094e3251e3f48f0acb4853310"
AUTH_TOKEN = "47c5f4501af1693a8ecfdcd887aa2632"
payload = ''

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

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
	last_text = messages.popleft().body
	list_of_tuples = get_sent_tuples(parse_string(str(last_text)))
	print list_of_tuples
	my_chords = analyze_tuples(list_of_tuples)
	print my_chords
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
 
@app.errorhandler(500)
def internal_error(error):
  return "500 Internal Error"

@app.errorhandler(404)
def not_found(error):
	return "404 Error: Page not found", 404


