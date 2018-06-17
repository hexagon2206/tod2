import server

from gameLoby import handler as gameLobyHandler

def handler(requestData,games):
  url = server.newUrl(games)
  games[url] = (gameLobyHandler,(games,url,[]))
  return 200,'text/html',("new game created: {}".format(url)).encode('ascii')
