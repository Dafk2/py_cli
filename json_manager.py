import json
import os

def redJson ():
  if not os.path.isfile('data.json'):
    with open('data.json', 'w') as file:
      json.dump([], file)

  with open('data.json', 'r') as file:
    data = json.load(file)
    return data

def writeJson (data):
  with open('data.json', 'w') as file:
    json.dump(data, file)    