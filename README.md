# Harvest-API
Tweet Harvester

###Dependencies
-- python-tweepy

-- python-couchdb

The tweet harvester is written in python 2. It leverages the tweepy module to access the twitter streaming and search apis. It also uses the python-couchdb module to access the couchdb db to save tweets.

There are two different types of search in this package. One to access the Search API (harvester-search.py) and two for the streaming API in the north and south regions (harvester-south.py & harvester-north.py). The streaming API uses the entry point harvester-stream.py to choose the region and api key to use.

Usage:
harvester-stream.py <region> <API_key>
region: south, north
API_key: daniel, jun, jimmy, david

harvester-search.py


###Functionality
The harvester gathers tweets (by either listening on a stream, or requesting them via search) and then inserts them into the db with the Tweet ID as the primary key.
