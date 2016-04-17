#!/usr/bin/python

import sys
from app.sentiment import *
from app.views import *

def main():
	if len(sys.argv) != 2:
		print "usage: ./main.py {{string}}"
		sys.exit(1)

	user_str = sys.argv[1]

	# data = get_ratings(user_str)
	# pos = data['probability']['pos']
	# neg = data['probability']['neg']
	# neutral = data['probability']['neutral']

	list_of_tuples = get_sent_tuples(parse_string(user_str))
	chords = analyze_tuples(data)
	# print chords


if __name__ == '__main__':
  main()

