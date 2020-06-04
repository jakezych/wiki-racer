import requests
from bs4 import BeautifulSoup 

class Wikiscraper:
  def __init__(self):
    self.page = None
    self.pageLinks = set()
    self.setRandomPage()
    self.getPageLinks()
    
  def setRandomPage(self):
    self.page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
  
  def getPageLinks(self):
    soup = BeautifulSoup(self.page.content, 'html.parser');
    possibleLinks = soup.find_all('a', href=True)

    for elem in possibleLinks:
      link = elem.get('href')
      
      if(self.isValid(link)):
        self.pageLinks.add(link)

  def isValid(self, link):
    if(link == '/wiki/Main_Page'):
      return False

    if(not link.startswith('/wiki/')):
      return False

    if(link.find(':') != -1 or link.find('#') != -1):
      return False

    return True
