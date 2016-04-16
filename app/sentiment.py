import os 
import subprocess
import json
from bs4 import BeautifulSoup #parse from html
import urllib #visit page
import re #regex



def parse_string(paragraph):
	sentences = map(str.strip, paragraph.split("."))
	for sentence in sentences:
		if not len(sentence):
			sentences.pop()
	return sentences

def get_ratings(user_str):
	url = 'http://text-processing.com/api/sentiment/'
	text = '"text=%s"' % (user_str)
	command = 'curl -d ' + text + ' ' + url

	response = subprocess.check_output([command], shell=True)

	data = json.loads(response)
	print data

	return data

def get_sent_tuples(sentences):
	sent_tuples = []
	print sentences
	for sentence in sentences: 
		rating = get_ratings(sentence)['probability']['pos']
		length = len(sentence)

		
		sent_tuple = (rating, length)
		sent_tuples.append(sent_tuple)

	return sent_tuples

def get_syllables(word):
	opener=urllib.FancyURLopener({})
	url="http://www.syllablecount.com/syllables/"+str(word)
	openerFile = opener.open(url)
	htmlFile = openerFile.read()
	soup = BeautifulSoup(htmlFile,"html.parser")
	rawdata = soup.find(id="ctl00_ContentPane_paragraphtext")
	# print rawdata
	syllablesreg=re.compile(r'\d syllables',re.DOTALL)
	numsyll=syllablesreg.search(str(rawdata))
	print int(numsyll.group()[0])

