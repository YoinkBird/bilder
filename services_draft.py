#TODO: split 'services_draft.py' into 'services.py' and 'classes.py' once things work a bit
'''
questionsList = [
  "what is a page range?",
  "",
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

  #TODO: return self by default
  #def get_stream(self,*args,**kwargs):
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
  selfStreamList = userid.getStreams(self) # default is self
  otherStreamList = userid.getStreams(subscribed)
  
  # get subscribed streams
  return(selfStreamList, subscribeStreamList)



