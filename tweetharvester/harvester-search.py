# Team 9    (Adelaide)
# 
# Jun Jen CHAN    (341759)
# Daniel TEH    (558424)
# Tou LEE    (656128)
# David MONROY    (610346)
# Jaime MARTINEZ    (642231)

## Tweet Harvester - Search API
## 
## The twitter search api generally only allows for searches up to 1 week into the
## past when scraping for tweets.
## The decision to only use a single node for the Search API was because the city
## of Adelaide does not get enough volume to warrent several harvesters at once.
## The decision not to delve into single users timelines stems from the desire
## to keep data as unbiased.
##
## Daniel Teh
import tweepy, json
from tweetstore import TweetStore
import time
import datetime

storage = TweetStore('tweets_adelaide')

@classmethod
def parse(cls, api, raw):
	status = cls.first_parse(api, raw)
	setattr(status, 'json', json.dumps(raw))
	return status

tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse


## OAuth Keys
# Application Key
consumer_key = "kuPrFsWufTx87nCSc4HKJ6HVU"
consumer_key_secret = "ks7OQHDyAAL1SV3kUm8SSWywxUQfj2SZfXCxUB7Y8DCXQ3omxy"
# Daniel's personal twitter account key (DON'T GET ME BANNED PLEASE)
access_token = "112086608-SYYSPBrqeOCnvNP0FbvlWHycSclndFCjUM0fgRmh"
access_token_secret = "PLk9Ze50lA2mO4bWDjnRYrzGxm3euNCW9no2lOEloeK1C"

## Init OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

## Main
api = tweepy.API(auth)
print "Interface set up.."

def start():
    print "*"*78
    print "Searching tweets from Adelaide"
    print "*"*78
    # use bboxfinder.com to figure out bounding boxes lat/long coordinates
    # DO NOT USE GOOGLE MAPS! (coordinates are flipped)
    search = tweepy.Cursor(api.search,
                           geocode="-34.919719,138.570557,62.60km",
                           rpp=99,
                           result_type="recent",
                           include_entities=True,
                           wait_on_rate_limit=True,
                           lang="en").pages()
    try:
        for pages in search:
            time.sleep(5)
            for results in pages:
                try:
                    decoded = json.loads(results.json)
                    storage.save_tweet(decoded)
                except Exception as e:
                    print e
                    pass
    except Exception as e:
        print e
        pass
start()
 




