import server
import logick

import game


def handler(requestData,data):
  games,url,players = data;
  if requestData[1]:
    paras = server.parsePara(requestData[1])
    

    if "start" in paras:
      data = game.setupGame(players) 
      games[url] = (game.handler,(games,url,data))
      html = "Succsess !<br><a href=\"{}\">[click Here]</a><br>\n".format(requestData[0][0])     
      return 200,'text/html',html.encode('ascii')


    while True:
      if not "name" in paras:
        break
      if not "roles" in paras:
        break
      if not "tags" in paras:
        break
      
      roles = set(paras["roles"].split("+"))
      tags = set(paras["tags"].split("+"))
      
      players.append((tags,roles,paras["name"]))
      break


    if "delete" in paras:
      i=len(paras)
      while i>0:
        i=i-1
        if players[i][2] == paras["delete"] :
          del players[i]

  result = "players :<br>\n"
  if len(players) == 0 :
      result += "- empty -<br>\n"
  else:
    for player in players:
      html="{} ".format(str(player))
      deleteUrl = "{}?delete={}".format(requestData[0][0],player[2])
      html += "<a href=\"{}\">[delete]</a><br>\n".format(deleteUrl)
      result += "{}<br>\n".format(html)

  result += "<br><br>Add Player<br>\n"
  
  result += """ <form action="{}">
  Name : <br>
  <input type="text" name="name" value=""><br>
  Roles durch lehrzeichen seperiert:<br>
  <input type="text" name="roles" value=""><br><br>
  Tags durch lehrzeichen seperiert:<br>
  <input type="text" name="tags" value=""><br><br>
  <input type="submit" value="Create">
  </form>""".format(requestData[0][0])
  result += "<a href=\"{}?start\">StartGame</a><br>\n".format(requestData[0][0]) 

  return 200,'text/html',result.encode('ascii')
