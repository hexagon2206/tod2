import server
from newGame import handler as newGameHadler

import logick

logick.loadTaskList("./json/anna_dare.json")

games = {}
server.root["new"]=(newGameHadler,games)
server.root["games"]=games



p = 1337
print("serving at port", p)
server.serve(p)