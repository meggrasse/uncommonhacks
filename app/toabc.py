import random

myabcfile=open("abcsheet.abc.txt",'w')

chords = {'I': ['c', 'c', 'e', 'g'], 'i': ['C', 'c', '_e', 'g'], 'ii' : ['D','d', 'f', 'a'], 'ii6': ['F', 'd', 'f', 'a'], 'iio': ['D', 'd', 'f', '_a'], 'iii': ['E', 'e', 'g', 'b'], 'IV' : ['F', 'f', 'a', 'c'], 'iv' : ['F', 'f', '_a', 'c'], 'V' : ['G', 'g', 'b', 'd'], 'Vs': ['G', 'b', 'd', 'f'], 'vi' : ['A', 'a', 'c', 'e'], 'viio' : ['B', 'b', 'd', 'f']}
categories = {'happy' : ['ii', 'iii', 'V', 'vi'], 'sad' : ['iio', 'viio']}
#the below tuplist is just a tester
tuplist=[(0.6,1),(0.5,1),(0.9,1),(0.2,1),(0.6,1),(0.6,1),(0.9,1),(0.3,1),(0.5,1)]
def get_chords(tuple_list):
	"""chooses roman numeral chords based on text input"""
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
		midseg=tuplist[1:-3]
		for item in midseg:
			if item[0] >=0.5:
				music.append(random.choice(categories['happy']))
			else:
				music.append(random.choice(categories['sad']))
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

muz=get_chords(tuplist)
print muz
print chords
# got the chords boy
# now make it a .abc lad

def simpleasabc(muzik):
	"""transforms roman numeral chords to an abc file"""
	s=""
	for i in range(1,5):
		s=s+"X: %d\nT: callback\nC: uncommonhax\nM: 1/4\nL: 1/4\nK: C\nQ: 1/4=120\n| "%i
		#s=s+"| C A F G |\n\n" #placeholder- this works
		for note in muzik:
			s=s+chords[note][i-1]+" "
		s=s+'|\n\n'
	return s

abcstring=simpleasabc(muz)
print abcstring
myabcfile.write(abcstring)
myabcfile.close()
#works in pysynth with the placeholder