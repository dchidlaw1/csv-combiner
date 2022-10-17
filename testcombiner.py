#!/usr/bin/env python3

import csv
import io
import unittest
from unittest.mock import patch
import pandas as pd
import csvcombiner
import sys

class TestCombiner(unittest.TestCase):
    def testWriteCols(self):
        testCsv = pd.DataFrame([['test10', 'test11'], ['test20', 'test21']], columns=['testCol1', 'testCol2'])
        testCsv.to_csv('test.csv', index=False, sep=",", mode="w", quoting=csv.QUOTE_ALL, escapechar="\\")
        writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        self.assertEqual(csvcombiner.writeCols('test.csv', writer), ['testCol1', 'testCol2', 'filename'])
    def testReadFile(self):
        testCsv = pd.DataFrame([['test10', 'test11'], ['test20', 'test21']], columns=['testCol1', 'testCol2'])
        testCsv.to_csv('test.csv', index=False, sep=",", mode="w", quoting=csv.QUOTE_ALL, escapechar="\\")
        writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        with patch('sys.stdout', new=io.StringIO()) as output:
            csvcombiner.readFile('test.csv', ['testCol1', 'testCol2', 'filename'])
            self.assertEqual(output.getvalue(), '"test10","test11","test.csv"\r\n"test20","test21","test.csv"\r\n')

if __name__ == '__main__':
    unittest.main()
