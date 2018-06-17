import json
# part = list von rollen, in order
# task = (part,set([tags]),"name 1 : {} name 2 : {} ")


example_task = (["f","m"],set(["intim","soft"]),"Die {} küsst den {} ")

# likes = set([tags])
# player = (likes,set([roles]),"name")

example_player_m = (set(["intim","soft"]),set(["m"]),"hans")
example_player_f = (set(["intim","soft"]),set(["f"]),"julia")


taskList = [example_task]

playerList = [
  example_player_m,
  example_player_f,
  (set(["intim","soft"]),set(["m"]),"hugo"),
  (set(["intim","soft"]),set(["f"]),"ina")
]


# processedTaskList = [set(["intim","soft"]),set(["hans","julia"]),"der hans küsst die julia"]

def solve_stepp(participants,roles, tags,players,result):
  if( len(participants) == len(roles) ):
    result.append(participants)
    return

  role = roles[len(participants)]

  for player in players:
    if player[2] in participants:     # Ist bereits involviert
      continue
    if not(tags.issubset(player[0])): # tags passen nicht
      continue
    if not(role in player[1]) :       # Rollen Passen nicht
      continue

    np = list(participants)
    np.append(player[2])
    solve_stepp(np,roles, tags,players,result)
    

def solve(roles, tags,players):
  result = []
  solve_stepp( [], roles, tags, players, result)
  return result

def processTask(task,players,result):
  roles, tags, text = task
  settings = solve(roles,tags,players)
  for setting in settings:
    nt = text.format(*setting)
    result.append((tags,setting,nt)) 

def processTasks(tasks,players):
  result = []
  for task in tasks:
    processTask(task,players,result)
  return result


def loadList(targetList,fileName):

  with open(fileName) as data_file:   
    data = json.load(data_file)   
  for e in data["data"]:
    targetList.append((e["needs"],set(e["tags"]),e["text"]))


def taskSet(taskList,playerList):
  processedTaks = processTasks(taskList,playerList)
  return processedTaks

def questionSet(questionList,playerList):
#  global taskList
#  processedTaks = processTasks(taskList,playerList)
  return []
