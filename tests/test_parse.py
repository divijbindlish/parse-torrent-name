import json
import os
import unittest

import PTN


class ParseTest(unittest.TestCase):

    def test_parser(self):
        with open(os.path.join(
                os.path.dirname(__file__),
                'files/input.json'
                )) as input_file:
            torrents = json.load(input_file)

        with open(os.path.join(
                os.path.dirname(__file__),
                'files/output.json'
                )) as output_file:
            expected_results = json.load(output_file)

        for torrent, expected_result in zip(torrents, expected_results):
            result = PTN.parse(torrent)
            self.assertItemsEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
