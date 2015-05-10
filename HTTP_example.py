import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  # This will return entire content.
conn.request("GET", "/")
r1 = conn.getresponse()
while not r1.closed:
 print(r1.read(200)) # 200 bytes
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
conn.close()
