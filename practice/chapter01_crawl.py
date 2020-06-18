# ** chapter01_crawl.py
# * requests로 크롤링하는 부분을 모듈화하고,
# * Import해서 사용하는 코드
# *

from libs.crawler import crawl # libs의 crawler를 호출해서 crawl로 부르겠다는 의미

# 수집하고 싶은 인스타그램의 해시태크(#) 페이지 URL주소
url = 'https://www.instagram.com/explore/tags/%EC%B9%B4%ED%8E%98/'

pageString = crawl(url)
print(pageString)