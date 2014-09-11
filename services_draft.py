import json
#TODO: split 'services_draft.py' into 'services.py' and 'classes.py' once things work a bit

def _questions():
  questionsList = [
    "What is a page range?# \n (which takes a stream id and a page range and returns a list of URLs to images and a page range)",
    "For page list, does the order matter, i.e. can it be a hash/set internally",
    "When two things are returned should both be in one json object or one object per string, e.g. two lists of streams",
    "Is json to be passed between python functions as well? Is it efficient for each function to read DB for an ID",
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

############# classes ########################
'''
Class user
* self streams
  "streams I own"
* subscribed streams
  "streams I subscribe to"

  methods:
    add_stream(name)
    rem_stream(name)
    get_stream(name)

Class stream

'''

class User:
  def __init__(self,id):
    self.id = id

    # list to hold stream objects
    self.streams_mine = []
    self.streams_subscribed = []


  def listConcat(self,listName,streamId):
    if(0):
      print("listConcat called on id(self.streams_mine) == " + str(id(self.streams_mine)))
    if(type(streamId) is list):
      listName.extend(streamId) # note to self: this definitely updates by reference
    elif(type(streamId) is str):
      listName.append(streamId)
    else:
      print("cannot append:")
      print(streamId)
    return

  # add streams
  def stream_add(self,streamId):
    if(0):
      print("stream_add called on id(self.streams_mine) == " + str(id(self.streams_mine)))
      print("calling self.listConcat:")
    self.listConcat(self.streams_mine,streamId)
    
  def stream_sub(self,streamId):
    self.listConcat(self.streams_subscribed,streamId)

  # access streams
  #TODO: return self by default
  # future: 'get_streams_mine' calls 'get_stream'
  # future: 'get_streams_subscribed' calls 'get_stream'
  def get_stream(self,*args,**kwargs):
    streamType = ''
    if(kwargs):
      if(kwargs['type']):
        streamType = kwargs['type']
    if(args):
      width = args[0]
  #</def get_stream>

  def get_streams_mine(self):
    #return get_stream(type=mine)
    return self.streams_mine
  def get_streams_subscribed(self):
    #return get_stream(type=subscribed)
    return self.streams_subscribed

  # remove streams
  def stream_rm(self,streamId):
    #TODO: implement as a set if possible to avoid duplicate streams
    self.streams_mine.remove(streamId)
  def stream_unsub(self,streamId):
    #TODO: implement as a set if possible to avoid duplicate streams
    self.streams_subscribed.remove(streamId)



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

#< def getObjectFromStorage>
#TODO: make generic for retrieving stream as well
#TODO: dump/retrieve json storage file with userids 
def getObjectFromStorage(userId):
  # in lieue of db connection

  # two methods, both are fake about the id

  from services_tb import createTestUsers
  tmpUser = createTestUsers(1)
  tmpUser.id = userId

  from services_tb import genRandomUser
  testUser = genRandomUser(**{
      'seed':userId, 
      'mystream':['sheets','pillows'],
      'theirstream':'phantoms',
    })
  return testUser
#</def getObjectFromStorage>


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
  
  userObject = getObjectFromStorage(userid)
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



