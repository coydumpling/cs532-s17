# Import the necessary methods from different libraries
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "721752096169705476-M8XjTgLwx23Dv5wFn7QwSyQJywvMTFI"
access_token_secret = "aiaYQEY5Tg9KIu17OmJFt9ikZmpjmwv69Zh13CfobJSMy"
consumer_key = "fyZD1WdvbYU72CZjQf5ynv1xh"
consumer_secret = "Uqs3JNunlwm8cFJ1d41TB2BGq3j4LS1IpEnDi1BlUbwvKGpnRM"

# Accessing tweepy API
# api = tweepy.API(auth)

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        # resource: http://code.runnable.com/Us9rrMiTWf9bAAW3/how-to-stream-data-from-twitter-with-tweepy-for-python
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # resource: http://socialmedia-class.org/twittertutorial.html
        # Print each tweet in the stream to the screen
        # Here we set it to stop after getting 1000 tweets.
        # You don't have to set it to stop, but can continue running
        # the Twitter API to collect data for days or even longer.
        count = 1000

        for url in decoded["entities"]["urls"]:
            count -= 1
            print "%s" % url["expanded_url"] + "\r\n\n"
            if count <= 0:
                break

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keyword: YouTube
    stream.filter(track=['YouTube'])
