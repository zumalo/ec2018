from src.database_utils import *
from src.data_visualize import *
cursor = get_tweets_after_date('2018', '4', '4', '18', '29', '20', 'photo')
print(get_tweets_amount(cursor))
create_chart(get_most_used_words(cursor, min_word_length=4), 'Najczęsciej używane słowa ')
create_chart(get_country_list_from_cursor(cursor), 'Kraje z których najczęściej wysyłano tweety')
create_chart(get_users_from_cursor(cursor), 'Użytkownicy którzy najczęściej tweetowali')


