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
		# print res.content
		try:
			print "Error Occurred: " + str(parsed_json["errors"])
			print "With code: " + str(parsed_json["errors"][0]["code"])
			return
		except:
			userids = []
			userids_json = parsed_json["ids"]
			for userid in userids_json:
				userids.append(userid)
			return userids

	#Writes unique values to specified file, each value in new line.
	def getNewFollowers(self):
		old_followers = []
		new_followers = []
		followers = self.getFollowers(-1, 5000, "mayankrajoria")
		if len(followers) == 0:
			print "No Followers"
			return

		try:
			followers_file = open(self.BOT_OPTIONS['FOLLOWERS_FILE'], 'a+')
		except:
			print "Error reading followers file.\n"

		print "Old Followers:"
		followers_file.seek(0, 0)
		old_follower_lines = followers_file.readlines()
		for old_follower in old_follower_lines:
			print "   " + old_follower[:-1]
			old_followers.append(old_follower[:-1])

		print "New Followers:"
		for follower in followers:
			if not str(follower) in old_followers:
				self.sendMessage(follower)
				new_followers.append(follower)
				followers_file.write(str(follower) + "\n")
				print "   " + str(follower)

	def sendMessage(self, userid):
		url = 'https://api.twitter.com/1.1/direct_messages/new.json'
		res = requests.post(url, data = {'text':'Hi, thanks for the follow!', 'user_id':userid}, auth = self.auth)
		print res.content



aBot = Bot()
aBot.getNewFollowers()
