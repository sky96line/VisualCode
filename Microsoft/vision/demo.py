import httplib
import urllib
import base64
import json

#subscription_key = 'ca335d9bd2a44842b055666ef1f63750' key2
subscription_key = '3aba9a66fe16491ea90615b199b0e68d'

uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
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
