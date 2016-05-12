#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import unittest

import PTN


class ParseTest(unittest.TestCase):
    def test_parser(self):
        json_input = os.path.join(os.path.dirname(__file__), 'files/input.json')
        with open(json_input) as input_file:
            torrents = json.load(input_file)

        json_output = os.path.join(os.path.dirname(__file__), 'files/output.json')
        with open(json_output) as output_file:
            expected_results = json.load(output_file)

        for torrent, expected_result in zip(torrents, expected_results):
            result = PTN.parse(torrent)
            for key in expected_result:
                self.assertEqual(result[key], expected_result[key])

if __name__ == '__main__':
    unittest.main()
