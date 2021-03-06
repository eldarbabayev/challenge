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

This algorithm is linear in the number of closed intervals. So the running time is O(#lines of extents file).

## Testing

I have included three test cases to check my api which consists of two functions. `TestLoadData` is testing `load_data` function which loads data from a file into array.
`TestEmptyExtents` and `TestLargeExtents` are testing `compute_num_intervals` function. The first test is used to check whether it is ok to have empty extents file and makes sure that for any `P`, `N` will be 0.
`TestLargeExtents` is checking a large extents file with a million closed intervals. 
