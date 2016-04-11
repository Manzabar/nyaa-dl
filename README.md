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
* 0.1.1: Updated version# in output from '-v'.
* 0.1.0: Switched from my weak attempt at error handling to a better method for rewriting the URLs.
* 0.0.1: Added some basic error handling.
* 0.0.0: First Release

TODO
================================
* Add exception handling
  * Catch failed downloads
* Add ability to pass a list of links from a file.
  * Maybe remove -u option when passing only a single URL to the script?
  * Maybe add an option to display details and otherwise just dowload the torrent file?
* Add ability to handle HTTPS urls.

LICENSE
================================
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
