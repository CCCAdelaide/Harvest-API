# Team 9    (Adelaide)
# 
# Jun Jen CHAN    (341759)
# Daniel TEH    (558424)
# Tou LEE    (656128)
# David MONROY    (610346)
# Jaime MARTINEZ    (642231)

import json, csv, sys
from tweetstore import TweetStore

# Python script for importing tweets from text file;
# Usage: importTweets.py *sourcefile *couchdbname

# Daniel Teh

filename = sys.argv[1]
storage = TweetStore(sys.argv[2])

i = 0
with open(filename, 'rb') as tweetfile:
    reader = csv.DictReader(tweetfile)
    for tweet in reader:
        decoded = json.loads(tweet['value'])
        try:
            storage.save_tweet(decoded)
        except:
            print("Tweet %d already exists.. skipping" % i)
        print("Importing tweet no. %d" % i)
        i+=1
print ("Inserted %d tweets" % i)
