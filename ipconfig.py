import http.client

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ip = conn.getresponse().read().decode('utf-8')
IPv4 = int(ip.replace('.', ''), 16)
