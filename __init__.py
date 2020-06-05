from wikiscraper import *
import heapq
import copy

class Controller:
  def __init__(self):
    self.scraper = Wikiscraper() 

  #return a set of the links of the next page of a ladder
  def getNextPageLinks(self, ladder):
    nextPage = self.scraper.getPage(ladder[len(ladder) - 1])
    return self.scraper.getPageLinks(nextPage)

  #returns the priority of a ladder by looking at how many links the next page 
  #in the ladder shares with the target page. 
  def calculatePriority(self, ladder, targetLinks):
    pageLinks = self.getNextPageLinks(ladder)
    inCommon = len(set.intersection(pageLinks, targetLinks))
    #negate the result because heapq is a min-heap but max-heap required
    return -inCommon 

  #takes in 2 wiki pages and finds a path of wiki pages between them
  def findSolution(self, start, target):
    pQueue = [] 
    targetPage = self.scraper.getPage(target)
    targetLinks = self.scraper.getPageLinks(targetPage)
    startLadder = [start]
    startPriority = self.calculatePriority(startLadder, targetLinks)
    heapq.heappush(pQueue, (startPriority, startLadder))

    while(len(pQueue) != 0):
      (priority, curLadder) = heapq.heappop(pQueue)
      pageLinks = self.getNextPageLinks(curLadder)

      if(target in pageLinks):
        curLadder.append(target)
        return curLadder

      #this loops takes a really long time -> beautiful soup??
      for page in pageLinks:
        ladderCopy = [] + curLadder
        ladderCopy.append(page)
        ladderPriority = self.calculatePriority(ladderCopy, targetLinks)
        print("new priority" + str(ladderPriority))
        print('new ladder:')
        print(ladderCopy)
        heapq.heappush(pQueue, (ladderPriority, ladderCopy))
      
    #no ladder found
    return []

test = Controller()

#look into using pywikibot
print(test.findSolution('/wiki/Emu', '/wiki/Stanford_University'))