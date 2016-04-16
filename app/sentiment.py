import os 
import subprocess
import json

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


