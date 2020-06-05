import requests
from bs4 import BeautifulSoup 

class Wikiscraper:
  #returns the json object of a wiki page given a path
  def getPage(self, path):
    return requests.get('https://en.wikipedia.org' + path)

  #returns a set of all the possible links given a wiki page
  def getPageLinks(self, page):
    soup = BeautifulSoup(page.content, 'html.parser');
    possibleLinks = soup.find_all('a', href=True)

    pageLinks = set()
    for elem in possibleLinks:
      link = elem.get('href')
      
      if(self.isValid(link)):
        pageLinks.add(link)

    return pageLinks

  #checks if a link is a valid link to another wiki page
  def isValid(self, link):
    if(link == '/wiki/Main_Page'):
      return False

    if(not link.startswith('/wiki/')):
      return False

    if(link.find(':') != -1 or link.find('#') != -1):
      return False

    return True

#/wiki/Special:Random = random wiki article
