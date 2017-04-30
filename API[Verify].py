import re
from urlparse import urlparse, parse_qs

x = "https://api.namecheap.com/xml.response?ApiUser=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=192.168.1.109&Years=2&Type=Posi1tiveSSL"
n = urlparse(x)

# v.group(1) is the key Value 31char long
v = re.search(r'&ApiKey=([\d\w]+)', x)

#check of the API link (domian)
if n.netloc != "api.namecheap.com":
  print "Expected API link: 'https://api.namecheap.com'"
#check if ApiUser argument is present in a Call
elif 'ApiUser=' not in n.query:
  print "Parameter 'ApiUser' is missing \n the syntax is: 'ApiUser=apiuser'"

elif "Command=namecheap.ssl.create" not in n.query:
  print "Please verify the API command in use: \n 'Command=namecheap.ssl.create'"
  
#check the ApiKey length
elif len(v.group(1)) != 31:
  print "The API key Value is wrong"


SSLtypes = ['PositiveSSL+Multi+Domain', 'Multi+Domain+SSL', 'EV+Multi+Domain+SSL', 'Unified+Communications']

P1 = parse_qs(n.query)
if P1["Type"] not in SSLtypes:
  print "SSL Type is invalid. Possible values are: \n PositiveSSL+Multi+Domain \n Multi+Domain+SSL \n EV+Multi+Domain+SSL \n Unified+Communications"


