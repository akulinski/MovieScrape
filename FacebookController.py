import CSVWrite
from bs4 import BeautifulSoup as Soup
import json
import os.path
import sqlite3

from facepy import GraphAPI

#class witch collets likes on facebook

class Facebook:

    def __init__(self,token,db):
        self.graph = GraphAPI(token)
        self.movies_raw=[]
        self.soup=[]
        self.db=db


    def getMovies(self):
        #movies_raw is nested dictionary

        self.movies_raw = self.graph.get('me/movies')
        if os.path.isfile("fbData.csv"):
            os.remove("fbData.csv")

        writer = CSVWrite.Writer("fbData")
        for x in self.movies_raw['data']:
            writer.wirteToFile(x['name'])
            self.db.uploadToFacebook(x['name'])