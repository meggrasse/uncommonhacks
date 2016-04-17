import subprocess
import shutil
import os
import sys

file=""
if sys.argv[1]==None:
	print "Enter an abc file name"
else: 
	print "Working with your file: "+sys.argv[1]
	file=sys.argv[1]

commanda="python2 read_abc.py "+file+" 1 --syn_b"
# ren1="ren out.wav 1.wav"
commandb="python2 read_abc.py "+file+" 2 --syn_b"
# ren2="ren out.wav 2.wav"
commandc="python2 read_abc.py "+file+" 3 --syn_b"
# ren3="ren out.wav 3.wav"

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

merge12="python2 mixfiles.py 1.wav 2.wav first.wav"
merge123="python2 mixfiles.py first.wav 3.wav final.wav"

process = subprocess.Popen(merge12.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
process = subprocess.Popen(merge123.split(), stdout=subprocess.PIPE)
print process.communicate()[0]