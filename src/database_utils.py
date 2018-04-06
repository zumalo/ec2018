from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['twitter_mashup_db']  # nazwa bazy danych


def get_tweets_after_date(year, month, day, hour, minute, second, table_name):
    print(str(year + ', ' + month + ', ' + day + ', ' + hour + ', ' + minute + ', ' + second))
    date = datetime.datetime.strptime(str(year + ', ' + month + ', ' + day + ', ' + hour + ', ' + minute + ', ' + second), "%Y, %m, %d, %H, %M, %S")
    cursor = db[table_name].find({'created_at': {"$gt": date}}).sort("created_at")
    return cursor

def get_tweets_amount(cursor):
    return(cursor.count())


def show_tweets_from_cursor(cursor):
    for document in cursor:
        print(document)


