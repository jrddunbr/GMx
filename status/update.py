#!/usr/bin/python3

from mcstatus import MinecraftServer
from time import sleep
from pprint import pprint

server = MinecraftServer("gmx.cosi.clarkson.edu", 2424)

outputName = "../index.html"

templateName = "templates/index.html"

HTML = ""

f = open(templateName)
for line in f:
    HTML += line
f.close()

def uuidToImgURI(uuid):
    return "https://crafatar.com/avatars/{}.png".format(uuid)

def makeTable(playerList):
    text = "<table>\n"
    for player in playerList:
        name = player[0]
        uuid = player[1]
        text += "<tr>\n"
        text += "<td>{}</td><td><img width=32px src=\"{}\" alt=\"{}\"></img></td>\n".format(name, uuidToImgURI(uuid), name)
        text += "</tr>\n"
    text += "</table>\n"
    return text

def renderHTML(content):
    output = ""
    outFile = open(outputName, "w")
    for line in HTML.split("\n"):
        if "CONTENT" in line:
            output += content + "\n"
        else:
            output += line + "\n"
    outFile.write(output)
    outFile.close()

while 1:
    playerList = [] # list of pairs of ("name", "uuid")

    status = server.status()
    for player in status.players.sample:
        playerList.append((player.name, player.id))

    output = "<p class=\"indent\">Number of Players Online: {}</p>\n".format(status.players.online)
    output += makeTable(playerList)

    renderHTML(output)
    sleep(5)
