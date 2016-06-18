import sys
import re
import os
from types import *
from utils import *
import collections as cl

def load_data(file_prefix):
    """
    Args:
        file_name: The name of extents file.
    Yields:
        An array of intervals.
    """
    assert type(file_prefix) is StringType, "file_prefix is not a string: %r" % file_prefix

    data_file = open('extents/' + file_prefix + '_extents.txt')
    data = data_file.read()
    data_file.close()
    intervals = data.split('\n')
    # remove last line
    if (not re.match(r'\d+\s\d+', intervals[-1])):
        intervals = intervals[0:-1]

    # count the number of same intervals, create an array of intervals with corresponding
    # counts and sort the array by lower bounds
    counter = cl.Counter()
    for interval in intervals:
        counter[interval] += 1
    intervals_count = map(lambda (a,b): map(int, a.split(' ')) + [b], counter.items())
    sort_intervals = sorted(intervals_count)

    return sort_intervals


def compute_num_intervals(P, intervals):
    """
    Args:
        P: The input number from the user.
        intervals: An array of intervals.
    Yields:
        The number of intervals that P is contained in.
    """
    assert type(P) is IntType, "P is not an integer: %r" % P

    sum = 0

    lower = lowerBoundBinarySearch(intervals, P)
    upper = upperBoundBinarySearch(intervals, P)

    if (lower == -1 or upper == -1):
        return 0

    for i in range(lower, upper+1):
        if (intervals[i][0] <= P and P <= intervals[i][1]):
            sum += intervals[i][2]

    return sum

def main(test_file_prefix):

    assert type(test_file_prefix) is StringType, "file_prefix is not a string: %r" % file_prefix

    intervals = load_data(test_file_prefix)
    out = ''
    # Write stdin and stdout to files for testing
    numbers_path = 'numbers/' + test_file_prefix + '_numbers.txt'
    output_path = 'outputs/' + test_file_prefix + '_output.txt'
    fo_num = open(numbers_path, 'w')
    fo_out = open(output_path, 'w')
    for line in sys.stdin:
        fo_num.write(line)
        N = str(compute_num_intervals(int(line), intervals))
        out = out + N + '\n'
        fo_out.write(N + '\n')
    fo_num.close()
    fo_out.close()
    sys.stdout.write(out)

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        print "Please provide file prefix"
    else:
        main(sys.argv[1])
