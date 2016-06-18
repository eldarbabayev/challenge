# challenge

To run the code

```bash 
$ python code.py prefix
```

Here prefix is `example1` in `example1_extents.txt`. To run on custom data add file into `extents` folder with the file name as `prefix_extents.txt`.


To run the tests

```bash 
$ python test.py
```

## Complexity Analysis

After we put intervals with corresponding count number into dictionary, let the size of the dictionary be m (m < #of intervals). Then the running time of `load_data` due to sorting function is O(m\*log(m)). The running time of `compute_num_intervals` is O(log(m)) + O(upper) which in a worse case will be O(#of intervals). So overall if the number of input numbers N is large (N >> m) then running time is O(N\*log(m)) + O(N\*upper) (compared to previous solution where it was O(N\*m)).

## Testing

I have included three test cases to check my api which consists of two functions. `TestLoadData` is testing `load_data` function which loads data from a file into array.
`TestEmptyExtents` and `TestLargeExtents` are testing `compute_num_intervals` function. The first test is used to check whether it is ok to have empty extents file and makes sure that for any `P`, `N` will be 0.
`TestLargeExtents` is checking a large extents file with a million closed intervals. `TestBinarySearch` checks the binary search function from `utils`.
