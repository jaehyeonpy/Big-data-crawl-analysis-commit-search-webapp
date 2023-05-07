from common import add_sentiment_and_return, detect_invalid_sql_crawl, exclude_tweets_not_including_keywords, logger
from twitter_scraper_selenium import scrape_some_keyword

from django.db import connection
from django.shortcuts import render


global_tweet_positive = None 
global_tweet_negative = None
global_keyword = None


def main(request):
    return render(
        request,
        'crawled_view/main.html'
        )

def crawl(request):
    if request.method == 'POST':
        # if invalid, raise an exception in the function.
        detect_invalid_sql_crawl(request.POST['keyword'])


        tweets = scrape_some_keyword(
            keyword=request.POST['keyword'], 
            tweets_count=int(request.POST['tweet-count']),
            browser='chrome', 
            headless=False,
            ) 


        keywords = None 

        if ' ' in request.POST['keyword']: 
            keywords = request.POST['keyword'].split(' ') # for korean keyword
        else:
            keywords = request.POST['keyword'].split('　') # for japanese keyword


        tweets = exclude_tweets_not_including_keywords(keywords, tweets)


        tweet_positive, tweet_negative = add_sentiment_and_return(tweets) 


        # these will be used in limited usages.
        global global_tweet_positive, global_tweet_negative, global_keyword
        global_tweet_positive = tweet_positive
        global_tweet_negative = tweet_negative
        global_keyword = '_'.join([k for k in keywords])

        return render(
            request,
            'crawled_view/main.html', {
                'crawled_tweet_positive': tweet_positive,
                'crawled_tweet_negative': tweet_negative,
                'crawled_tweet_positive_count': len(tweet_positive),
                'crawled_tweet_negative_count': len(tweet_negative),
                }) 

def commit_to_db_buffer_size(db_buffer_size):
    table_name_positive = global_keyword+'_positive'
    table_name_negative = global_keyword+'_negative'
    is_first_commited = False
    initial_data_size = 0
    cc = connection.cursor()


    while True:
        for v in global_tweet_positive.values():
            try:
                cc.execute(
                    'INSERT INTO %s VALUES("%s", "%s")' 
                    % (table_name_positive, v[0], v[1])
                    )
            except Exception as e: 
                    err = str(e)

                    if '1064' in err or '1366' in err: # sql syntax error numbers
                        logger.error('An error occured while inserting positive data into a table: %s' % err)
                    else: # other errors
                        logger.error('An error occured while inserting positive data into a table: %s' % err)
                        raise Exception('An error occured while inserting positive data into a table: %s' % err)


        for v in global_tweet_negative.values():
            try:
                cc.execute(
                    'INSERT INTO %s VALUES("%s", "%s")' 
                    % (table_name_negative, v[0], v[1])
                    )
            except Exception as e: 
                    err = str(e)

                    if '1064' in err or '1366' in err:
                        logger.error('An error occured while inserting negative data into a table: %s' % err)
                    else:
                        logger.error('An error occured while inserting negative data into a table: %s' % err)
                        raise Exception('An error occured while inserting negative data into a table: %s' % err)


        cc.execute('SELECT SUM(LENGTH(CONTENTS) + LENGTH(SENTIMENT_CATEGORY)) FROM %s' % table_name_positive)
        cf_positive = 0 if (cf_positive:=cc.fetchone()) == (None,) else cf_positive[0]

        cc.execute('SELECT SUM(LENGTH(CONTENTS) + LENGTH(SENTIMENT_CATEGORY)) FROM %s' % table_name_negative)
        cf_negative = 0 if (cf_negative:=cc.fetchone()) == (None,) else cf_negative[0]

        if is_first_commited == False:
            initial_data_size = cf_positive+cf_negative
            is_first_commited = True
    
        logger.info('table_name_positive data size: %d(positive), %d(negative), %d(all)' 
                    % (cf_positive, cf_negative, cf_positive+cf_negative))

        if (cf_positive+cf_negative+initial_data_size) >= db_buffer_size:
            cc.close()
            return
                    
            
def commit(request): 
    if request.method == 'POST':
        try: 
            cc = connection.cursor()
            cc.execute(
                'CREATE TABLE %s_positive (contents TEXT, sentiment_category TEXT) DEFAULT CHARACTER SET UTF8'
                % global_keyword) 
            cc.execute(
                'CREATE TABLE %s_negative (contents TEXT, sentiment_category TEXT) DEFAULT CHARACTER SET UTF8'
                % global_keyword)
            cc.close() 
        except Exception as e:
            logger.error('An error occured while creating a table: %s' % e)
            raise Exception('An error occured while creating a table: %s' % e)

        # commit the data global_tweet_positive, global_tweet_negative refer to, 
        # when the size of the data reaches to the specified byte,
        # by duplicating the data itself.
        commit_to_db_buffer_size(5242880) 

        return render(
            request,
            'crawled_view/main.html',
            {'is_commited': 'true'} 
            ) 