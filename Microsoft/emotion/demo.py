import httplib
import urllib
import base64


def readKeys():
    f = open('../Keys').read()
    keys = f.split('\n')

    key = []
    for i in keys:
        res = i.split(',')
        for j in res:
            key.append(j)
    return key

subscription_key = readKeys()

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key[2],
}

params = urllib.urlencode({
})

body = "{ 'url': 'http://www.freeiconspng.com/uploads/obama-face-png-3.png' }"

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))