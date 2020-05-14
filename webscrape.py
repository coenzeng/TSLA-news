import requests

import bs4 
import requests

source = requests.get('https://ca.news.search.yahoo.com/search;_ylt=AwrJ7JKUXLxe4hIA6iTrFAx.;_ylu=X3oDMTB0N2Noc21lBGNvbG8DYmYxBHBvcwMxBHZ0aWQDBHNlYwNwaXZz?p=TSLA&fr2=piv-web&fr=uh3_news_web_gs').text
soup = bs4.BeautifulSoup(source, 'lxml')

filename = "TSLA.csv"
f = open(filename, "w")

headers = "Title, Source, Time\n"
f.write(headers)

for article in soup.find_all('div', class_="dd NewsArticle"):

    title = article.ul.li.a['title']

    site = article.find('span', class_="mr-5 cite-co").text
  
    time = article.find('span', class_="fc-2nd mr-8").text

    f.write(title.replace(",", "|") + "," + site + "," + time + "\n")

f.close()
