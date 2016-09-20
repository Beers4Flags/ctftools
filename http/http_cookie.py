import httplib
import re
import urllib2
import urllib
import base64
import cookielib

#http://challenge01.root-me.org/programmation/ch7/

#<img src="data:image/png;base64,___"
cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]
opener = urllib2.build_opener(*handlers)

def fetch(uri):
    req = urllib2.Request(uri)
    return opener.open(req)

def post(uri, data):
    req = urllib2.Request(uri, data)
    req.get_method = lambda: 'POST'
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    return opener.open(req)

def dump():
    for cookie in cookies:
        print cookie.name, cookie.value

res = fetch("uri")
res = res.read()

params = urllib.urlencode({'metu': value, 'submit': 'Try'})
response = post("uri", params)
print response.read()
