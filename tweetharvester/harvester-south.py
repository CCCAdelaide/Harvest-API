## Tweet harvester 1.0
## Daniel Teh
import tweepy, json
from tweetstore import TweetStore

storage = TweetStore('test_db')

## OAuth Keys
# Application Key
consumer_key = "oUhOvqzIA8eOKUqF9aop3o0cr"
consumer_key_secret = "srTmktMLMgRlWsP8vjO5NOgmLuk1UrBYxdyUrWPvy7iW2fbIpb"
# Jun's personal twitter account key (DON'T GET ME BANNED PLEASE)
access_token = "3181667162-nj1ISYIF058pZ4q7WVJFTdCRg49IhSErPCiW0fd"
access_token_secret = "J53YpiAF2WAXmLbnPgrelLppM7xOchRw8DXWJMJ8NeCrD"

## Init OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

## Main
api = tweepy.API(auth)
print "Interface set up.."
            
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        storage.save_tweet(decoded)
        print '@%s: %s' %(decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ""
        return True
    def on_error(self,status):
        print status

l = StdOutListener()
stream = tweepy.Stream(auth,l)

def start():
    print "*"*78
    print "Getting tweets from Adelaide"
    print "*"*78
    # use bboxfinder.com to figure out bounding boxes lat/long coordinates
    # DO NOT USE GOOGLE MAPS! (coordinates are flipped)
    try:
        stream.filter(locations=[138.213501,-35.395767,139.070435,-34.953493])
    except Exception as e:
        print e
        start()
    
start()
 




