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

res = fetch("http://challenge01.root-me.org/programmation/ch7/")
res = res.read()

p = re.compile('.*base64,(.*)" /><br/>.*')
d=p.sub(r'\1', res)
f = open("qr.png", 'w')
f.write(base64.b64decode(d))
f.close()
#image saved.

from PIL import Image
import zbarlight
imflag = Image.open("flag.png")
flag = imflag.load()
im = Image.open("qr.png")
pix = im.load()
height,width = im.size

for i in range(0,height):
  for j in range(0,width):
    s1,s2,s3 = flag[i,j]
    #s2 = flag[i,j]
    if s2 <= 150:
      pix[i,j] = 0,0,0

im.save("qrblack.png")


img = Image.open("qrblack.png").transpose(Image.FLIP_LEFT_RIGHT)

res = zbarlight.scan_codes('qrcode', img)
print res[0][11:]

params = urllib.urlencode({'metu': res[0][11:], 'submit': 'Try'})
response = post("http://challenge01.root-me.org/programmation/ch7/", params)
print response.read()
