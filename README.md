# :camera: Project_Python_InstagramMacro 

Python 기반의 Selenium(feat: Chrome Driver)을 사용하여 인스타그램에 로그인하고, 원하는 해시태그로 피드를 검색한 후 피드별로 좋아요 클릭과 댓글 등록을 반복하는 매크로 프로그램

## :heavy_check_mark: Developer Environment
  - Language: :crocodile:Python 3.7
  - IDE Tool: :computer:Pycharm
  - Package Manager: :snake:Anaconda
  - Using Package: requests, selenium, beautifulsoup4, time, random
  
## :heavy_check_mark: Contents
  1. 인스타그램 로그인
  2. 인스타그램 해시태그 검색
  3. 검색된 피드에 좋아요버튼 클릭 + 댓글 등록하는 매크로 프로그램

## :heavy_check_mark: Repository structure description
  1. practice
  - [Chapter 01. crawl](#running-the-tests)
  - [Chapter 02. webdriver](#deployment)
  - [Chapter 03. selenium](#built-with)
  - [Chapter 04. ](#contributing)
  - [Chapter 05.](#versioning)
  - [Chapter 06.](#authors)

  
  ## 
## :heavy_check_mark: Details

🎲Project_Python_InstagramMacro
Python 기반의 Selenium(feat: Chrome Driver)을 사용하여 인스타그램에 로그인하고, 원하는 해시태그로 피드를 검색한 후 피드별로 좋아요를 클릭하고 댓글 등록을 반복하는 매크로 프로그램.

✔️Developer Environment
Language: 🐊Python 3.7
IDE Tool: 💻Pycharm
Package Manager: 🐍Anaconda
Using Package: requests, selenium, beautifulsoup4, time, random
Using WebDriver: Chrome Driver ( Use the same version as the Chrome browser version you use!)
💾Repository structure description
1.practice
chapter01_crawl
chapter02_webdriver
chapter03_selenium_crawl
chapter04_facebook_login
2.libs
crawler
3.instagram
hashtag_reply_macro
💬How to use?
Prepare your Instagram ID and password.
Download the same version of the chrome driver as your Chrome browser
Import the project into Pycharm tool
Create webdriver directory within project
Drag and Drop the downloaded chrome driver to the webdriver directory
Go to Instagram's Feed and check the selector(Refer to instagram/hashtag_reply_macro.py 33 Line)
Run the program!
