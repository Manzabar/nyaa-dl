#!/usr/bin/env python

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

script_name = 'nyaa-dl'
script_version = '0.3.1'

import argparse
from lxml.html import fromstring
import os
import requests
import urllib


def open_torrent_list(filename, debug):
    """Returns a file object holding the file with a list of torrents
    """
    f = open(filename, 'rU')
    if not debug:
            return f

    if debug == 'Y':
        print 'Filename     :', filename
        print 'CWD          :', os.getcwd()
        return f


def torrent_filename(view_url, debug):
    """Returns the filename to give the torrent to be downloaded.
    """
    r = requests.get(view_url)
    tree = fromstring(r.content)
    title = tree.findtext('.//title')
    filename = title.replace('NT > ', '')
    torrent = filename +'.torrent'

    if not debug:
        return torrent

    if debug == 'Y':
        # Print variables before returning value
        print "Title        :", title
        print "Filename     :", filename
        print "Torrent      :", torrent
        return torrent


def torrent_id(url, debug):
    """Parses the url to find the ID# for the torrent
    """
    id = url[url.find('tid=')+4:]

    if not debug:
        return id

    if debug == 'Y':
        print "ID       :", id
        return id


def torrent_url(url_type, id_num, debug='Y'):
    """Builds the view/download url for further processing.
    """
    full_url = 'http://www.nyaa.se/?page=' + url_type + '&tid=' + id_num
    if not debug:
        return full_url

    if debug == 'Y':
        print "url_type     :", url_type
        print "id_num       :", id_num
        print "full_url     :", full_url
        return full_url


def torrent_download(download_url, torrent):
    """Downloads the URL using the torrent to the current working directory.
    """
    webFile = urllib.urlopen(download_url)
    localFile = open(torrent, 'wb')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()


def main():
    parser = argparse.ArgumentParser(prog='nyaa-dl')
    parser.add_argument('-u', action="store", dest="url", help='The URL from nyaa to parse and download.')
    parser.add_argument('-i', action="store", dest="inputfilename", help='The input file holding multiple URLs (one per line) from nyaa to parse and download.')
    parser.add_argument('-d', action="store", dest="debug", default='', help='Turns on debugging, causing additional information to print to the command-line.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+ script_version)
    args = parser.parse_args()
    verbose = args.debug
    if verbose == 'Y':
        print 'Args :', args
    # Use the following code when passing a single URL to to the script
    if args.url:
        if verbose == 'Y':
            print 'Processing url'
        t_Id = torrent_id(args.url, verbose)
        view_url = torrent_url('view', t_Id, verbose)
        download_url = torrent_url('download', t_Id, verbose)
        torrent = torrent_filename(view_url, verbose)

        if os.path.exists(torrent):
            print "File already exists."
        else:
            torrent_download(download_url, torrent)

    if args.inputfilename:
        if verbose == 'Y':
            print 'Processing torrent list'
        torrentlist = open_torrent_list(args.inputfilename, verbose)
        urls = [line.rstrip('\n') for line in torrentlist]
        for u in urls:
                if len(u) != 0:
                    t_Id = torrent_id(u, verbose)
                    view_url = torrent_url('view', t_Id, verbose)
                    download_url = torrent_url('download', t_Id, verbose)
                    torrent = torrent_filename(view_url, verbose)
                    if os.path.exists(torrent):
                        print torrent + " already exists."
                    else:
                        torrent_download(download_url, torrent)

if __name__ == "__main__":
    main()
