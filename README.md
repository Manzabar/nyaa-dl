nyaa-dl
================================
Several of the fansubbing groups I follow post links to the View pages on [Nyaa.eu](https://www.nyaa.eu/)/[Nyaa.se](https://www.nyaa.se/). Since I download these using the command-line on a Linux box; I wanted a better way to download these torrents. Previously, I'd been using wget, manually rewriting the URLs, and then manually renaming the download.

This script was written under Python 2.7.6. It may work under other versions of Python, but I make no guarantees.

USAGE
================================
python nyaa-dl -u 'http://www.nyaa.se/?page=view&tid=781669'

This will print a few comments to your command-line and write a file, named "[Commie] Lupin the Third (2015) - 03 [4588CA05].mkv.torrent" to the current directory.

CHANGELOG
================================
* First Release (0.0.0)

TODO
================================
* Add exception handling
  * Catch failed downloads
  * Catch passing a download rather than a view link to the script.
* Add ability to pass a list of links from a file.

LICENSE
================================
Copyright © 2016 Mark McKibben <manzabar@gmail.com>

This work is free. You can redistribute it and/or modify it under the terms of the [Do What The Fuck You Want To Public License](http://www.wtfpl.net/), Version 2, as published by Sam Hocevar. See the COPYING file for more details.
