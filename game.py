import server
import logick

def setupGame(players):
  return (players,logick.taskSet(players),logick.questionSet(players),[])


def handler(requestData,data):
  games,url,gameData = data
  players,taskSet,questionSet,history = gameData
  html = "game<br>"
  
  if requestData[1]:
    paras = server.parsePara(requestData[1])

    if "truth" in paras:
      selectionList = questionSet
    if "dare" in paras:
      selectionList = taskSet

    currentPlayer = players.pop(0)
    players.append(currentPlayer)

    task = None 
    for e in selectionList:
      tags,setting,nt = e
      if currentPlayer in setting:
        task = e
        break
    if task == None :
      html += "no task found for {}<br>".format(currentPlayer) 
    else:
      selectionList.remove(e)
      history.append(e)
    
  html += "<br><br><br>"
  html += "{} is next,<br>".format(players[0])
  html += "<a href=\"{}?truth\">Truth</a><br>\n".format(requestData[0][0])     
  html += "<a href=\"{}?dare\">Dare</a><br>\n".format(requestData[0][0])     
      
  return 200,'text/html',html.encode('utf8')