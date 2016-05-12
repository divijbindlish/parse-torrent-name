import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    description = f.read()

setup(
    name='parse-torrent-name',
    version=__import__('PTN').__version__,
    author=__import__('PTN').__author__,
    author_email=__import__('PTN').__email__,
    license=__import__('PTN').__license__,
    url='https://github.com/divijbindlish/parse-torrent-name',
    description='Extract media information from torrent-like filename',
    long_description=description,
    packages=['PTN'],
    keywords=('parse parser torrent torrents name names proper rename '
              'movie movies tv show shows series extract find quality '
              'group codec audio resolution title season episode year '
              'information filename filenames file files meaningful'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Text Processing'
    ]
)
