from pymongo import MongoClient
import datetime
from collections import Counter, OrderedDict, defaultdict
import operator
import re
from time import time
client = MongoClient()
db = client['twitter_mashup_db']  # nazwa bazy danych


def get_tweets_after_date(year, month, day, hour, minute, second, table_name):
    date = datetime.datetime.strptime(str(year + ', ' + month + ', ' + day + ', ' + hour + ', ' + minute + ', ' + second), "%Y, %m, %d, %H, %M, %S")
    cursor = db[table_name].find({'created_at': {"$gt": date}})
    # cursor.sort('created_at')
    return cursor


def get_tweets_amount(cursor):
    return cursor.count()


def show_tweets_from_cursor(cursor):
    cursor.rewind()
    for document in cursor:
        print(document)


def get_users_from_cursor(cursor, amount=10):
    list = []
    cursor.rewind()
    for document in cursor:
        list.append(document['user_name'])
    freq = sorted(Counter(list).items(), key=operator.itemgetter(1), reverse=True)
    return freq[:amount]


def get_country_list_from_cursor(cursor, amount = 10):
    list = []
    cursor.rewind()
    for document in cursor:
        list.append(document['lang'])

    freq = sorted(Counter(list).items(), key=operator.itemgetter(1), reverse=True)
    return freq[:amount]


def get_most_used_words(cursor, amount=10, min_word_length=3):
    t0 = time()
    cursor.rewind()
    main_dict = defaultdict(list)
    for element in cursor:
        temp_set = set()
        text = element['text']
        word_list = re.sub('[^\w]', " ", text).split()
        for word in word_list:
            temp_set.add(word)

        for word in temp_set:
            main_dict[word] = main_dict.get(word, 0) + 1
    main_dict.pop('RT')
    main_dict.pop('https')

    to_delete = []
    for key, value in main_dict.items():
        if len(key) < min_word_length:
            to_delete.append(key)

    for key in to_delete:
        main_dict.pop(key)
    t1 = time()

    print("it took {}s".format(t1-t0))
    return sorted(main_dict.items(), key=operator.itemgetter(1), reverse=True)[:amount]