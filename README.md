# parse-torrent-name ![Build Status](https://travis-ci.org/divijbindlish/parse-torrent-name.svg?branch=master)

> Extract media information from a filename

A python port of [Jānis](https://github.com/jzjzjzj)' awesome
[library](https://github.com/jzjzjzj/parse-torrent-name) written in javascript.

## Install

```sh
$ easy_install parse-torrent-name
```

PTN can also be installed using `pip`.

## Usage

```py
import PTN

PTN.parse('A freakishly cool movie or TV episode')
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

## Contributing

Take a look at the open
[issues](https://github.com/jzjzjzj/parse-torrent-name/issues) on the original
project and submit a PR!

## License

MIT © [Divij Bindlish](http://divijbindlish.com)
