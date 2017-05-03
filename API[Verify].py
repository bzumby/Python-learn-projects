import re
import socket
from urlparse import urlparse, parse_qs

#API call example:
# https://api.namecheap.com/xml.response?ApiUser=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=192.168.1.109&Years=2&Type=PositiveSSL

x = raw_input("API call, please ""\n")
x = x.lower()
n = urlparse(x)
#list of acceptable SSL types in URL encoding
SSLtypes = ['positivessl+multi+domain', 'multi+domain+ssl', 'ev+multi+domain+ssl', 'unified+communications', 'positivessl']
#dict with key-value API call parameters
params = parse_qs(n.query)
ip_addr = params['clientip'][0]

#print "\n"

error_mess = {'apiuser':'ApiUser is invalid', 'apikey':'ApiKey is invalid', 'username':'Username is invalid', 'command':'Command is invalid', 'clientip':'ClientIP is invalid', 'years':'Parameter "Years" is invalid', 'type':'Type is invalid'}

#comparing the Key parameters from ApiCall with the correct Key values of error_mess dict
for key in error_mess:
  if key not in params:
    print "\n", error_mess[key]
    

try:
    socket.inet_aton(ip_addr)
except socket.error:
    print "Value 'ClientIP' is incorrect: \n'{}'".format(ip_addr)

    
if params['type'] not in SSLtypes:
    print "SSLtype value is invalid:'{}'".format(params['type'][0])
    
