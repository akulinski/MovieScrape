from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import CSVWrite

class scraper:

    link='http://www.imdb.com/list/ls004427773/'
    def __init__(self):
        self.uClient = uReq(scraper.link)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = Soup(self.page_html, "html.parser")

    def scrape(self):
        self.containers = self.page_soup.find_all("div", {"class": "lister-item-content"})

        writer = CSVWrite.Writer("dataImdb")
        count=0
        for container in self.containers:
            titles = container.find_all("a")
            rating = container.find_all("strong")
            try:
                writer.wirteToFile(titles[0].text, rating[0].text)
                count+=1
            except IndexError:
                pass