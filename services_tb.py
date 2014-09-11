#TODO: 
# read https://developers.google.com/appengine/docs/python/tools/localunittesting

import json

from pprint import pprint
import random
from ipdb import *

'''
test the services and classes
'''
from services_draft import *

'''
test the services
import services.py
'''
'''
test the classes
import classes.py
'''


# create user
def genRandomUser(**kwargs):
  # create random id or name
  _seed = random.randint(0,1000000)
  paramList = [
      #"seed",
      "mystream",
      "theirstream",
      ]
  #for arg in paramList:
  #  if(arg in kwargs):
  if('seed' in kwargs):
    _seed = kwargs['seed']
  # use the seed
  idRand = str(_seed)

  randomUser = User(idRand)

  if('mystream' in kwargs):
    randomUser.stream_add(kwargs['mystream'])
  if('theirstream' in kwargs):
    randomUser.stream_sub(kwargs['theirstream'])
  return randomUser

#< def createTestUsers>
#TODO: potentially change to create several users
#TODO: test feasibility of merge with 'genRandomUser'
def createTestUsers(amount):
  verbose = 0
  # initialise a user with parameters as a simple doa test
  if(verbose == 1):
    print("creating a test user")
  # mystream is a list of stream names
  # theirstream is a string
  testUser = genRandomUser(**{
    'mystream':['horses','armadillos'],
    'theirstream':'ducks'
    })
  # print out simple data
  if(verbose == 1):
    pprint(testUser)
    print("id:" + str(testUser.id))
    print("mystream:" + ' '.join(testUser.get_streams_mine()))
    print("theirstream:" + ' '.join(testUser.get_streams_subscribed()))


  #TODO: potentially return list of users 
  return testUser
#</def createTestUsers>

def getJson(jsonStr):
  try:
    jsonDict = json.loads(jsonStr)
  #except ValueError, e:
  except TypeError, e:
    print(e.message)
    return False
  return jsonDict

#TODO: generate a bunch of users, then let 'manage' look up user object based on id
def main():
  # initialise a user as a simple doa test
  tmpUser = createTestUsers(1)

  #TODO: put the unit test stuff here
  manageJson = manage(tmpUser)
  # make sure json is correct
  if getJson(manageJson):
    print("json string is valid")
  # to store back into dict:
  # json.loads(manageJson)
  else:
    # errorList.append('json string has issues:")
    print("-E-: json string has issues:")
  print("raw json:")
  print(manageJson)
  ## print the dict if it exists
  #print("pretty json:")
  #print(manageJson)
  #TODO: check that the json for 'manage' has two lists of streams (idea: use the dict conversion for now)
  #TODO: find way to check types within json string


  return

# call main
main()



'''
http://stackoverflow.com/a/1381652
How do I close a single buffer (out of many) in Vim?

:bw

Like |:bdelete|, but really delete the buffer.

:bd

Unload buffer [N] (default: current buffer) and delete it from the buffer list. If the buffer was changed, this fails, unless when [!] is specified, in which case changes are lost. The file remains unaffected.

'''
