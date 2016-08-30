import requests
from requests_oauthlib import OAuth1
import json
import time

class Bot(object):

	def __init__(self):
		self.BOT_OPTIONS = {}

		options = open("OPTIONS.txt")
		for line in options.readlines():
			if line[0] in ['#', '\n']:			#Ignore comments and newline
				continue
			line_option = line.split(' ')
			print line_option
			self.BOT_OPTIONS[line_option[0]] = line_option[1][:-1]		#Ignore newline char

		self.auth = OAuth1(self.BOT_OPTIONS['CONSUMER_KEY'], self.BOT_OPTIONS['CONSUMER_SECRET'], self.BOT_OPTIONS['ACCESS_TOKEN'], 
			self.BOT_OPTIONS['ACCESS_TOKEN_SECRET'])

	def doit(self):
		url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=mayankrajoria&count=5000'
		res = requests.get(url, auth = self.auth)

		parsed_json = json.loads(res.content)
		print res.content
		print parsed_json["errors"][0]["code"]

aBot = Bot()
aBot.doit()

while(False):
	url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=mayankrajoria&count=5000'

	res = requests.get(url, auth = auth)

	parsed_json = json.loads(res.content)

	print parsed_json

	time.sleep(10)