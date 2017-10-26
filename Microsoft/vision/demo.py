import httplib
import urllib
import base64
import json


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

uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key[4],
}

params = urllib.urlencode({
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

body = "{'url':'https://top10reviewof.com/wp-content/uploads/2016/03/10.Top-10-Richest-Bollywood-Actors-in-2016-450x338.jpg'}"

try:
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()

except Exception as e:
    print('Error:')
    print(e)
