
import scrape_filmweb
import scrape_imdb
import DatabaseController
import scrapeRottenTomatoes
import FacebookController
import TOKEN
import GoogleInfo
import threading

def main():

    #starting point invoking methods from classes, scraping data info csv and uploding csv to db

    db=DatabaseController.Controller()
    #fb = FacebookController.Facebook(TOKEN.token)
    #fb.getMovies()

    #scrape
    filmweb=scrape_filmweb.scraper()

    threadFilmweb = threading.Thread(target=filmweb.scrape)
    threadFilmweb.start()
    #upload


    #scrape

    imdb=scrape_imdb.scraper()
    threadImdb=threading.Thread(target=imdb.scrape)
    #threadImdb.start()
    #upoload


    #scrape

    rotten=scrapeRottenTomatoes.scraper()
    threadRotten = threading.Thread(target=rotten.scrape)
    threadRotten.start()

    #upoload

    threadRotten.join()
    db.readCSV('dataRottenTomatoes.csv',"ROTTEN")

    #threadImdb.join()
    #db.readCSV('dataImdb.csv', 'IMDB')

    threadFilmweb.join()
    db.readCSV('dataFilmWeb.csv', 'FILMWEB')
    #comon titles
    db.generateComon()

#closing cursore
    db.cursor.close()
    db.connection.close()

