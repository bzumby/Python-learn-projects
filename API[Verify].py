import re
from urlparse import urlparse

x = "https://api.namecheap.com/xml.response?ApiUser=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=192.168.1.109&Years=2&Type=PositiveSSL"
n = urlparse(x)

if n.netloc != "api.namecheap.com":
  print "Expected API link: 'https://api.namecheap.com'"
elif 'ApiUser=' not in n.query:
  print "Parameter 'ApiUser' is missing \n the syntax is: 'ApiUser=apiuser'"
  
v = re.search(r'&ApiKey=([\d\w]+)', x)
# v.group(1) is the key Value 31char long

if len(v.group(1)) != 31:
  print "The API key Value is wrong"
