
import scrape_filmweb
import scrape_imdb
import DatabaseController

def main():

    db=DatabaseController.Controller()

    filmweb=scrape_filmweb.scraper()
    filmweb.scrape()

    db.readCSV('dataFilmWeb.csv','FILMWEB')

    imdb=scrape_imdb.scraper()
    imdb.scrape()

if __name__ == '__main__':
    main()