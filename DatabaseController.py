import sqlite3
import csv


class Controller:

    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(
                '''
                  CREATE TABLE FILMWEB
                    (
                      title TEXT PRIMARY KEY,
                      rating DOUBLE 
                    )
                '''
            )
            self.connection.commit()

        except sqlite3.OperationalError:
            pass

        try:
            self.cursor.execute(
                '''
                  CREATE TABLE IMDB
                    (
                      title TEXT PRIMARY KEY,
                      rating DOUBLE 
                    )
                '''
            )
            self.connection.commit()

        except sqlite3.OperationalError:
            pass

    def uploadToDb(self,title,values):
        statement = "INSERT INTO %s VALUES (?,?);" % title
        try:
            self.cursor.execute(statement, values)
            self.connection.commit()

        except sqlite3.IntegrityError:
            print("INtegrity error ")
            print(values)

    def readCSV(self,file,title):
        with open(file,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                tuple=(row[0],row[1])
                self.uploadToDb(title,tuple)

