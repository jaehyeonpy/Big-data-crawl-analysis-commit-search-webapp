import logging, re

from asari.api import Sonar
#from guppy import hpy
from langdetect import detect

from django.db import connection


s = Sonar() 
#h = hpy()
logger = logging.getLogger('logger')
rc = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ]+')


def exclude_tweets_not_including_keywords(keywords, tweets):
    '''
        The function excludes elemtents in tweet that do not have the keywords in their values.
        for instance, if the index 0 element in tweet does not have the keywords in its value, 
        the input and output would be like:

        Input: 
            {0: (content 0), 1: (content 1), ...} for the expected input,
            {} for the no-tweet-found-case input, the abnormal input. refer to scrape_some_keyword()
        Output: 
            {1: (content 1), ...} for the expected output,
            {} following the above input
    '''

    tws = {}

    for key, val in tweets.items():
        included_words = 0

        for k in keywords:
            if k in val:
                included_words += 1

        if included_words == len(keywords):
            tws[key] = val

    return tws


def add_sentiment_and_return(tweets):
    '''
        The function divides elemtents in tweet that are classified
        as 'positive' sentiment tweets into tweet_positive, 
        as 'negative' sentiment tweets into tweet_negative.
        the input and output would be like:

        Input: 
            {0: (content 0), 1: (content 1), ...} for the expected input,
            {} following exclude_tweets_not_including_keywords()
        Output: 
            tweet_positive: {0: (content 0, 'positive'), 2: (content 2, 'positive'), ...}
            tweet_negative: {1: (content 1, 'negative'), 3: (content 3, 'negative'), ...}
            for the expected output,

            tweet_positive: {}
            tweet_negative: {}
            following the above input
    '''

    tweet_positive = {}
    tweet_negative = {}

    for k, v in tweets.items():
        sentiment = s.ping(v)['top_class']

        if sentiment == 'positive':
            tweet_positive[k] = (v, sentiment) 
        else:
            tweet_negative[k] = (v, sentiment)
    
    return tweet_positive, tweet_negative


def detect_invalid_sql_crawl(keyword):
    rf = rc.findall(keyword)
    if rf != []:
        return

    lang = detect(keyword) 
    if lang == 'ko' or lang == 'ja' or lang == 'zh-cn': # zh-cn for japanese in kanji only.
        return
    
    logger.critical('Invalid sql string detected: %s' % keyword) 
    raise Exception('Invalid sql string detected: %s' % keyword)
    

def detect_invalid_sql_db(keyword):
    cc = connection.cursor()
    cc.execute(
        'SHOW TABLES WHERE' \
        ' TABLES_IN_DB LIKE "%_positive" OR' \
        ' TABLES_IN_DB LIKE "%_negative"'
        )            
    searched_table = cc.fetchall() 
    cc.close()

    if searched_table == ():
        logger.critical('Accessing the database even though there is no table in it.')
        raise Exception('Accessing the database even though there is no table in it.')    
    else:
        for st in searched_table:
            if keyword == st[0]:
                return
            
        logger.critical('Invalid sql string detected: %s' % keyword)
        raise Exception('Invalid sql string detected: %s' % keyword)