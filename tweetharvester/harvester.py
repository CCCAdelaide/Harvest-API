## Tweet harvester 1.0
## Daniel Teh
import tweepy, json

## OAuth Keys
consumer_key = "pSFHu1r2xAbqtbOsVvOU5vuFP"
consumer_key_secret = "hjMn6oCPCyBUanidBwAImXX051ILf1JVhrW4IO268qZS00IFvI"
access_token = "19472785-vQJRKwqBNuOMs1s5AwTzv3wFWQlqtjeIflj5rNuyy"
access_token_secret = "R88rhzJBF3Rr85HDHn5kMKRkSmOEGKLJAO4mDrtK2ic7C"

## Something
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

##
api = tweepy.API(auth)
print "Interface set up.."

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        
        print '@%s: %s' %(decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
#        print data
        print ""
        return True
    def on_error(self,status):
        print status

l = StdOutListener()
stream = tweepy.Stream(auth,l)
print "*"*78
print "Getting tweets from Melbourne CBD.."
print "*"*78
#stream.filter(locations=[-79.72452163696289,43.37158360778362,-79.72297668457031,43.527517 7007501])
stream.filter(locations=[-37.847579,144.923850,-37.785335,145.001785])

#public_tweets = api.home_timeline()
#for tweet in public_tweets: 
#    print tweet.text
    