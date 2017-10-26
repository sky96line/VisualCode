import httplib, urllib, base64, json

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
    'Ocp-Apim-Subscription-Key': subscription_key[0],
}

params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

body = "{'url':'https://mosthdwallpapers.com/wp-content/uploads/2016/05/WWE-Sheamus-Face-Image.jpg'}"

try:
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
