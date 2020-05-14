import requests

import bs4 
import requests

source = requests.get('https://www.google.com/search?rlz=1C1OCLT_enCA771CA771&biw=1366&bih=657&tbm=nws&sxsrf=ALeKk02qA4I8X1ziUmVUhj5qhb6vWEfLwA%3A1589417866562&ei=ipe8XrbpIYKytAah2hY&q=TSLA&oq=TSLA&gs_l=psy-ab.4...5965.7649.0.7792.0.0.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..0.0.0....0.eE6QU08tNBE').text
soup = bs4.BeautifulSoup(source, 'lxml')

#filename = "TSLAgoogle.csv"
#f = open(filename, "w")

#headers = "Title, Source, Time\n"
#f.write(headers)

for article in soup.find_all('div', class_="g"):

    title = article.div.div.h3.a['href']
    print(title)

    #site = article.find('span', class_="xQ82C e8fRJf").text
    #print(site)
    

    #time = article.find('span', class_="f nsa fwzPFf").text
    #print (time)
    #print()#used for a space

    #f.write(title + "," + site + "," + time + "\n")
