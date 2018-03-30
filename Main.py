from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import CSVWrite

import scrape_filmweb
import scrape_imdb

def main():

    filmweb=scrape_filmweb.scraper()
    filmweb.scrape()

    imdb=scrape_imdb.scraper()
    imdb.scrape()

if __name__ == '__main__':
    main()