import re
from urlparse import urlparse, parse_qs

x = "https://api.namecheap.com1/xml.response?ApiUser1=apiexample&ApiKey=56b4c87ef4fd49cb96d915c0db68194&UserName=apiexample&Command=namecheap.ssl.create&ClientIp=1923.168.1.109&Years=5&Type=PositiveSSL1"
x = x.lower()
n = urlparse(x)
#list of acceptable SSL types in URL encoding
SSLtypes = ['positivessl+multi+domain', 'multi+domain+ssl', 'ev+multi+domain+ssl', 'unified+communications', 'positivessl']
#dict with key-value API call parameters
params = parse_qs(n.query)


# check of the API link (domian)
if n.netloc != "api.namecheap.com":
    print "Expected API link: 'https://api.namecheap.com'\n"
# check if ApiUser argument is present in a Call
if 'ApiUser=' not in n.query:
    print "Parameter 'ApiUser' is missing \n the syntax is: 'ApiUser=apiuser'\n"

if "Command=namecheap.ssl.create" not in n.query:
    print "Please verify the API command in use. The syntax is: \n 'Command=namecheap.ssl.create'\n"

#THINK ABOUT IT LATER
# check the ApiKey length
if len(params['apikey'][0]) != 31:
    print "The API key Value is wrong\n"

#check of the SSL type in API call
if params["type"][0] not in SSLtypes:
    print "SSL Type is invalid. Acceptable values are: \n PositiveSSL+Multi+Domain \n Multi+Domain+SSL \n EV+Multi+Domain+SSL \n Unified+Communications \n PositiveSSL\n"

#pattern of an IP address acceptable - xxx.xxx.xxx.xxx
ip_pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
#var with the value of a ClientIP from the given API call
clientIP = params["clientip"][0]

#shit this was hard
#var with comparison of the given IP address against the pattern.
ipcheck = ip_pattern.match(clientIP)

if not ipcheck:
    print "Client IP address is invalid\n"

#check the 'years' paramater
years = [1,2,3]
if int(params["years"][0]) not in years:
    print "The amount years is invalid"
