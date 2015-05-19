# Team 9    (Adelaide)
# 
# Jun Jen CHAN    (341759)
# Daniel TEH    (558424)
# Tou LEE    (656128)
# David MONROY    (610346)
# Jaime MARTINEZ    (642231)

## Tweet harvester - Streaming API
##
## The city of Adelaide was divided in to two regions, north and south
## Further divisions were not necessary as the city did not receive enough daily
## volume to warrant working around API rate limits (the rate limit was never
## reached).
##
## Daniel Teh
import tweepy, json
from tweetstore import TweetStore
import time
import datetime
import sys

if len(sys.argv) < 3 : 
    print "ERROR: Please enter 2 arguments! (harvester-stream.py <region> <API_key>)"
    sys.exit()
else :
    # use bboxfinder.com to figure out bounding boxes lat/long coordinates
    # DO NOT USE GOOGLE MAPS! (coordinates are flipped)
    if sys.argv[1] == "north" :
        region = "North"
        coordinates = [138.213501,-34.953493,139.070435,-34.492975]
    elif sys.argv[1] == "south" :
        region = "South"
        coordinates = [138.213501,-35.395767,139.070435,-34.953493]
    else :
        print "ERROR: Please enter either 'north' or 'south' as <region>"
        sys.exit()

    # OAuth Keys (DON'T GET US BANNED PLEASE)
    if sys.argv[2] == "daniel" :
        # Daniel's personal twitter account key (used for couchNorth Development)
        API_keys = "Daniel's"
        consumer_key = "pSFHu1r2xAbqtbOsVvOU5vuFP"
        consumer_key_secret = "hjMn6oCPCyBUanidBwAImXX051ILf1JVhrW4IO268qZS00IFvI"
        access_token = "19472785-vQJRKwqBNuOMs1s5AwTzv3wFWQlqtjeIflj5rNuyy"
        access_token_secret = "R88rhzJBF3Rr85HDHn5kMKRkSmOEGKLJAO4mDrtK2ic7C"
    elif sys.argv[2] == "jun" :
        API_keys = "Jun Jen's"
        # Jun's personal twitter account key (used for couchSouth Development)
        consumer_key = "oUhOvqzIA8eOKUqF9aop3o0cr"
        consumer_key_secret = "srTmktMLMgRlWsP8vjO5NOgmLuk1UrBYxdyUrWPvy7iW2fbIpb"
        access_token = "3181667162-nj1ISYIF058pZ4q7WVJFTdCRg49IhSErPCiW0fd"
        access_token_secret = "J53YpiAF2WAXmLbnPgrelLppM7xOchRw8DXWJMJ8NeCrD"
    elif sys.argv[2] == "jimmy" :
        API_keys = "Jimmy's"
        # Jimmy's personal twitter account key (used for couchNorth Deployment)
        consumer_key = "Vuce63dPcOgS0o3sCMk0IrPTh"
        consumer_key_secret = "QMBdwW2fil4nRr815RRc32G7yTfDQvF4imjjg81cwk6vI2qvip"
        access_token = "46279225-DvynAIpVfLIuNVZZZ6a7LXXU4u1wRuUmv5vj8PmIO"
        access_token_secret = "9FhKfoE9j4fbFCv5GD2aU6AX05mc9XAMit5wOFt3hnSPx"
    elif sys.argv[2] == "david" :
        API_keys = "David's"
        # David's personal twitter account key (used for couchSouth Deployment)
        consumer_key = "Jgu6HGiLr8lZCvRLeCxuRNphO"
        consumer_key_secret = "TRpm5QNjMeTIemwO2S8QrTT3vv5DHjvNnUseShm7Oniey8w9xm"
        access_token = "3184873568-KAaeFPKVhXEVorENkK59mZBsmZVZfROCbppJzPt"
        access_token_secret = "VV2slmCU1a0Ne3BDlkSv6MxU9cWb5OPYp5V5KAihTDJVS"
    else :
        print "ERROR: Please enter either 'daniel', 'jun', 'jimmy' or 'david' as <API_keys>"
        sys.exit()

storage = TweetStore('tweets_adelaide')

## Init OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

## Main
api = tweepy.API(auth)
print "Interface set up.."
            
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        if data[0] == "4":
            datetime.datetime.now().time()
            time.sleep(900)
            print "Error.. sleeping for 15 minutes"
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
    print "Streaming tweets from Adelaide "+region+" using "+API_keys+" Twitter API keys"
    print "*"*78
    try:
        stream.filter(locations=coordinates)
    except Exception as e:
        print e
        start()
    
start()
 




