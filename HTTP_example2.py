import http.client
conn = http.client.HTTPSConnection("www.google.es")
conn.request("HEAD", "/")
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(len(data))
data == b''

