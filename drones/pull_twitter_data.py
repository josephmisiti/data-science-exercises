import re
import sys
import datetime
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from settings import *

""" Parse out date and death count. """

MONTHS = {}
MONTHS['Apr'] = 4
MONTHS['Aug'] = 8
MONTHS['Dec'] = 12
MONTHS['Feb'] = 2
MONTHS['Jan'] = 1
MONTHS['Jul'] = 7
MONTHS['Jun'] = 6
MONTHS['Mar'] = 3
MONTHS['May'] = 5
MONTHS['Nov'] = 11
MONTHS['Oct'] = 10
MONTHS['Sep'] = 9

REGEX_GET_NUMS = re.compile('r()')

def convert_to_datetime(thedate):
	thedate=thedate.replace(",","")
	month = MONTHS[thedate.split(" ")[0]]
	day = int(thedate.split(" ")[1])
	year  = int(thedate.split(" ")[2])
	return datetime.datetime(year=year,month=month,day=day)
	
def from_twitter(api):
	for status in api.user_timeline(screen_name='dronestream',count=1000):
		print status.text
		
def from_file(thefile='twitter.dat'):
	statuses = [line.strip() for line in open(thefile).readlines()]
	for status in statuses:
		thedate = convert_to_datetime(status.split(":")[0])
		thetext = status.split(":")[1].strip()
		print thetext
		
if __name__ == '__main__':
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	if len(sys.argv) < 2:
		print("usage: python pull_twitter_data.py <from-twitter or from-file>")
		sys.exit()
	else:
		if sys.argv[1] == 'from-twitter':
			from_twitter(api)
		else:
			from_file()
			
		
		
		
		
