from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import CSVWrite
import os.path

class scraper:

#link to rotten 100
    filmweb_top500 = "https://www.rottentomatoes.com/top/bestofrt/"

    def __init__(self):
        #initialize vars for scraping

        self.uClient = uReq(scraper.filmweb_top500)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = Soup(self.page_html, "html.parser")

    def scrape(self):

        #check if file exists if so, remove
        if os.path.isfile("dataRottenTomatoes.csv"):
            os.remove("dataRottenTomatoes.csv")

        writer = CSVWrite.Writer("dataRottenTomatoes")
        count=0

        #titles in table
        for container in self.page_soup.find_all('tr'):
            titles = container.findAll("a", {"class": "unstyled articleLink"})
            rating = container.findAll("span", {"class": "tMeterScore"})
            try:
                writer.wirteToFile(str(titles[0].text).strip(" "), self.convertRating(str(rating[0].text).strip("%")))
                #print(str(titles[0].text).strip( )+str(self.convertRating(rating[0].text))
            except IndexError:
                pass



    def convertRating(self,value):
        return float((int(value)*10)/100)
