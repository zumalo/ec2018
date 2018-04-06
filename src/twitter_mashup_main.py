import datetime
from pymongo import MongoClient
from twitter import Api
import os


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


for line in api.GetStreamFilter(track='#facebook'):
    if 'text' in line:
        print(line)
        date = datetime.datetime.strptime(line['created_at'], "%a %b %d %H:%M:%S %z %Y")
        db['facebook'].insert_one({
            'created_at': date,
            'id': line['id'],
            'text': line['text'],
            'source': line['source'],
            'lang' : line['lang'],
            'user_id': line['user']['id']
        })
