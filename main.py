import server
from newGame import handler as newGameHadler

import logick

#!/usr/bin/env python
import signal
import sys
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

def main(dareFiles,port = 1337):
  # register ctrl+c for exit
  signal.signal(signal.SIGINT, signal_handler)

  for file in dareFiles: 
    logick.loadTaskList()

  games = {}
  server.root["new"]=(newGameHadler,games)
  server.root["games"]=games



  print("serving at port", port)
  server.serve(port)

if __name__ == '__main__':
    main(["./json/anna_dare.json"])