from wikiracer import *
import time
#TO-DO: make api calls asynchronous, use asynchio library
#       when inputting Special:Random, ladder doesn't actually contains name of page
def main():
  wikiRacer = Wikiracer()
  
  print('Starting search')

  startTime = time.perf_counter()
  solution = wikiRacer.findSolution('/wiki/Milkshake', '/wiki/Gene')
  endTime = time.perf_counter()

  formatted = [page[6:] for page in solution]

  print(formatted)
  print(f'Time Elapsed: {endTime - startTime:0.3f} seconds')

if __name__ == '__main__':
  main()

#Milkshake -> Gene = ~76s