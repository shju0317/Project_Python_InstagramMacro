# * chapter02_webdriver.py
# * : Selenium의 Webdriver 사용방법(+ Chrome driver)
# *

from selenium import webdriver

# instagram 페이지에서 원하는 해쉬태그로 selenium 접속(+ Chrome driver)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe') # 상대주소: 내가 위치한 파일을 기준으로

# https://www.instagram.com/explore/tags/카페
# URL 주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%EC%B9%B4%ED%8E%98/'
driver.get(url)
# driver.close() # 실행 후 브라우저 종료