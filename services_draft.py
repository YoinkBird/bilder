#from ipdb import *
import json
from services_objects import User
from services_objects import Stream
#TODO: split 'services_draft.py' into 'services.py' and 'classes.py' once things work a bit

def _questions():
  questionsList = [
    "What is a page range? \n# (which takes a stream id and a page range and returns a list of URLs to images and a page range)",
    "For page list, does the order matter, i.e. can it be a hash/set internally",
    "When two things are returned should both be in one json object or one object per string, e.g. two lists of streams",
    "Is json to be passed between python functions as well? Is it efficient for each function to read DB for an ID",
    "add subscribers: Does a stream need to track its subscribers or does this just need to send out an email",
    ]
  questionStr = ''
  questionStr += "\n# < questions>"
  questionsList[0] = '\n# * ' + questionsList[0]
  questionStr += '?\n# * '.join(questionsList)
  questionStr += "\n# </questions>\n"
  print(questionStr)
  return
_questions()

'''
todoList = [
  "ensure all user ids are unique",
  ]
'''

############# services ########################
'''
Write specific services for
* management (in which you take a user id and return two lists of streams)
* create a stream (which takes a stream definition and returns a status code)
* view a stream (which takes a stream id and a page range and returns a list of URLs to images and a page range)
* image upload (which takes a stream id and a file)
* view all streams (which returns a list of names of streams and their cover images)
* search streams (which takes a query string and returns a list of streams (titles and cover image urls) that contain matching text
* most viewed streams (which returns a list of streams sorted by recent access frequency)
* and reporting request.
'''

#< def getJsonDict>
def getJsonDict(jsonStr):
  retJsonDict = {}

  # load the thing
  try:
    jsonObj = json.loads(jsonStr)
  except ValueError, e:
    print(e.message)
    return False
  except TypeError, e:
    print(e.message)
    return False

  # make sure it is a dict
  if(type(jsonObj) is dict):
    retJsonDict = jsonObj
  else:
    print("-E-: no valid json string passed to 'def manage' - after json.loads, type is not any of int,str,dict")
    print(jsonString)

  return retJsonDict
#</def getJsonDict>

#< def readJsonDBFile>
# use dict instead of list to have unique user ids and easylookup
def readJsonDBFile(jsonUserDB):
  userDataDict = {}
  import os.path
  if(os.path.isfile(jsonUserDB)):
    userDataJson = open(jsonUserDB).read()
    userDataDict = json.loads(userDataJson)
    if(not type(userDataDict) is dict):
      print("-E- file is not json dict")
      
  return userDataDict
#</def readJsonDBFile>

#< def putObjectInStorage>
# requesting unique key be passed in to make this object-type agnostic
#   i.e. 'id' is python reserved word, so 'User' should have 'userid' and 'Stream' should have 'StreamID'
# also, what i currently call 'id' is the name, not the db storage id, so this may help eventually in the future
def putObjectInStorage(objectid,objectRef):
  statusCode = 0
  jsonDBfile = 'data.json'

  # read in json "db"
  dbDict = readJsonDBFile(jsonDBfile)

  # add user "key"
  dbDict[objectid] = objectRef.get_hash_repr()

  # dump object string representation to file
  with open(jsonDBfile, 'w') as outfile:  #note: 'w' to overwrite with new dict, 'a' to append if using a list
    # dump json repr of dict to string
    json.dump(dbDict, outfile, sort_keys=True,indent=4)
  return statusCode
#< def putObjectInStorage>

#< def getObjectFromStorage>
def getObjectFromStorage(objectid):
  jsonDBfile = 'data.json'
  dbDict = readJsonDBFile(jsonDBfile)

  if(objectid in dbDict):
    retObject = dbDict[objectid]
  else:
    print("-E-: object not in json db file" + str(objectid))
    retObject = 0

  return retObject
#</def getObjectFromStorage>

