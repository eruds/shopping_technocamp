import json

def getData() : 
    f = open("./database.json", "r")
    database = json.load(f)
    return database

# def getUserData() : 

def setDatabase(database) :
    f = open("./database.json", "w")
    json.dump(database, f, indent=4)




