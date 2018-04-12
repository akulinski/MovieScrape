import sqlite3
import csv
import string
import CSVWrite
import heapq

class Controller:

#db controller class

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
                    );
                '''
            )
        except sqlite3.OperationalError:
            pass

        try:
            self.cursor.execute(
                '''
                  CREATE TABLE IMDB
                    (
                      title TEXT PRIMARY KEY,
                      rating DOUBLE 
                    );
                '''
            )
            self.connection.commit()

        except sqlite3.OperationalError:
            pass

        try:
            self.cursor.execute(
                '''
                  CREATE TABLE ROTTEN
                    (
                      title TEXT PRIMARY KEY,
                      rating DOUBLE 
                    );
                '''
            )
            self.connection.commit()

        except sqlite3.OperationalError:
            pass

        try:
            self.cursor.execute(
                '''
                  CREATE TABLE COMMON
                    (
                      title TEXT PRIMARY KEY,
                      rating DOUBLE 
                    );
                '''
            )
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

        try:
            self.cursor.execute(
                '''
                  CREATE TABLE FACEBOOK
                    (
                      title TEXT PRIMARY KEY
                    );
                '''
            )
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

        self.heap=[]

    def uploadToDb(self,title,values):
        #prepare statment
        statement = "INSERT INTO %s VALUES (?,?);"%title
        try:
            #exec statment
            self.cursor.execute(statement, values)

        except sqlite3.IntegrityError:
            #getting errors because of stacking data in csv files, for debbuging pourpose deleate csv
            pass

    def readCSV(self,file,title):
        #method to read data from csv and call upload
        with open(file,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                #string strings of punctiations
                row[0] = row[0].strip("+")
                row[0] = row[0].strip()

                if title is "ROTTEN":
                    row[0] = row[0][:-6]


               #print(row[0])

                tuple = (row[0], row[1])
                row[0]=row[0].strip("+")
                row[0] = row[0].strip()
                if title is "ROTTEN":
                    row[0] = row[0][:-6]

                #print(row[0])
                tuple=(row[0].translate(string.punctuation), row[1].translate(string.punctuation))
                self.uploadToDb(title,tuple)
        self.connection.commit()

    def generateComon(self):

        statment = "SELECT * FROM FILMWEB,ROTTEN WHERE FILMWEB.title == ROTTEN.title;"

        wr = CSVWrite.Writer("result")
        self.returnSet = self.cursor.execute(statment)

        if self.returnSet.arraysize == 1:
            #jezeli nie ma wspolnych wartosci to wybierz top z filmwebu
            statment = "SELECT * FROM FILMWEB;"
            self.returnSet = self.cursor.execute(statment)

            #go threw all movies from filmweb heapsort them and display top 10
            for t in self.returnSet:
                #heap sort teoretycznie powinien sortowac wzgledem pierwszego tupla

                self.title=t[0]
                if t[1] != "rating":
                    self.rating=float(t[1])
                    self.values=(self.rating,self.title)
                    self.heap.append(self.values)

            #heap sort going one here
            heapq._heapify_max(self.heap)

            self.count=0
            for x in self.heap:
                if self.count == 9:
                    break
                #kazda litera w slowie liczona jest jako odzielny argument rozwiazanie wrzucenie w tuple
                t=(x[1],)
                self.cursor.execute("SELECT COUNT(*) FROM FACEBOOK WHERE TITLE == ?; ", t)
                self.result = self.cursor.fetchone()

                if(self.result[0] == 0):
                    print("Title "+x[1]+" Rating: "+str(x[0]))
                    wr.wirteToFile("Tytul: " + str(x[1]), "Srednia: " + str(x[0]))
                self.count += 1

                #poping from heap
                heapq.heappushpop(self.heap,x)


        for t in self.returnSet :
            #map values from query to variables
            title = t[0]
            firstMark = str(t[1])
            secondMark=str(t[3])

            #replace , with .
            firstMark=firstMark.replace(",",".")
            secondMark=secondMark.replace(",",".")
            try:
                #calculate mean
                mean=(float(firstMark)+float(secondMark))/2
                print("title: "+str(title)+"\nraking from FILMWEB: "+str(firstMark)+"\nranking from ROTTENTOMATOES:  "+str(secondMark)+"\nMEAN value of both : "+str(mean))
                wr.wirteToFile("Tytul: "+str(title),"Srednia z FILMWEB i ROTTENTOMATOES: "+str(mean))
                #upload common titiles to database
                #check if title is in watched movies from facebook

                self.countStatment="SELECT COUNT(*) FROM FACEBOOK"
                self.count=self.connection.execute(self.countStatment)
                self.values=(str(title), mean)
                self.uploadToDb("COMMON", self.values)

            except ValueError:
                pass
