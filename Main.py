from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import CSVWrite

import scrape_filmweb

def main():

    filmweb=scrape_filmweb.scraper()
    filmweb.scrape()



if __name__ == '__main__':
    main()