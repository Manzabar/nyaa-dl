#!/usr/bin/env python

#Name: nyaa-dl
#Version: 0.0.0

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org>

import argparse
from lxml.html import fromstring
import requests
import urllib

parser = argparse.ArgumentParser(prog='nyaa-dl')
parser.add_argument('-u', action="store", dest="url", help='The url from nyaa to parse and download.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.0')
results = parser.parse_args()
parsed_url = results.url.replace("view", "download")

print "Original URL:", results.url
print "Parsed URL:", parsed_url

r = requests.get(results.url)
tree = fromstring(r.content)
title = tree.findtext('.//title')
print "Title:", title

filename = title.replace('NT > ', '')+'.torrent'
print "Filename:", filename

webFile = urllib.urlopen(parsed_url)
localFile = open(filename, 'wb')
localFile.write(webFile.read())
webFile.close()
localFile.close()
