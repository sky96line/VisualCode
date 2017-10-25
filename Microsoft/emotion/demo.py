import httplib
import urllib
import base64

# key2 = 5415e4b8d36348058a0fdfaf04ec642a
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '47fec90429eb444990bc3865c75071e3',
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
