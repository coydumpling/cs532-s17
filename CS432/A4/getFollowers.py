#coding: utf-8
import tweepy
from tweepy import OAuthHandler
import sys

def init():
    global api
consumer_key = "uIHgcJNDmmbeunAQ3PtwnB7aW"
consumer_secret = "3E15kDsBLyfIFncgxQ3Cnh6Vu6TTVsVuTa0y5nt6oIx2JVV921"
access_key="721752096169705476-M8XjTgLwx23Dv5wFn7QwSyQJywvMTFI"
access_secret="aiaYQEY5Tg9KIu17OmJFt9ikZmpjmwv69Zh13CfobJSMy"
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

file = open('TwitterFollowers.txt', 'w')

user = api.get_user("koidumpling")
print user.screen_name
print user.followers_count

lFollowers = []
for user in tweepy.Cursor(api.followers, count = 50).items():
    lFollowers.append((user.followers_count, user.screen_name))

lFollowers.sort()
for follower in lFollowers:
    print "%d - %s" % (follower[0], follower[1])
