#!/usr/bin/env python
# -*- coding: utf-8 -*-

patterns = [
    ('season', '[\. ]((?:Complete.)?s[0-9]{2}-s[0-9]{2}|'
               's([0-9]{1,2})(?:e[0-9]{2})?|'
               '([0-9]{1,2})x[0-9]{2})(?:[\. ]|$)'),
    ('episode', '((?:[ex]|ep)([0-9]{2})(?:[^0-9]|$))'),
    ('year', '([\[\(]?((?:19[0-9]|20[0-9])[0-9])[\]\)]?)'),
    ('resolution', '([0-9]{3,4}p|1280x720)'),
    ('quality', ('((?:PPV\.)?[HP]DTV|(?:HD)?CAM|B[DR]Rip|(?:HD-?)?TS|'
                 '(?:PPV )?WEB-?DL(?: DVDRip)?|HDRip|HDTVRip|DVDRip|DVDRIP|'
                 'CamRip|W[EB]BRip|BluRay|DvDScr|hdtv|telesync)')),
    ('codec', '(xvid|[hx]\.?26[45])'),
    ('audio', ('(MP3|DD5\.?1|Dual[\- ]Audio|LiNE|DTS|DTS5\.1|'
               'AAC[ \.-]LC|AAC(?:\.?2\.0)?|'
               'AC3(?:\.5\.1)?)')),
    ('group', '(- ?([^-]+(?:-={[^-]+-?$)?))$'),
    ('region', 'R[0-9]'),
    ('extended', '(EXTENDED(:?.CUT)?)'),
    ('hardcoded', 'HC'),
    ('proper', 'PROPER'),
    ('repack', 'REPACK'),
    ('container', '(MKV|AVI|MP4)'),
    ('widescreen', 'WS'),
    ('website', '^(\[ ?([^\]]+?) ?\])'),
    ('language', '(rus\.eng|ita\.eng|nordic)'),
    ('subtitles', '(DKsubs)'),
    ('sbs', '(?:Half-)?SBS'),
    ('unrated', 'UNRATED'),
    ('size', '(\d+(?:\.\d+)?(?:GB|MB))'),
    ('3d', '3D')
]

types = {
    'season': 'integer',
    'episode': 'integer',
    'year': 'integer',
    'extended': 'boolean',
    'hardcoded': 'boolean',
    'proper': 'boolean',
    'repack': 'boolean',
    'widescreen': 'boolean',
    'unrated': 'boolean',
    '3d': 'boolean'
}

bt_sites = ['eztv', 'ettv', 'rarbg', 'rartv', 'ETRG']
