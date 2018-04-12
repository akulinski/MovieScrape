import csv


class Writer:
#class for writing data to csv file
    def __init__(self, fileName):
       self.name = fileName+".csv"
       with open(self.name,'a') as f:
            writer = csv.writer(f)
            writer.writerow(['title']+['rating'])
            f.close()


    def wirteToFile(self, title, rating=0):
        with open(self.name, 'a') as f:
            writer = csv.writer(f)
            rating = float(str(rating).replace(",", "."))

    def wirteToFile(self, title, rating='n/d'):
        with open(self.name, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([title]+[rating])
            f.close()
