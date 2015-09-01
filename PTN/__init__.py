from .parse import PTN

__author__ = 'Divij Bindlish'
__email__ = 'dvjbndlsh93@gmail.com'
__version__ = '0.1.0'
__license__ = 'MIT'

ptn = PTN()


def parse(name):
    return ptn.parse(name)
