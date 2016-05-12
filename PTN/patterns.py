#!/usr/bin/env python
# -*- coding: utf-8 -*-

patterns = [
    ('season', '([Ss]?([0-9]{1,2}))[Eex]'),
    ('episode', '([Eex]([0-9]{2})(?:[^0-9]|$))'),
    ('year', '([\[\(]?((?:19[0-9]|20[01])[0-9])[\]\)]?)'),
    ('resolution', '(([0-9]{3,4}p))[^M]'),
    ('quality', ('(?:PPV\.)?[HP]DTV|(?:HD)?CAM|B[rR]Rip|TS|(?:PPV '
                 ')?WEB-?DL(?: DVDRip)?|H[dD]Rip|DVDRip|DVDRiP|DVDR'
                 'IP|CamRip|W[EB]B[rR]ip|[Bb]lu[Rr]ay|DvDScr|hdtv')),
    ('codec', 'xvid|x264|h\.?264'),
    ('audio', ('MP3|DD5\.?1|Dual[\- ]Audio|LiNE|DTS|AAC(?:\.?2\.0)'
               '?|AC3(?:\.5\.1)?')),
    ('group', '(- ?([^-]+(?:-={[^-]+-?$)?))$'),
    ('region', 'R[0-9]'),
    ('extended', 'EXTENDED'),
    ('hardcoded', 'HC'),
    ('proper', 'PROPER'),
    ('repack', 'REPACK'),
    ('container', 'MKV|AVI'),
    ('widescreen', 'WS'),
    ('website', '^(\[ ?([^\]]+?) ?\])'),
    ('language', 'rus\.eng')
]

types = {
    'season': 'integer',
    'episode': 'integer',
    'year': 'integer',
    'extended': 'boolean',
    'hardcoded': 'boolean',
    'proper': 'boolean',
    'repack': 'boolean',
    'widescreen': 'boolean'
}
