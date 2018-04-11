
import scrape_filmweb
import scrape_imdb
import DatabaseController
import scrapeRottenTomatoes
import FacebookController
import TOKEN

def main():

#starting point invoking methods from classes, scraping data info csv and uploding csv to db

    db=DatabaseController.Controller()

#scrape
    filmweb=scrape_filmweb.scraper()
    filmweb.scrape()

#upload
    db.readCSV('dataFilmWeb.csv','FILMWEB')

#scrape
    imdb=scrape_imdb.scraper()
    imdb.scrape()

#upoload
    db.readCSV('dataImdb.csv','IMDB')

#scrape

    rotten=scrapeRottenTomatoes.scraper()
    rotten.scrape()

#upoload
    db.readCSV('dataRottenTomatoes.csv',"ROTTEN")

#comon titles

    db.generateComon()

#closing cursore
    db.cursor.close()
    db.connection.close()

    fb=FacebookController.Facebook(TOKEN.token)

    fb.getMovies()

if __name__ == '__main__':
    main()