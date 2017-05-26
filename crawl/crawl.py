# naver 패키지 내부의 NaverWebtoon클래스형 인스턴스를
# 생성 인스턴스에서  crawl_episode실행
from naver import *

# from naver import NaverWebtoonCrawler

webtoon_id = 183559
comics = NaverWebtoonCrawler(webtoon_id)
comics.crawl_episode(4)
