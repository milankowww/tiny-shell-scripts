#! /usr/bin/env python

import sys, re

def sanitize(match):
	return match.group(1).replace('.', '[.]')

r = re.compile(r'\b(\d+\.\d+\.\d+\.\d+|https?://([A-Za-z0-9_~-]+(\.[A-Za-z0-9_~-]+)+)|([A-Za-z0-9_~.-]+\.([a-z]{2,4})))\b', re.IGNORECASE)

for line in sys.stdin:
	print r.sub(sanitize, line),
