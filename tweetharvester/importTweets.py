import json, csv
from tweetstore import TweetStore

filename = 'adelaide.csv'

storage = TweetStore('tweets_adelaide')

i = 0
with open(filename, 'rb') as tweetfile
    reader = csv.DictReader(tweetfile)
    for tweet in reader
        decoded = json.loads(tweet['value'])
        storage.save_tweet(decoded)
        i+=1
print ("Inserted %d tweets" % i)