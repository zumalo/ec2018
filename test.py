from src.database_utils import *

cursor = get_tweets_after_date('2018', '4', '6', '16', '27', '40', 'facebook')
show_tweets_from_cursor(cursor)
print("Amount of tweets = " + str(get_tweets_amount(cursor)))


