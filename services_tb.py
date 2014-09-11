#TODO: 
# read https://developers.google.com/appengine/docs/python/tools/localunittesting

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
  _seed = 10 * random.random()
  if(kwargs):
    _seed = kwargs['seed']

  # use the seed
  idRand = str(_seed)
  return User(idRand)


def main():
  tmpUser = genRandomUser()

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
