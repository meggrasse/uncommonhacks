import os 
import subprocess
import json
import unirest

def parse_string(paragraph):
	sentences = map(str.strip, paragraph.split("."))
	return sentences

def get_ratings(user_str):
	url = 'http://text-processing.com/api/sentiment/'
	text = '"text=%s"' % (user_str)
	command = 'curl -d ' + text + ' ' + url

	response = subprocess.check_output([command], shell=True)
	data = json.loads(response)

	return data


def get_sent_tuples(sentences):
	sent_tuples = []
	for sentence in sentences: 
		sent_tuple = (get_ratings(sentence)['probability']['pos'], len(sentence))
		sent_tuples.append(sent_tuple)
	return sent_tuples


def get_syllables(word):
	response = unirest.get("https://wordsapiv1.p.mashape.com/words/" + word,
  		headers={
	    "X-Mashape-Key": "Qu63G7DaJqmsh9hVz5NLmPAKTifYp1NuFLWjsnAGhHdAiNsdHo",
	    "Accept": "application/json"
  		}
	)
	return response.body