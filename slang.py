import urllib
import json

query = str(raw_input('What word do you want to search? '))
url = 'http://api.urbandictionary.com/v0/define?term=%s' % (query)

response = urllib.urlopen(url)
data = json.loads(response.read())

# Takes in the first definition result of all urban dictionary results
definition = data['list'][0]['definition']

print query + ': ' + definition