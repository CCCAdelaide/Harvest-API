# Team 9    (Adelaide)
# 
# Jun Jen CHAN    (341759)
# Daniel TEH    (558424)
# Tou LEE    (656128)
# David MONROY    (610346)
# Jaime MARTINEZ    (642231)

import couchdb
import couchdb.design

# Modified version of the code found at:
# https://geduldig.github.io/tutorials/twitter-couchdb/
# (c) Jonas Gedulig

#Change this to point to location of couchdb server
DBURL = 'http://localhost:5984/'

class TweetStore(object):
    def __init__(self, dbname, url = DBURL):
        try:
            self.server = couchdb.Server(url=url)
            self.db = self.server.create(dbname)
        except couchdb.http.PreconditionFailed:
            self.db = self.server[dbname]
    
# Store id_str as the key in db    
    def save_tweet(self, tw):
        tw['_id'] = tw['id_str']
        self.db.save(tw)
