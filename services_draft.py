import json
#TODO: split 'services_draft.py' into 'services.py' and 'classes.py' once things work a bit
'''
questionsList = [
  "what is a page range?",
  "for page list, does the order matter",
  ]

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

  # add streams
  def stream_add(self,streamId):
    self.streams_mine.append(streamId)
    
  def stream_sub(self,streamId):
    self.streams_subscribed.append(streamId)

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



def manage(userid):

  # THOUGHTS: how to set up user to contain streams
  # ramble:
  #   userid.getUserStreams(self) # default is self
  #   userid.getSubscribedStreams(subscribed)
  # get user streams
  #selfStreamList = userid.get_streams_mine() # default is self
  #otherStreamList = userid.get_streams_subscribed()
  #return(json.dumps(selfStreamList, otherStreamList))

  contentDict = {}
  contentDict['streams_proprietary'] = userid.get_streams_mine() # default is self
  contentDict['streams_subscribed'] = userid.get_streams_subscribed()
  
  
  # get subscribed streams
  return(json.dumps(contentDict))



