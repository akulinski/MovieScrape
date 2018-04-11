
import scrape_filmweb
import scrape_imdb
import DatabaseController
import scrapeRottenTomatoes
import FacebookController
import TOKEN
<<<<<<< HEAD

=======
>>>>>>> 8502a2519c54cba741527620e507c32c0dbf386b
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

<<<<<<< HEAD
    db.generateComon()
=======
#    db.generateComon()
>>>>>>> 8502a2519c54cba741527620e507c32c0dbf386b

#closing cursore
    db.cursor.close()
    db.connection.close()

<<<<<<< HEAD
    fb=FacebookController.Facebook(TOKEN.token)

    fb.getMovies()
=======
fb=FacebookController.Facebook(TOKEN.token)

fb.getMovies()
>>>>>>> 8502a2519c54cba741527620e507c32c0dbf386b

if __name__ == '__main__':
    main()