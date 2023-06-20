# Big-data-crawl-analysis-commit-search-webapp


## Description


<table>
 <tbody>
  <tr>
   <th>endpoint</th>
   <th>method</th>
   <th>explanation</th>
  </tr>

  <tr>
   <td>/crawl-analysis-commit-er</td>
   <td>GET</td>
   <td>
    <li>트위터에서 crawl할 키워드 등을 입력하는 화면을 클라이언트에 리턴합니다. 화면에서 키워드는 '키워드1', '키워드1 키워드2' 와 같이 입력합니다. 이 때, 키워드는 한국어, 일본어로만 쓰여야 합니다.</li> 
    <li>관련 요구사항, 테스트 사항은 https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/3, https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/4, https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/5 참고하시길 바랍니다.</li>
    <li><img width="1440" alt="cv1" src="https://user-images.githubusercontent.com/123809332/236416836-393bf009-2365-4445-bad3-9ba400b4a6fd.png"></li>
    <li><img width="1440" alt="cv2" src="https://user-images.githubusercontent.com/123809332/236417322-5b02c985-9c09-49ca-92ec-09198f8d2919.png"></li>
   </td>
  </tr>
  
  <tr>
   <td>/crawl-analysis-commit-er/crawler-analyzer</td>
   <td>POST</td>
   <td>
    <li>위 화면 상 crawl 버튼 누르면, 트위터에서 crawl하고, 그 결과를 sentiment analysis 하기 위한 정보를 서버에 전달합니다.</li>
    <li>GET /crawl-analysis-commit-er 하여 그 결과 화면을 클라이언트에 리턴하는 내용도 포함되어 있습니다. Restful API 원칙 어긋나겠지만, 포트폴리오 같이 규모 작은 프로젝트에는 무방하리라 생각했습니다.</li> 
    <li>POST 시 '키워드1'로 포함해 전달했다면, '키워드1'이 모든 트윗에 포함되어 있어야 합니다. 마찬가지로, POST 시 '키워드1 키워드2'로 포함해 전달했다면, '키워드1', '키워드2'가 모든 트윗에 포함되어 있어야 합니다.</li>
    <li>sentiment는 positive, negative 분류하여 표시합니다.</li> 
    <li>관련 요구사항, 테스트 사항은 https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/6 참고하시길 바랍니다.</li>
    <li>아래 사진은 POST 시 '불닭'으로 포함하여 전달한 것으로, '불닭'이 모든 트윗에 포함되어 있음을 나타냅니다. negative 분류된 트윗 없어서 0개로 표시된 점 주의 바랍니다.</li>
    <li><img width="1440" alt="cc1" src="https://user-images.githubusercontent.com/123809332/236419003-c769ec37-0e9b-412d-b296-4cb046eaa02e.png"></li>
    <li><img width="1440" alt="cc2" src="https://user-images.githubusercontent.com/123809332/236419029-fa9a9bcb-127f-4954-ac23-97b4f25b0cb3.png"></li>
   </td>
  </tr>
  <tr>
   <td>/crawl-analysis-commit-er/committer</td>
   <td>POST</td>
   <td>
    <li>위 화면 상 commit 버튼 눌렀을 때, 이전에 POST /crawl-analysis-commit-er/crawler-analyzer 시 '키워드1' 포함해 전달했었다면, positive 분류된 트윗을 데이터베이스 내 '키워드1_positive' 테이블, negative 분류된 트윗을 데이터베이스 내 '키워드1_negative' 테이블에 적재합니다.</li> 
    <li>이전에 POST /crawl-analysis-commit-er/crawler-analyzer 시 '키워드1 키워드2' 포함헤 전달했었다면, 데이터베이스 내 '키워드1_키워드2_positive', '키워드1_키워드2_negative' 테이블에 적재합니다.</li> 
    <li>관련 요구사항, 테스트 사항 https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/7 참고하시길 바랍니다.</li>
   </td>
  </tr>
  
  <tr>
   <td>/searcher</td>
   <td>GET</td>
   <td>
    <li>데이터베이스 저장된 테이블 리스트 출력 명령 입력받거나, 혹은 데이터베이스 저장된 특정 테이블 내용 출력하도록 테이블 이름 입력받는 화면을, 클라이언트에게 리턴합니다.</li> 
    <li>화면에서 'all' 입력하는 경우, 데이터베이스 저장된 테이블 리스트 표시합니다. '키워드1_positve', '키워드1_negative', '키워드1_키워드2_positve', '키워드1_키워드2_negative' 입력하여 해당 테이블 내용을 불러올 수 있습니다. 이 때, 모든 row를 데이터베이스에서 웹서버 불러오되 화면에는 100개 row만 표시합니다. 데이터를 데이터베이스에서 불러오는 시간인 search time도 표시합니다.</li>
    <li>관련 요구사항, 테스트 사항은 https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/8, https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/9 참고하시길 바랍니다.</li>
    <li><img width="1440" alt="dv1" src="https://user-images.githubusercontent.com/123809332/236418164-82f6e047-00b1-44b8-9f41-8f647743b2d8.png"></li>
    <li><img width="1440" alt="dv2" src="https://user-images.githubusercontent.com/123809332/236418303-d0f2ce7b-817d-498a-a6da-5090fe8bca2d.png"></li>
   </td>
  </tr>
  
  <tr>
   <td>/searcher</td>
   <td>POST</td>
   <td>
    <li>위 화면 상 search 버튼 눌러서, 데이터베이스에 있는 테이블 리스트 출력 명령 서버에 전달하거나, 데이터베이스 저장된 특정 테이블 내용 출력하도록 테이블 이름 서버에 전달합니다.</li>
    <li>GET /searcher 하여 그 결과 화면을 클라이언트에 리턴하는 내용도 포함되어 있습니다. Restful API 원칙 어긋나겠지만, 포트폴리오 같이 규모 작은 프로젝트에는 무방하리라 생각했습니다.</li> 
    <li>관련 요구사항, 테스트 사항은 https://github.com/jaehyeonpy/Big-data-crawl-analysis-commit-search-webapp/issues/10 참고하시길 바랍니다.</li>
    <li><img width="1440" alt="ds" src="https://user-images.githubusercontent.com/123809332/236432723-0a2f2642-a8f5-40df-af26-729eda286cef.png"></li>
   </td>
  </tr>
 </tbody>
