"""
This unit test checks the listenformessage() API call to make sure it raises
the correct exceptions.
"""

#pragma repy
#pragma repy restrictions.twoports

def trylisten(args, expected, errstr):
  try:
    s = listenformessage(args[0], args[1])
  except Exception, e:
    if type(e) is not expected:
      log("wrong exception for: " + errstr,'\n')
      log(str(e),'\n')
      log(str(type(e)),'\n')
  else:
    s.close()
    log("no exception for: " + errstr,'\n')

s1 = listenformessage('127.0.0.1', 12345)
trylisten(('127.0.0.1', 12345), AlreadyListeningError, \
    "trying to bind an address more than once")
s1.close()

for addr in [(5, 5), \
    ("127.0.0.1", None), \
    ("1...", 5), \
    ("127.0.0.1", 65536), \
    ]:
  trylisten(addr, RepyArgumentError, "invalid local addr")

trylisten(("8.8.4.4", 12345), AddressBindingError, "invalid local ip")
trylisten(("127.0.0.1", 12347), ResourceForbiddenError, "local port not allowed")

