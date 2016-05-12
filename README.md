# parse-torrent-name ![Build status](https://travis-ci.org/divijbindlish/parse-torrent-name.svg?branch=master)

> Extract media information from torrent-like filename

![Python versions](https://img.shields.io/badge/Python-2.7%2C%203.3-brightgreen.svg?style=flat-square)
![Downloads](https://img.shields.io/pypi/dm/parse-torrent-name.svg?style=flat-square)

A python port of [Jānis](https://github.com/jzjzjzj)' awesome
[library](http  s://github.com/jzjzjzj/parse-torrent-name) written in 
javascript.

Extract all possible media information present in filenames. Multiple regex 
rules are applied on filename string each of which extracts correponding
information from the filename. If a regex rule matches, the corresponding part
is removed from the filename. In the end, the remaining part is taken as the
title of the content.

## Why?

Online APIs by providers like
[TMDb](https://www.themoviedb.org/documentation/api),
[TVDb](http://thetvdb.com/wiki/index.php?title=Programmers_API) and
[OMDb](http://www.omdbapi.com/) don't react to well to search
queries which include any kind of extra information. To get proper results from
these APIs, only the title of the content should be provided as the search
query where this library comes into play. The accuracy of the results can be
improved by passing in the year which can also be extracted using this library.

## Usage

```py
import PTN

info = PTN.parse('A freakishly cool movie or TV episode')

print info # All details that were parsed
```

PTN works well for both movies and TV episodes. All meaningful information is
extracted and returned together in a dictionary. The text which could not be
parsed is returned in the `excess` field.

### Movies

```py
PTN.parse('San Andreas 2015 720p WEB-DL x264 AAC-JYK')
# {
#     'group': 'JYK',
#     'title': 'San Andreas',
#     'resolution': '720p',
#     'codec': 'x264',
#     'year':  '2015',
#     'audio': 'AAC',
#     'quality': 'WEB-DL'
# }

PTN.parse('The Martian 2015 540p HDRip KORSUB x264 AAC2 0-FGT')
# {
#     'group': '0-FGT',
#     'title': 'The Martian',
#     'resolution': '540p',
#     'excess': ['KORSUB', '2'],
#     'codec': 'x264',
#     'year': 2015,
#     'audio': 'AAC',
#     'quality': 'HDRip'
# }
```

### TV episodes 

```py
PTN.parse('Mr Robot S01E05 HDTV x264-KILLERS[ettv]')
# {
#     'episode': 5,
#     'season': 1,
#     'title': 'Mr Robot',
#     'codec': 'x264',
#     'group':  'KILLERS[ettv]'
#     'quality': 'HDTV'
# }

PTN.parse('friends.s02e01.720p.bluray-sujaidr')
# {
#     'episode': 1,
#     'season': 2,
#     'title': 'friends',
#     'resolution': '720p',
#     'group': 'sujaidr',
#     'quality': 'bluray'    
# }
```

### Note

PTN does not gaurantee the fields `group`, `excess` and `episodeName` as these 
fields might be interchanged with each other. This shoudn't affect most 
applications since episode name can be fetched from an online database 
after getting the season and episode number correctly.

### Parts extracted

* audio
* codec
* container
* episode
* episodeName
* excess
* extended
* garbage
* group
* hardcoded
* language
* proper
* quality
* region
* repack
* resolution
* season
* title
* website
* widescreen
* year

## Install

### Automatic

PTN can be installed automatically using `easy_install` or `pip`.

```sh
$ easy_install parse-torrent-name
```

OR 

```sh
$ pip install parse-torrent-name
```

Note that these commands might require `sudo` permission depending on whether
a virtual environment is used or not.

### Manual

First clone the repository.

```sh
$ git clone https://github.com/divijbindlish/parse-torrent-name PTN && cd PTN
```

And run the command for installing the package.

```sh
$ python setup.py install
```

## Contributing

Take a look at the open
[issues](https://github.com/jzjzjzj/parse-torrent-name/issues) on the original
project and submit a PR!

## License

MIT © [Divij Bindlish](http://divijbindlish.in)
