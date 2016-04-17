import subprocess
import shutil
import os

commanda="python2 read_abc.py 4chord.abc.txt 1 --syn_b"
# ren1="ren out.wav 1.wav"
commandb="python2 read_abc.py 4chord.abc.txt 2 --syn_b"
# ren2="ren out.wav 2.wav"
commandc="python2 read_abc.py 4chord.abc.txt 3 --syn_b"
# ren3="ren out.wav 3.wav"
commandd="python2 read_abc.py 4chord.abc.txt 4 --syn_b"
# ren4="ren out.wav 4.wav"

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
# process = subprocess.Popen(ren4.split(), stdout=subprocess.PIPE)
shutil.move('out.wav','4.wav')

merge12="python2 mixfiles.py 1.wav 2.wav first.wav"
merge34="python2 mixfiles.py 3.wav 4.wav second.wav"
final="python2 mixfiles.py first.wav second.wav final.wav"

process = subprocess.Popen(merge12.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
process = subprocess.Popen(merge34.split(), stdout=subprocess.PIPE)
print process.communicate()[0]
process = subprocess.Popen(final.split(), stdout=subprocess.PIPE)
print process.communicate()[0]