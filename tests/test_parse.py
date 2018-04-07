#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import unittest
import sys

# Force using PTN relative to this test file
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))

import PTN


class ParseTest(unittest.TestCase):
    def test_parser(self):
        json_input = os.path.join(os.path.dirname(__file__), 'files/input.json')
        with open(json_input) as input_file:
            torrents = json.load(input_file)

        json_output = os.path.join(os.path.dirname(__file__), 'files/output.json')
        with open(json_output) as output_file:
            expected_results = json.load(output_file)

        self.assertEqual(len(torrents), len(expected_results))

        for torrent, expected_result in zip(torrents, expected_results):
            print("Test: " + torrent)
            result = PTN.parse(torrent)
            for key in expected_result:
                if not expected_result[key]:
                    self.assertNotIn(key, result)
                else:
                    self.assertIn(key, result)
                    result1 = result[key]
                    if key == 'excess' and type(result1) == list:
                        result1 = ', '.join(result1)
                    self.assertEqual(result1, expected_result[key])


if __name__ == '__main__':
    unittest.main()
