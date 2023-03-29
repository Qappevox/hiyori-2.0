import os
import json
from json import JSONDecodeError
names = []
scripts = []
script = """"
"""
def jsonParse():
    global names, script
    with open(os.path.realpath(getDirectory())) as s:
        s = json.load(s)
        objects = s["objects"]
        indexlen = 0
        for i in objects:
            name = objects[indexlen]["name"]
            
            if objects[indexlen]["visible"] == True or objects[indexlen]["visible"] == False:
                scripts.append(str(objects[indexlen]["visible"]) + "//from getSource.py")
            else:
                script = script + objects[indexlen]["visible"]["script"]
                scripts.append(script+ "//from getSource.py" )
            script = """ """
            names.append(name)
            indexlen += 1
      
def getDirectory():
    path =__file__.replace(__file__.split("\\")[-1], "")
    path = path + "scene.json"
    return path

def main():
    jsonParse()
    print(names)
    for name in names:
        index = names.index(name)
        jsfile = names[index] + ".js"
        jsfile = str(jsfile)
        print(jsfile)
        open(jsfile, "x")
        with open(jsfile, "w") as d:
            d.write(str(scripts[index]))
            d.close()
        print(scripts[index])
      
main()
