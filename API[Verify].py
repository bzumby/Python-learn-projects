from urlparse import urlparse, urlsplit

x = "https://api.namecheap.com/xml.response?ApiUserq=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=192.168.1.109&Years=2&Type=PositiveSSL"
n = urlparse(x)

if n.netloc != "api.namecheap.com":
  print "Expected API link: 'https://api.namecheap.com'"
elif 'ApiUser=' not in n.query:
  print "Parameter 'ApiUser' is missing \n the syntax is: 'ApiUser=apiuser'"
  
print "\n",n
