from urlparse import urlparse

x = "https://api.namecheap.com/xml.response?ApiUser=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=192.168.1.109&Years=2&Type=PositiveSSL"
n = urlparse(x)

if n.netloc != "api.namecheap.com":
  print True

print n.scheme
