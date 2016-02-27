#!/usr/bin/env python

#Name: nyaa-dl
#Version: 0.0.1

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
import os.path
import requests
import urllib

error = 0

parser = argparse.ArgumentParser(prog='nyaa-dl')
parser.add_argument('-u', action="store", dest="url", help='The url from nyaa to parse and download.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.0')
results = parser.parse_args()

try:
    no_ssl_url = results.url.replace('https', 'http')
except AttributeError:
    print "URL did not use HTTPS"
    error = 1
else:
    if error == 1:
        no_ssl_url = results.url
    if error == 0:
        no_ssl_url = results.url.replace('https', 'http')

try:
    download_url = no_ssl_url.replace("view", "download")
except AttributeError:
    print "URL was already a download link"
    error = 1
else:
    if error == 1:
        download_url = no_ssl_url
        view_url = no_ssl_url.replace("download", "view")
    if error == 0:
        download_url = no_ssl_url.replace("view", "download")
        view_url = no_ssl_url

r = requests.get(view_url)
tree = fromstring(r.content)
title = tree.findtext('.//title')
filename = title.replace('NT > ', '')
torrent = filename +'.torrent'

# Print debugging info
print "\nOriginal URL :", results.url
print "Download URL :", download_url
print "View URL     :", view_url
print "Title        :", title
print "Filename     :", filename
print "Torrent      :", torrent

if os.path.exists(torrent):
    print "\nThis torrent file already exists!\n"
else:
    webFile = urllib.urlopen(download_url)
    localFile = open(torrent, 'wb')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()
