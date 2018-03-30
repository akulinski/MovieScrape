from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as Soup

filmweb_top500="http://www.filmweb.pl/ranking/film"

uClient=uReq(filmweb_top500)

page_html=uClient.read()


uClient.close()

page_soup=Soup(page_html,"html.parser")


containers=page_soup.find_all("div",{"class":"item place"})

for container in containers:
    titles=container.findAll("div",{"class":"film__original"})

    try:
        print(titles[0].text)
    except IndexError:
        pass