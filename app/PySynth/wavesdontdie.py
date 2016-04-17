import subprocess
import shutil
import os
import sys

file=""
if len(sys.argv[1])<2:
	print "Enter an abc file name"
else: 
	print "Working with your file: "+sys.argv[1]
	file=sys.argv[1]

commanda="python2 read_abc.py "+file+" 1 --syn_b"
commandb="python2 read_abc.py "+file+" 2 --syn_b"
commandc="python2 read_abc.py "+file+" 3 --syn_b"
commandd="python2 read_abc.py "+file+" 4 --syn_b"

process = subprocess.Popen(commanda.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
# process = subprocess.Popen(ren1.split(), stdout=subprocess.PIPE)
shutil.move('out.wav','1.wav')
process = subprocess.Popen(commandb.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
# process = subprocess.Popen(ren2.split(), stdout=subprocess.PIPE)
shutil.move('out.wav','2.wav')
process = subprocess.Popen(commandc.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
# process = subprocess.Popen(ren3.split(), stdout=subprocess.PIPE)
shutil.move('out.wav','3.wav')
process = subprocess.Popen(commandd.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
# process = subprocess.Popen(ren3.split(), stdout=subprocess.PIPE)
shutil.move('out.wav','4.wav')

merge12="python2 mixfiles.py 1.wav 2.wav first.wav"
merge34="python2 mixfiles.py 3.wav 4.wav second.wav"
mergefin="python2 mixfiles.py first.wav second.wav final.wav"

process = subprocess.Popen(merge12.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
process = subprocess.Popen(merge34.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
process = subprocess.Popen(mergefin.split(), stdout=subprocess.PIPE)
print process.communicate()[0]

shutil.move('final.wav', '/Users/Meg/Documents/Hackathons/uncommonhacks/app/static/final.wav')
print "moved"