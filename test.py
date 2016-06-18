import unittest
import os
from code import *
from random import randint

class TestLoadData(unittest.TestCase):

    def setUp(self):
        # Create a temporary file
        self.prefix = 'test'
        self.test_path = 'extents/' + self.prefix + '_extents.txt'
        self.test_file = open(self.test_path, 'w')

        contents = '1 12' + '\n' + '106 122' + '\n' + '123 124' + '\n' + '12 33' + '\n'

        self.test_file.write(contents)
        self.test_file.close()

    def tearDown(self):
        # Remove the file after the test
        os.remove(self.test_path)

    def test_load_data(self):
        """
            load_data function should return an array of intervals
        """
        intervals = load_data(self.prefix)
        self.assertEqual(intervals, [[1,12],[106,122],[123,124],[12,33]])


class TestEmptyExtents(unittest.TestCase):

    def setUp(self):
        # Create a temporary file
        self.prefix = 'test_empty'
        self.test_path = 'extents/' + self.prefix + '_extents.txt'
        self.test_file = open(self.test_path, 'w')
        self.test_file.write(' ')
        self.test_file.close()

    def tearDown(self):
        # Remove the file after the test
        os.remove(self.test_path)

    def test_empty(self):
        """
            Working with empty extents file should always yield N to be 0
        """
        intervals = load_data(self.prefix)
        N = compute_num_intervals(randint(0, 2147483647), intervals)
        self.assertEqual(N, 0)


class TestLargeExtents(unittest.TestCase):

    def test_large(self):
        """
            Working with large extents file should be fine
        """
        intervals = load_data('test_large')
        N = compute_num_intervals(randint(0, 2147483647), intervals)
        self.assertEqual(N, 1000000)


if __name__ == '__main__':
    unittest.main()
