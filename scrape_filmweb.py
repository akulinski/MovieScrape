from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import CSVWrite

class scraper:

    filmweb_top500 = "http://www.filmweb.pl/ranking/film"

    def __init__(self):
        self.uClient = uReq(scraper.filmweb_top500)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = Soup(self.page_html, "html.parser")

    def scrape(self):

        self.containers = self.page_soup.find_all("div", {"class": "item place"})

        writer = CSVWrite.Writer("data")

        for container in self.containers:
            titles = container.findAll("div", {"class": "film__original"})
            rating = container.findAll("span", {"class": "rate__value"})
            try:
                print(titles[0].text + " " + rating[0].text)
                writer.wirteToFile(titles[0].text, rating[0].text)
            except IndexError:
                pass