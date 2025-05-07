import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

# 1. 사이트분석
main_url = 'https://www.boannews.com'
news_list_url = '/media/t_list.asp'
response = requests.get(main_url + news_list_url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

# 2. 첫번째 뉴스 기사 제목 가져오기
첫번째_뉴스_selector = '#news_area > div:nth-child(1) > a:nth-child(1)'

first_news_title = soup.select_one(첫번째_뉴스_selector)

first_news_title = first_news_title.select_one('span').text

# 3. 전체 뉴스 기사의 제목 가져오기
# 3.1 news_area 내용 전부 가져온다
news_area_selector = '#news_area'
news_area = soup.select_one(news_area_selector)

# 3.2 news_area에서 news_list를 가져온다
news_items = news_area.select('div.news_list')

# 3.3 제목 : news_list > 첫번째 a태그 > span태그를 가져온다
sample = news_items[0]
a_tag = sample.select_one('a')

# 실제 주소는 아니고, main_url 뒤에 오는 주소
link = a_tag['href']
title = a_tag.select_one('span')
print(main_url + link)
print(title.text)

# 3.4 날짜 : news_list > span태그

# 3.5 url : news_list > 첫번째 a태그의 href 속성