</table>


## Troubleshooting

- 대용량 데이터 다룰 시 disk IO 줄이는 것이 중요한 것임을 알고, in-memory 상에 필요한 데이터를 적재 시키고자 하였습니다.
  - mysql query cache 기능 사용하고, 테이블 파티셔닝 하였습니다만, django 서버 상에서 쿼리 실행 시 기대만큼 성능 상 이득을 보지 못하였습니다.(10초) 하지만, mysql built-in client 상에서 쿼리 실행 시 상당한 성능 이득을 보았기에(query cache 적용 전 2초, 적용 후 1초), 데이터가 query cache에서 django 서버 이동 중 overhead 일어나고 있다 판단 하였습니다. 따라서, mysql database connector 교체했습니다.(4초)

- [twitter crawling library](https://github.com/shaikhsajid1111/twitter-scraper-selenium) 사용해 browser automation 통해 트위터 게시물 crawl 하는데, 트위터 문제로 트윗이 브라우저에 나타나지 않는 문제 있었습니다. 코드 복잡도 있는 라이브러리 code reading 하여, 본 webapp 문제 아닌 트위터 고유의 문제임을 확인했습니다.
  - 트윗 브라우저 나타나지 않는 문제 대해 code reading 하다 보면 위 라이브러리 거쳐 selenium 코드로 넘어가게 되는데, 마지막에 urlib3 이용해 http request 수행합니다. 그 이전에 문제가 될만한 소지의 코드 보이지 않고, urlib3 이후는 널리 사용되는 코드로 문제가 일어날 소지 적습니다. 따라서, 본 webapp 잘못 없음이라 판단을 내렸습니다.
- 트위터에서는 스크롤하여 더 많은 트윗을 불러올 수 있는데, 스크롤 하여도 트윗 더 불러올 수 없는 문제 있었습니다. 위와 마찬가지로 code reading 해서 본 webapp 문제 아님 확인했습니다. 위 라이브러리, selenium에도 본 문제와 관련한 코드 찾을 수 없었습니다.

- 위 라이브러리 그대로 사용할 수 없어, code reading 후 필요에 따라 수정해서 사용하였습니다.
  - crawl 도중 일부 트윗의 경우 fetch_and_store_all() 내 username 등지에서 raise exception 되고 프로그램 종료됩니다. 이와 같은 문제 피하기 위해, 그리고 본 webapp 경우 content 정도만 필요하여 fetch_and_store_all() 함수 비대한 감 없지 않아, fetch_and_store_some(), fetch_and_store_some()에 coupling 된 함수 새로 만들어 사용했습니다.

~~~py
#fetch_and_store_all() in twitter_scrape_selenium/keyword.py

while len(self.posts_data) < self.tweets_count:
 for tweet in present_tweets:
  name = Finder.find_name_from_tweet(tweet)
  status, tweet_url = Finder.find_status(tweet)
  replies = Finder.find_replies(tweet)
  retweets = Finder.find_shares(tweet)
  username = tweet_url.split("/")[3]
  status = status[-1]
  is_retweet = Finder.is_retweet(tweet)
  posted_time = Finder.find_timestamp(tweet)
  content = Finder.find_content(tweet)
  likes = Finder.find_like(tweet)
  images = Finder.find_images(tweet)
  videos = Finder.find_videos(tweet)
  hashtags = re.findall(r"#(\w+)", content)
  mentions = re.findall(r"@(\w+)", content)
  profile_picture = Finder.find_profile_image_link(tweet)
  link = Finder.find_external_link(tweet)
~~~

~~~py
#fetch_and_store_some() in twitter_scrape_selenium/keyword.py

while len(self.posts_data) < self.tweets_count:
 for tweet in present_tweets:
  content = Finder.find_content(tweet)
~~~

- 요구사항 코드 구현 시 제약사항으로 인해 django ORM 아닌 raw sql 사용하였기에, sql injection 방지할 필요 있었습니다. 
  - POST /crawl-analysis-commit-er/crawl-analysis 해서 건네받은 키워드가 한국어, 일본어 아닌 것이 확인되면 raise exception 하였습니다. 한국어, 일본어로만으로는 sql injection 일으킬 수 없기 때문에, 한국어, 일본어만 valid keyword 인정한다는 논리입니다.
  - POST /searcher 하여 건네받은 키워드가, '키워드1_positive', '키워드1_negative', '키워드1_키워드2_positive', '키워드1_키워드2_negative' 의 형식을 엄격히 지키지 않는 경우 raise exception 하였습니다.


## Installation instructions and warning

- 다음 환경에서 본 프로젝트 실행되었습니다.
  - Mac m1 monterey 12.6.4
  - python 3.10
  - chrome 최신버전
  - mysql5.7
    - /etc/my.cnf 다음과 같이 수정

~~~
[mysqld]
query_cache_type=1
query_cache_size=(임의값 입력)
query_cache_limit=(임의값 입력)
~~~

- 세팅 시 주의사항 
  - pip install -r requirements.txt 이용해 dependency 설치
  - webview/settings.py 참고하여 mysql password 세팅, 'db' 데이터베이스 만들기
  - [connector 설정하기](https://ssungkang.tistory.com/entry/Django-Django-22-mysql-8-버전-연동하기)
  - 트위터 크롤 시 browser automation 이용되는 브라우저에 [인증서 만들고 추가하기](https://github.com/wkeeling/selenium-wire/issues/137), [추가한 인증서 신뢰하기](https://github.com/wkeeling/selenium-wire/issues/120)
 
- 사용 시 주의사항
  - 처음 트위터 crawl 시 대기시간 있음
  - 트위터 crawl 시 browser automation 이용되는 브라우저에서, 트위터 로그인 직접 하고, django 서버 중지하고 다시 실행한 후 사용하기
  - 트위터 crawl 시, crawl용 크롬 외 여러 개 동작시 오동작 우려
