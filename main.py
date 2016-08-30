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

	def getFollowers(self, cursor = -1, count = 5000, name = "mayankrajoria"):
		url = 'https://api.twitter.com/1.1/followers/ids.json?cursor='+str(cursor)+'&screen_name=mayankrajoria&count='+str(count)
		print 'URL: '+url
		res = requests.get(url, auth = self.auth)

		parsed_json = json.loads(res.content)
		print res.content
		try:
			print "Error Occurred: " + parsed_json["errors"]
			print "With code: " + parsed_json["errors"][0]["code"]
			return
		except:
			userids = parsed_json["ids"]
			return userids

aBot = Bot()
print aBot.getFollowers(-1, 5, "mayankrajoria")

while(False):
	url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=mayankrajoria&count=5000'

	res = requests.get(url, auth = auth)

	parsed_json = json.loads(res.content)

	print parsed_json

	time.sleep(10)