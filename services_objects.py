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
* basic attribs:
  name
  tags
  cover img url
  subscribers - maybe; could also simply need to email people. play it safe...

'''

#TODO: natively dump json string - just convert 'get_hash_repr'
#TODO: natively import json string
#< class User>
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
#</class User>

#< class Stream>
class Stream:
  def __init__(self,streamId,streamName):
    self.streamId = streamId
    self.streamName = streamName
    self.viewCounter = 0
    self.coverImgUrl = 'blank'
    self.imageList = []
    self.subscriberList = []
    self.tagList = []


  # https://docs.python.org/2/reference/datamodel.html#object.__repr__
  # TODO: this should look like a valid Python expression that could be used to recreate an object with the same value
  # this seems to allow typing of the instantiation without args
  def __repr__(self):
    #strValue = "name: " + self.name + " gpa: " + str(self.gpa) + " age: " + str(self.age)
    strValue = "{\
        'streamId':"    + str(self.streamId) + ",\
        'viewCounter':" + str(self.viewCounter) + ",\
        'coverImgUrl':" + self.coverImgUrl + ",\
        'imageList':"   + str(self.imageList) + "}"
    return strValue

  def get_hash_repr(self):
    return self.__dict__
  
  #< cover image>
  def set_cover_url(self,urlStr):
    retcode = -1
    # TODO: check if valid url
    if( isinstance(urlStr, basestring)):
      self.coverImgUrl = urlStr
      retcode = 0
    else:
      print("-E-: must pass url as string")
    return

  def get_cover_url(self):
    return self.coverImgUrl
  #</cover image>

  #< tags>
  # store tags as set but convert to list along the way to avoid duplicates
  def set_tags(self,tagListStr):
    #self.tagSet.add(tagListStr)
    #TODO: parse tags into a list or set or whatnot
    #NOTE: right now it's just string literal
    tagListTmp = tagListStr.split(' ')
    tmpSet     = set(tagListTmp)
    tagListTmp = list(tmpSet)
    self.tagList.extend(tagListTmp)
    return

  def get_tags(self,tagSet):
    return list(self.tagSet)
  #</tags>

  #< subscribers>
  def listConcat(self,listName,userId):
    if(0):
      print("listConcat called on id(self.subscriberList) == " + str(id(self.subscriberList)))
    if(type(userId) is list):
      listName.extend(userId) # note to self: this definitely updates by reference
    # http://stackoverflow.com/a/1303266
    elif( isinstance(userId, basestring)):
      listName.append(userId)
    else:
      print("cannot append:")
      print(userId)
    return

  # add subscriber
  # NOTE: either we need to add users, i.e. registered users, or just emails
  #       just add emails for now to make life easier
  #       otherwise system would create a new user for each unknown email that is added as subscription
  def subscriber_add(self,userId):
    if(0):
      print("add_subscriber called on id(self.subscriberList) == " + str(id(self.subscriberList)))
      print("calling self.listConcat:")
    import re
    userIdList = re.split('\s|,|;|\n',str(userId))
    self.listConcat(self.subscriberList,userIdList)

  # TODO? ?remove subscriber?
  def subscriber_rem(self,userId):
    #TODO: implement as a set if possible to avoid duplicate streams
    self.subscriberList.remove(userId)
  #</subscribers>


#</class Stream>

