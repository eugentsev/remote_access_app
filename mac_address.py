import netifaces

mac = netifaces.ifaddresses('enp4s0')[netifaces.AF_LINK]

for item in mac:
    MAC = int(item['addr'].replace(':', ''), 16)
