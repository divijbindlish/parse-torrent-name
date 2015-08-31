import json
import logging
import os
import unittest

import ptn


class ParseTest(unittest.TestCase):

    def test_parser(self):
        with open('files/input.json') as input_file:
            torrents = json.load(input_file)

        with open('files/output.json') as output_file:
            results = json.load(output_file)

        for torrent, result in zip(torrents, results):
            logging.info('Checking %s', torrent)
            self.assertEqual(ptn.parse(torrent), result)


if __name__ == '__main__':
    unittest.main()
