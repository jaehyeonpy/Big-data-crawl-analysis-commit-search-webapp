#import cProfile
import time

from django.shortcuts import render
from django.db import connection

from common import detect_invalid_sql_db


def main(request):
    if request.method == 'GET':
        return render(
            request,
            'searcher/main.html'
            )

    elif request.method == 'POST':
        keyword = request.POST['keyword'].lower()
        searched_table = ()
        searched_tweet = ()


        if keyword == 'all':
            cc = connection.cursor()
            cc.execute(
                'SHOW TABLES WHERE' \
                ' TABLES_IN_DB LIKE "%_positive" OR' \
                ' TABLES_IN_DB LIKE "%_negative"'
                )
            searched_table = cc.fetchall() 
            cc.close()

            if searched_table == ():
                return render(
                    request,
                    'searcher/main.html', 
                    {'is_notable': 'true'}
                    )
            else:
                searched_table = [st[0] for st in searched_table]
                
                return render( 
                    request,
                    'searcher/main.html', {
                        'searched_table': searched_table,
                        'searched_table_count': len(searched_table),
                    }) 


        else:
            # if invalid, raise an exception in the function.
            # raise an exception too, when accessing the database even though there is no table in it.
            detect_invalid_sql_db(keyword) 

            cc = connection.cursor()
            start = time.time()
            cc.execute('SELECT * FROM %s' % keyword)
            end = time.time() 

            searched_tweet = cc.fetchall()
            cc.close()

            if searched_tweet == ():
                return render(
                    request,
                    'searcher/main.html', 
                    {'is_notweet': 'true'}
                    )            
            else:
                return render( 
                    request,
                    'searcher/main.html', {
                        'searched_tweet': searched_tweet[:100],
                        'searched_tweet_count': len(searched_tweet),
                        'search_time': round(end-start, 3),
                    }) 