import random
import urllib
import urllib2
import threading
import time


def script(interval, id):
    steps = range(1, 10000)
    for step in steps:
        data = {}
        url = "url"
        headers = {'content-type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Token token'}
        data = urllib.urlencode(data)
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req, timeout=30)
        print response.read()
        time.sleep(interval)


def init():
    # interval http query
    INTERVAL = 1

    FROM = 1
    TO = 500

    list_driver = range(FROM, TO)
    for id in list:
        time.sleep(INTERVAL)
        t = threading.Thread(
            target=script, args=(INTERVAL, id))
        t.start()

init()
