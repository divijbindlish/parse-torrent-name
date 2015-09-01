# parse-torrent-name

> Parse torrent name of a movie or TV show

A python port of [Jānis](https://github.com/jzjzjzj)' awesome
[library](https://github.com/jzjzjzj/parse-torrent-name) written in javascript.

## Install

```sh
$ pip install parse-torrent-name
```

## Usage

```py
import PTN

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

PTN.parse('Mr Robot S01E05 HDTV x264-KILLERS[ettv]')
# {
#     'episode': 5,
#     'season': 1,
#     'title': 'Mr Robot',
#     'codec': 'x264',
#     'group':  'KILLERS[ettv]'
#     'quality': 'HDTV'
# }
```

## Contributing

Take a look at the open
[issues](https://github.com/jzjzjzj/parse-torrent-name/issues) on the original
project and submit a PR!

## License

MIT © [Divij Bindlish](http://divijbindlish.com)
