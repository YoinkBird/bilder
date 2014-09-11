import json
#TODO: split 'services_draft.py' into 'services.py' and 'classes.py' once things work a bit

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

#TODO: natively dump json string - just convert 'get_hash_repr'
#TODO: natively import json string
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

  def get_hash_repr(self):
    hashRepr = {
        'userid':self.id,
        'streams_mine':self.streams_mine,
        'streams_subscribed':self.streams_subscribed,
        }
    return hashRepr

