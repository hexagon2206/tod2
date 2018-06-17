import http.server
import socketserver
import random

def newUrl(subHandlers): 
  while True:
    toret = str(random.randint(1, 1000000))
    if not toret in subHandlers:
      return toret

def parsePara(string):
  res={}
  paras = string.split("&")
  for val in paras:
    data = val.split("=",1)
    if len(data) == 1 :
      res[data[0]]=None
    else:
      res[data[0]]=data[1]
  return res

def error(requestData,data):
  return 404,'text/html',b"not found" 

def displayDict(path,para,dictionary):
  html="{} :<br>".format(path)
  for entry in dictionary:
    text = entry
    if para :
      url= "{}/{}?{}".format(path[1:],text,para)
    else:
      url= "{}/{}".format(path[1:],text)

    html += "<a href=\"{}\">{}</a><br>\n".format(url,text)

  return 200,'text/html',html.encode('ascii')

class simpleHandler(http.server.BaseHTTPRequestHandler):
  #Handler for the GET requests
  def do_GET(self):

    pathRaw = self.path.split("?",1)
    para = ""
    if len(pathRaw) > 1 :
      para = pathRaw[1]
    path = pathRaw[0].split("/")[1:]
    res = root
    for step in path:
      res = res.get(step,(error,None))
      if not type(res) == dict :
        break;


    if type(res) == dict :
      code,contentType,html = displayDict(pathRaw[0],para,res)
    else:
      handler,data = res
      code,contentType,html = handler((pathRaw,para),data)

    self.send_response(code)
    self.send_header('Content-type',contentType)
    self.end_headers()
    # Send the html message
    self.wfile.write(html)
    return

root = {}
root[""] = root
def serve(PORT = 1337):
  with socketserver.TCPServer(("", PORT), simpleHandler) as httpd:
    httpd.allow_reuse_address = True
    httpd.serve_forever()
