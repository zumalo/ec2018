import datetime
import time

from pymongo import MongoClient
from twitter import Api
import os

from src.database_utils import get_tweets_after_date, show_tweets_from_cursor

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)


client = MongoClient()
db = client['twitter_mashup_db']
hashtag = 'photo'

i = 0
t0 = time.time()
print("start")
for line in api.GetStreamFilter(track=[hashtag]):
    if 'text' in line:
        i += 1
        date = datetime.datetime.strptime(line['created_at'], "%a %b %d %H:%M:%S %z %Y")
        db[hashtag].insert_one({
            'created_at': date,
            'id': line['id'],
            'text': line['text'],
            'source': line['source'],
            'lang': line['lang'],
            'user_id': line['user']['id'],
            'user_name': line['user']['name']
        })
        if i > 1000:
            t1 = time.time()
            print("{} tweets / s".format(i/(t1-t0)))
            t0 = time.time()
            i=0

