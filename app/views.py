from flask import render_template, flash, redirect, url_for, request, abort
from  werkzeug.debug import get_current_traceback
from app import app
from sentiment import *
from .forms import *
from secret import *
import twilio.twiml
from twilio.rest import TwilioRestClient
from collections import deque

client = TwilioRestClient(account_sid, auth_token)
song_url = 'http://ocrmirror.org/files/music/remixes/Street_Fighter_2_Guile%27s_Theme_Goes_with_Metal_OC_ReMix.mp3'

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
	# print list_of_tuples
	list_of_chords=get_chords(list_of_tuples)
	# print list_of_chords
	abcstring=simpleasabc(muz)
	print abcstring
	myabcfile=open("abcsheet.abc.txt",'w')
	myabcfile.write(abcstring)
	myabcfile.close()
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
 
@app.errorhandler(500)
def internal_error(error):
  return "500 Internal Error"

@app.errorhandler(404)
def not_found(error):
	return "404 Error: Page not found", 404


