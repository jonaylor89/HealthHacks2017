
from urllib.request import urlopen
import urllib
import json
import calendar
import time

from temp_read import read_temperature

url = 'https://healthhacks2017-ec6bf.firebaseio.com/'

postdata = {
    'date' : str(calendar.timegm(time.gmtime())),
    'temp' : str(read_temperature())
}

req = urllib.request(url)
req.add_header('Content-Type', 'application/json')
data = json.dump(postdata)

response = urlopen(req, data)
