import json
import random
import time
import os
import logging

logging.basicConfig(filename='log.log', level=logging.DEBUG)

#####################################
# NOTES:                            #
# Clust. Name:      Cluster0        #
# Database Name:    breadapi        #
# Collection Name:  breads          #
# DB and Col. Name: breadapi.breads #
#####################################


def get(object="missing"):
    try:
      print(object)
      object = int(object)
      print(object)
    except ValueError:
      return{"success": "false", "name": "Must be integer!"}
    print("get")
    print(f"object is {object}")
    if object == "missing":
        return {
            "success": "false",
            "name":
            "object cannot be None! Please specify the object you want..."
        }

    else:
        if int(object) > 110:
            return {
                    "success": "false",
                    "name": "Messier only found 110 objects! You are over 110!"
                }
        elif int(object) <= 0:
            return {
                    "success": "false",
                    "name": "Object cannot be 0 or below!"}
                  
        else:
            try:
              object = f"M{object}"
              print(object)

              with open("./data/messier.json", "r") as f:
                  data = json.load(f)
                  print(data[object])
                  return data[object]
            except Exception as e:
              return {"success": "false", "name": e}
            # get content and print it
        # return {"success": "false", "name": "not found :o"}

"""
def vote(name):
  breadtovote = get(name=name)
  voteaccept,err = canVote(breadtovote)
  if voteaccept:
    breadtovote["rating"] += 1.0
    breads.replace_one({"name":name},breadtovote)
    breadtovote["success"]= True
    return breadtovote
  else:
    return err

def canVote(bread):
  with open("./data/vote.json","r") as file:
    votesjson = json.load(file)
  name = bread["name"]
  now = time.time()
  if name in votesjson:
    if now-votesjson[name]["time"] > 30:
      votesjson[name]["votes"] = 0
      with open("./data/vote.json", "w") as file:
        json.dump(votesjson, file)
      return True,None
    elif votesjson[name]["votes"] < 5:
      votesjson[name]["votes"] += 1
      with open("./data/vote.json", "w") as file:
        json.dump(votesjson, file)
      return True,None
    else:
      return False,{"success":False,"error":"cooldown"}
  else:
    votesjson[name] = {
      "votes":0,
      "time":now
    }
    with open("./data/vote.json", "w") as file:
      json.dump(votesjson, file)
    return True,None


def leaderboard(order="1"):
  if order == "-1":
    bread = breads.find().sort("rating",pymongo.DESCENDING)   
  elif order == "1":
    bread =breads.find().sort("rating",pymongo.ASCENDING)
  return list(bread)
"""
