def upperBoundBinarySearch(alist, item):
    '''
        Adapted from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
    '''
    if (len(alist) == 0):
        return -1

    first = 0
    last = len(alist)-1
    found = False

    while first<=last:
        midpoint = (first + last)//2

        if (alist[last][0] < item):
            midpoint = last
            break

        if (alist[first][0] > item):
            return -1

        if (alist[midpoint][0] == item) or (alist[midpoint][0] < item and item < alist[midpoint+1][0]):
            break
        else:
            if item < alist[midpoint][0]:
                last = midpoint-1
            else:
                first = midpoint+1
    return midpoint


def lowerBoundBinarySearch(alist, item):
    '''
        Adapted from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
    '''
    if (len(alist) == 0):
        return -1

    first = 0
    last = len(alist)-1
    found = False

    while first<=last:
        midpoint = (first + last)//2

        if (alist[first][1] > item):
            midpoint = first
            break

        if (alist[last][1] < item):
            return -1

        if (alist[midpoint][1] == item):
            break
        elif (alist[midpoint][1] < item and item < alist[midpoint+1][1]):
            midpoint += 1
            break
        else:
            if item < alist[midpoint][1]:
                last = midpoint-1
            else:
                first = midpoint+1
    return midpoint
