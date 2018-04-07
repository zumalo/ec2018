from src.database_utils import *
from src.data_visualize import *
cursor = get_tweets_after_date('2018', '4', '4', '18', '29', '20', 'photo')
print(get_tweets_amount(cursor))
print(get_most_used_words(cursor, min_word_length=4))


