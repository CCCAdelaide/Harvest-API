import couchdb
import couchdb.design



# Modified version of the code found at:
# https://geduldig.github.io/tutorials/twitter-couchdb/
# (c) Jonas Gedulig

#Change this to point to location of couchdb server
DBURL = 'http://146.118.96.142:5984/'

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