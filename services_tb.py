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


def main():
  # initialise a user as a simple doa test
  #tmpUser = genRandomUser()
  # initialise a user with parameters as a simple doa test
  tmpUser = genRandomUser(**{
    'mystream':['horses','armadillos'],
    'theirstream':'ducks'
    })
  # print out simple data
  pprint(tmpUser)
  print("id:" + str(tmpUser.id))
  print("mystream:" + ' '.join(tmpUser.get_streams_mine()))
  print("theirstream:" + ' '.join(tmpUser.get_streams_subscribed()))

  #TODO: put the unit test stuff here
  manageJson = manage(tmpUser)
  print("raw json:")
  print(manageJson)
  print("pretty json:")
  print(manageJson)
  # to store back into dict:
  # json.loads(manageJson)


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
