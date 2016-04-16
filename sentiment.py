import os 
import subprocess
import json

query = str(raw_input('Input text: '))

url = 'http://text-processing.com/api/sentiment/'
text = '"text=%s"' % (query)
command = 'curl -d ' + text + ' ' + url

response = subprocess.check_output([command], shell=True)
data = json.loads(response)

neg = data['probability']['neg']
pos = data['probability']['pos']
neutral = data['probability']['neutral']

print(neg, pos, neutral)