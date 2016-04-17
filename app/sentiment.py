import os 
import subprocess
import json
from bs4 import BeautifulSoup #parse from html
import urllib #visit page
import re #regex
import random

def parse_string(paragraph):
	words = map(str.strip, paragraph.split(" "))
	for word in words:
		if not len(word):
			words.pop()
	print words
	return words

def get_ratings(user_str):
	url = 'http://text-processing.com/api/sentiment/'
	text = '"text=%s"' % (user_str)
	command = 'curl -d ' + text + ' ' + url

	response = subprocess.check_output([command], shell=True)

	data = json.loads(response)
	return data

def get_sent_tuples(words):
	sent_tuples = []
	for word in words: 
		rating = get_ratings(word)['probability']['pos']
		length = len(word)
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


chords = {'I': ['c', 'c', 'e', 'g'], 'i': ['C', 'c', '_e', 'g'], 'ii' : ['D','d', 'f', 'a'], 'ii6': ['F', 'd', 'f', 'a'], 'iio': ['D', 'd', 'f', '_a'], 'iii': ['E', 'e', 'g', 'b'], 'IV' : ['F', 'f', 'a', 'c'], 'iv' : ['F', 'f', '_a', 'c'], 'V' : ['G', 'g', 'b', 'd'], 'Vs': ['G', 'b', 'd', 'f'], 'vi' : ['A', 'a', 'c', 'e'], 'viio' : ['B', 'b', 'd', 'f']}

categories = {'happy' : ['ii', 'iii', 'V', 'vi'], 'sad' : ['iio', 'viio']}

def get_chords(tuple_list):
	word_count = len(tuple_list)
	music = []

	if word_count == 1 or word_count == 0:
		if tuple_list[0][0]>=0.5:
			music.append('I')
		else:
			music.append('i')
	elif word_count == 2:
		music.append('V')
		if tuple_list[1][0] >= 0.5:
			music.append('I') 
		else:
			music.append('i')
	elif word_count == 3:
		if tuple_list[0][0] >=0.5:
			music.append('I')
		else:
			music.append('i')

		music.append('V')

		if tuple_list[2][0]>=0.5:
			music.append('I')
		else:
			music.append('i')
	elif word_count == 4:
		if tuple_list[0][0] >=0.5:
			music.append('I')
		else:
			music.append('i')

		if tuple_list[1][0] >=0.5:
			music.append('IV')
		else:
			music.append('iv')

		music.append('V')

		if tuple_list[3][0] >=0.5:
			music.append('I')
		else:
			music.append('i')
	else: 
		if tuple_list[0][0] >=0.5:
			music.append('I')
		else:
			music.append('i')
		for count in range(1, -3):
			if tuple_list[count][0] >=0.5:
				random.choice(categories['happy'])
			else:
				random.choice(categories['sad'])
		if tuple_list[-3][0] >=0.5:
			music.append('IV')
		else:
			music.append('iv')
		music.append('V')
		if tuple_list[-1][0] >=0.5:
			music.append('I')
		else:
			music.append('i')
	return music

def simpleasabc(muzik):
	"""transforms roman numeral chords to an abc file"""
	s=""
	print "found"
	for i in range(1,5):
		s=s+"X: %d\nT: callback\nC: uncommonhax\nM: 1/4\nL: 1/4\nK: C\nQ: 1/4=120\n|"%i
		#s=s+"| C A F G |\n\n" #placeholder- this works
		count=0
		for note in muzik:
			s=s+" "+chords[note][i-1]
			count=count+1
			if count == 4:
				s=s+" |"
				count=0
		if count!=0:
			s=s+" z"+str(4-count)+" |"
		s=s+'\n\n'
	return s

