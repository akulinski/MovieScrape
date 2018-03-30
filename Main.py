from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as Soup


import CSVWrite


def main():
    filmweb_top500="http://www.filmweb.pl/ranking/film"

    uClient=uReq(filmweb_top500)

    page_html=uClient.read()

    uClient.close()

    page_soup = Soup(page_html,"html.parser")

    containers=page_soup.find_all("div", {"class": "item place"})

    writer = CSVWrite.Writer("data")

    for container in containers:
        titles=container.findAll("div",{"class": "film__original"})
        rating=container.findAll("span",{"class": "rate__value"})
        try:
            print(titles[0].text+" "+rating[0].text)
            writer.wirteToFile(titles[0].text,rating[0].text)
        except IndexError:
            pass

if __name__ == '__main__':
    main()