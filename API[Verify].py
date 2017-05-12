import re, sys
import socket
from urlparse import urlparse, parse_qs

#API call example:
# https://api.namecheap.com/xml.response?ApiUser=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=192.168.1.109&Years=2&Type=PositiveSSL

x = raw_input("API call, please ""\n")
x = x.lower()
n = urlparse(x)
#list of acceptable SSL types in URL encoding
SSLtypes = ['positivessl multi domain', 'multi domain ssl', 'ev multi domain ssl', 'unified communications', 'positivessl']
#dict with key-value API call parameters
params = parse_qs(n.query)
#ip_addr = params['clientip'][0]

print "\n"

error_mess = {'apiuser':'Parameter ApiUser is invalid\n', 'apikey':'Parameter ApiKey is invalid\n', 'username':'Parameter Username is invalid\n', 'command':'Parameter Command is invalid\n', 'clientip':'Parameter ClientIP is invalid\n', 'years':'Parameter "Years" is invalid\n', 'type':'Parameter Type is invalid\n'}


#APIurl synth check
if "?" in x:
  if x.split('?')[0] != "https://api.namecheap.com/xml.response":
    print "\nInvalid URL %s" %x.split('?')[0], "\nExpected: 'https://api.namecheap.com/xml.response?'"
  if x.endswith('&'):
    print "API call should not end with '&'"
  if '==' in x:
    print "URL contains an extra '=' "
else:
  print "Character '?' is missing in URL"
  sys.exit()

if " " in x:
  print "ApiCall contains an extra space"
  

#comparing the Key parameters from ApiCall with the correct Key values of error_mess dict
for key in error_mess:
  if key not in params.keys():
    print "\n", error_mess[key]
    
if params['command'][0] != "namecheap.ssl.create":
  print "\nCommand is invalid or missing"
    
#IP validity check
try:
  ip_addr = params['clientip'][0]
  socket.inet_aton(ip_addr)
except socket.error:
    print "'ClientIP'value is incorrect: '{}'".format(ip_addr), "\n"

#SSLtype value check    
if str(params['type'][0]) not in SSLtypes:
    print "SSLtype value is invalid:'{}'".format(params['type'][0])
    
#Years value check
if int(params['years'][0]) not in range(1,4):
  print "Velue of 'Years' is invalid"
else:
  if params['type'][0] == SSLtypes[2] and int(params['years'][0]) not in range(1,3):
    print "Value of 'Years' for EV SSL is invalid: '%s' Expected: '1' or '2'" %params['years'][0]
    
#APIkey value check
if len(params['apikey'][0]) != 31:
  print "ApiKey value is incorrect. Please double-check yur ApiKey"
  
print params
