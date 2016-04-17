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
	print sentences
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


chords = {'I': '[Cceg]', 'i': '[Cc_eg]', 'ii' : '[Ddfa]', 'ii6': '[Fdfa]', 'iio': '[Ddf_a]', 'iii': '[Eegb]', 'IV' : '[Ffac]', 'iv' : '[Ff_ac]', 'V' : '[Ggbd]', 'vi' : '[Aace]', 'viio' : '[Bbdf]'}

def analyze_tuples(tuple_list):
	word_chords = []
	for tuple in tuple_list:
		rating = tuple[0]
		chord = ''
		if rating > 0.91:
			chord = chords['I']
		elif rating > 0.82:
			chord = chords['IV']
		elif rating > 0.73:
			chord = chords['V']
		elif rating > 0.64:
			chord = chords['vi']
		elif rating > 0.55:
			chord = chords['ii']
		elif rating > 0.46:
			chord = chords['ii6']
		elif rating > 0.37:
			chord = chords['iii']
		elif rating > 0.28:
			chord = chords['i']
		elif rating > 0.19:
			chord = chords['iv']
		elif rating > 0.10:
			chord = chords['iio']
		else:
			chord = chords['viio']
		word_chords.append(chord)

	return word_chords