#< def getUserObjectFromStorage>
#TODO: make generic for retrieving stream as well
#TODONE: dump/retrieve json storage file with userids 
def getUserObjectFromStorage(userId):
  # in lieue of db connection

  # two methods, both are fake about the id

  from services_tb import createTestUsers
  tmpUser = createTestUsers(1)
  tmpUser.id = userId

  from services_tb import genRandomUser
  # deliberately create user with same id but different data to verify that user data is being looked up correctly
  testUser = genRandomUser(**{
      'seed':userId, 
      'mystream':['sheets','pillows'],
      'theirstream':'phantoms',
    })

  #< old way >
  if(0):
    import os.path
    jsonUserDB = 'data.json'
    if(os.path.isfile(jsonUserDB)):
      del testUser # make sure no remnants of previous methods
      userDataJson = open(jsonUserDB).read()
      userDataDict = json.loads(userDataJson)
      if(type(userDataDict) is dict):
        testUser = User(userId)
        testUser.stream_add(userDataDict[userId]['streams_mine'])
        testUser.stream_sub(userDataDict[userId]['streams_subscribed'])
    del userDataDict
  #</old way >

  del testUser
  userDataDict = getObjectFromStorage(userId)
  if(userDataDict):
    testUser = User(userId)
    testUser.stream_add(userDataDict['streams_mine'])
    testUser.stream_sub(userDataDict['streams_subscribed'])

  return testUser
#</def getUserObjectFromStorage>


#< def manage()>
# (which takes a user id and return two lists of streams)
def manage(jsonString):

  #if(type(jsonString) not str):
    #print("-E-: 'def manage' expects a json-formatted string!")
  # extract from json
  jsonObj = json.loads(jsonString)
  userid = ''
  #TODO: put this in the 'getJson' function
  if(type(jsonObj) is dict):
    if('userid' in jsonObj):
      userid = jsonObj['userid']
  elif(type(jsonObj) is int or type(jsonObj) is str or type(jsonObj) is unicode):
    userid = jsonObj
  else:
    print("-E-: no valid json string passed to 'def manage' - after json.loads, type is not any of int,str,dict")
    print(jsonString)
  
  userObject = getUserObjectFromStorage(userid)
  # test objects
  if(0):
    selfStreamList = userObject.get_streams_mine() # default is self
    otherStreamList = userObject.get_streams_subscribed()
    # non-json return:
    return(selfStreamList, otherStreamList)
    # returns two strings - should the caller expect various returns?
    return(json.dumps(selfStreamList, otherStreamList))

  contentDict = {}
  contentDict['streams_proprietary'] = userObject.get_streams_mine() # default is self
  contentDict['streams_subscribed'] = userObject.get_streams_subscribed()
  
  
  # get subscribed streams
  return(json.dumps(contentDict))
#</def manage>

# function stubs
# TODO: populate below stubs
# NOTE: figure out which functions can inherit from each other

#< def create_stream()>
# (which takes a stream definition and returns a status code)
# "create stream page" shows
# name
# subscribers
# tags
# coverimgurl
def create_stream(streamJson):
  paramsDict = getJsonDict(streamJson)

  # TODO: check input
  # populate with bare minimum
  tmpStream = Stream(paramsDict['streamid'],paramsDict['name'])

  # TODOne: make a dict of params and setters
  #if('tags' in paramsDict):
  #  tmpStream.set_tags(paramsDict['tags'])
  #if('coverimgurl' in paramsDict):
  #  tmpStream.set_tags(paramsDict['coverimgurl'])
  #if('subscribers' in paramsDict):

  setterDict = {
      'tags':tmpStream.set_tags,
      'subscribers':tmpStream.subscriber_add,
      'coverimgurl':tmpStream.set_cover_url,
    }
  for param in paramsDict:
    if(param in setterDict):
      setterDict[param](paramsDict[param])
  # </object created>

  returnCode = putObjectInStorage(tmpStream.streamId,tmpStream)
    
  return(json.dumps('replace this dummy with a real boy!'))
#</def create_stream>

#< def view_stream()>
# (which takes a stream id and a page range and returns a list of URLs to images and a page range)
def view_stream():
  return(json.dumps('replace this dummy with a real boy!'))
#</def view_stream>

#< def image_upload()>
# (which takes a stream id and a file)
def image_upload():
  return(json.dumps('replace this dummy with a real boy!'))
#</def image_upload>

#< def view_streams_all()>
# (which returns a list of names of streams and their cover images)
def view_streams_all():
  return(json.dumps('replace this dummy with a real boy!'))
#</def view_streams_all>

#< def search_streams>
# (which takes a query string and returns a list of streams (titles and cover image urls) that contain matching text)
def search_streams():
  return(json.dumps('replace this dummy with a real boy!'))
#</def search_streams>

#< def most_viewed_streams()>
# (which returns a list of streams sorted by recent access frequency)
def most_viewed_streams():
  return(json.dumps('replace this dummy with a real boy!'))
#</def most_viewed_streams>

#< def reporting()>
def reporting():
  return(json.dumps('replace this dummy with a real boy!'))
#</def reporting()>




