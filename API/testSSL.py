import tweepy
import time

# API 키 설정
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFNr0wEAAAAAO1iPHU%2BcGhyAGG5UZ4%2BArYi%2FHRw%3DpAaVTGSpMSkCXbyvPJ0UdkrdoCVCZYHiCnYd9xwkEIv1rDey4s'
consumer_key = 'eN2FITCMw4Mi9gEl7k0P8RZlf'
consumer_secret = 'a0YwlfmgZZhSBa2YZAyUndBLyCyH993fOnRSS3DDGKseuHj1XE'
access_token = '1915776919121055745-gFNyNGg3vU8vseH2jRyIpEAj9xbLoH'
access_token_secret = 'PbI34lv1PHezQOrLt7e0ttjIBnjqXGScVsUgvSmtl5FoV'

# 클라이언트 설정 (재시도 기능 활성화)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True  # ★ 핵심 수정 부분 ★
)

# 트윗 검색 (재시도 로직 포함)
max_retries = 3
retry_delay = 60  # 60초 대기

for attempt in range(max_retries):
    try:
        tweets = client.search_recent_tweets(
            query='#food -is:retweet lang:en',
            max_results=50,  # 한 번에 최대 100개까지 가능
            tweet_fields=['public_metrics', 'created_at']
        )
        break  # 성공 시 반복문 탈출
    except tweepy.errors.TooManyRequests as e:
        print(f"Attempt {attempt + 1} failed. Waiting {retry_delay} seconds...")
        time.sleep(retry_delay)
else:
    print("모든 재시도 실패. 1시간 후 다시 시도하세요.")
    exit()

# 데이터 처리 (이전 코드와 동일)
tweet_list = []
if tweets.data:
    for tweet in tweets.data:
        tweet_list.append({
            'text': tweet.text,
            'likes': tweet.public_metrics['like_count'],
            'retweets': tweet.public_metrics['retweet_count'],
            'created_at': tweet.created_at
        })
    tweet_list.sort(key=lambda x: x['likes'], reverse=True)

# 결과 출력
for i, t in enumerate(tweet_list[:3], 1):
    print(f"{i}. {t['text']} (Likes: {t['likes']}, Created: {t['created_at']})")
