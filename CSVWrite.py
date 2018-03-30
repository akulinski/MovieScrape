import csv
class Writer:

#class for writing data to csv file
    def __init__(self, fileName):
       self.name = fileName+".csv"
       with open(self.name,'a') as f:
            writer = csv.writer(f)
            writer.writerow(['title']+['rating'])
            f.close()


    def wirteToFile(self, title, rating):
        with open(self.name, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([title]+[rating])
            f.close()
