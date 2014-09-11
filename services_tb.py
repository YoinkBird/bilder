#TODO: 
# read https://developers.google.com/appengine/docs/python/tools/localunittesting

import json

from pprint import pprint
import random
from ipdb import *

'''
test the services and classes
'''
from services_draft import manage
from services_draft import putObjectInStorage
from services_objects import User

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

#< def genRandomWord>
def genRandomWordList(listSize,wordLen):
  retList = []

  import os.path
  # from http://a-z-animals.com/animals/endangered/
  filename = 'tests/animals.txt'
  if(os.path.isfile(filename)):
    #animalFile = open('animals.txt').read()
    # http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array#comment28643126_3277515
    topicList = [line.rstrip('\n') for line in open(filename)] 
    print("")

  # make first item of list human-readable
  # my choices
  topicList.extend([
      "armadillos",
      "bats",
      "bandicoot",
      "cincilla",
      "ducks",
      "horses",
      "pangolins",
      "zephyr",
      "zebra",
      ])
  retList.append(random.choice(topicList))
  listSize -= 1 # added one element

  # adopted from: http://stackoverflow.com/a/2257449
  import string
  # lambda to return 'x' digits
  wordGen = lambda x : ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(x)])

  for num in range(listSize):
    retList.append(wordGen(wordLen))
  return retList
#</def genRandomWord>

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
    'theirstream':'ducks',
    })

  # regenerate with random data
  testUser = genRandomUser(**{
    'mystream':genRandomWordList(1,8),      # one word
    'theirstream':genRandomWordList(3,8),   # three words
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

# TODO: generate a bunch of users and store in fake db (json file) so that id-based retrieval more realistic
# TODO: test: functions should reject non-strings, 
#       i.e. this should fail because of int:    manageJson = manage(tmpUser.id)
def main():
  # initialise a user as a simple doa test
  # to put on airs of doing things correctly, this user's id will be passed to the 'manage' function
  tmpUser = createTestUsers(1)

  # dump user to file
  putObjectInStorage(tmpUser.id,tmpUser)

  # each testParamsDict defines input and output params for one function
  testDataList = []
  testDataList.append( {
    'function' : manage,
    'jsonIn'   : json.dumps({'userid':tmpUser.id}),
    #'jsonOut'  : '', # TODO
    'jsonOut'  : json.dumps({
      'streams_subscribed':tmpUser.get_streams_subscribed(),
      'streams_proprietary':tmpUser.get_streams_mine(),
      }),
    }
  )

  #TODO: put the unit test stuff here
  for testParamsDict in testDataList:
    funcName = testParamsDict['function']
    print("")
    print("-I-: testing " + str(funcName))

    #testJsonIn = funcName(testParamsDict['jsonIn']) # test the defined function against the defined json string
    testJsonExpected = testParamsDict['jsonOut'] # test the defined function against the defined json string

    # run function, capture output
    testJsonReturned = funcName(testParamsDict['jsonIn']) # test the defined function against the defined json string
    # make sure function returns something
    if(testJsonReturned):
      # make sure json is correct
      if getJson(testJsonReturned):
        print("json string is valid")
      # to store back into dict:
      # json.loads(testJsonReturned)
      else:
        # errorList.append('json string has issues:")
        print("-E-: json string has issues:")
      print("raw json:      " + testJsonReturned)
      # TODO: this won't work because 'manage' can't access our created user and therefore creates it's own
      if(testJsonReturned == testJsonExpected):
        print("-I-: output json matches test expectation!")
      else:
        #TODO: format such that the 'raw json' is directly above the 'expected json'
        print("expected json: " + testJsonExpected)
        print("-E-: output json does not match test expectation")
      ## print the dict if it exists
      #print("pretty json:")
      #print(testJsonReturned)
      #TODO: check that the json for 'manage' has two lists of streams (idea: use the dict conversion for now)
      #TODO: find way to check types within json string
    elif(not testJsonReturned):
      print("-E-: doa - function is returning nothing")
  #</testloop>


  return

# call main
#Note: this ensures that main won't be called if another file imports this one. 
# This is anecdotal, I have not looked up a definition of this
# found on:
# https://developers.google.com/appengine/docs/python/tools/localunittesting#Python_Setting_up_a_testing_framework
if __name__ == '__main__':
  main()



'''
VIM TIPS
http://stackoverflow.com/a/1381652
How do I close a single buffer (out of many) in Vim?

:bw

Like |:bdelete|, but really delete the buffer.

:bd

Unload buffer [N] (default: current buffer) and delete it from the buffer list. If the buffer was changed, this fails, unless when [!] is specified, in which case changes are lost. The file remains unaffected.
==================

  #VIM: help non-greedy ; see http://stackoverflow.com/a/1305957
  #VIM: add the quotes for hash key - nongreedy chars within [] :   s#\[\zs.\{-}\ze\]#'&'#g
  # this 
  manageJson = testParamsDict[function](testParamsDict[jsonIn]) # test the defined function against the defined json string
  # becomes
  manageJson = testParamsDict['function'](testParamsDict['jsonIn']) # test the defined function against the defined json string

==================
turn 'def function' into 
s#\zs.*\ze#\#< &>\r&():\r  return\r\#</&>#g
#< def function>
def function():
  return
#</def function>

==================
run on save
http://www.commandlinefu.com/commands/view/6515/using-vim-to-save-and-run-your-python-script.
http://stackoverflow.com/a/4628210
:autocmd BufWritePost * !run_tests.sh <afile>

# remove the setting with 'autocmd!'
:autocmd! BufWritePost * !run_tests.sh <afile>
'''
