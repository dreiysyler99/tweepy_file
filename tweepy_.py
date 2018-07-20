import sys  
import tweepy 
from tweepy import Stream
import json

from tweepy.streaming import StreamListener

consumer_key = 'eSv5kBortS7TLmAMPh8QcUWz6'
consumer_secret = '8B8uJ6y1QgjP3q5YEdjAPncuec5Tqi3IEfYUKlNLjFnfZG824O'
access_token = '1018809514982821888-Q9e290OBYdUZn61vneC46SpXkLlSLv'
access_secret = 'aMBeA8csZ6WSLRbLDQdjDfoV4wkmV7wTapTEUdr0pfXoF'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth)



class listener(tweepy.StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        #if 'globalcode' in tweet['text'].lower():
        
        print("-----------------------------------------------------------------------------")   
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))
        print("----------------------------------------------------------------------------") 
        
    def on_error(self, status):
        print status
#twitterStream = tweepy.streaming.Stream(auth, Listener(api))
twitterStream = tweepy.Stream(auth, listener()) 
#twitterStream.filter(follow=["order"])
#twitterStream.userstream(encoding='utf8')
twitterStream.filter( languages = ['en'],follow = ['1019577698409156608','190379238','201913251','764155961305100288'], track = ['%s accident_ghana %s ','%s  fireoutbreak_ghana %s ','%s  traffic_ghana %s ','%s armedrobbery_ghana %s ', '%s robbery_ghana %s ', '%s flood_ghana %s ', '%s heavy rainfall_ghana %s ' ], locations = [-0.327867,6.011559,-0.215981,6.214282],async=True)
