from __future__ import print_function
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

body = "{'url': 'http://i.dailymail.co.uk/i/pix/2013/12/15/article-2523930-1982DCEE00000578-690_634x435.jpg'}"

try:
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    parsed = json.loads(data)
    print ("Prediction :", end=" ")
    
    dt = json.dumps(parsed, sort_keys=True, indent=2)
    print(parsed['description']['captions'][0]['text'])
    print(parsed['description']['captions'][0]['confidence'])
    conn.close()

except Exception as e:
    print('Error:')
    print(e)
