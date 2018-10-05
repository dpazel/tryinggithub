from collections import OrderedDict
from fractions import Fraction


def find_lower1(alist, item):
    first = 0;
    last = len(alist) - 1
    found = -1

    if item >= alist[last]:
        return last
    if item < alist[first]:
        return -1

    while first <= last and found == -1:
        midpoint = (first + last) // 2
        if item < alist[midpoint]:
            last = midpoint - 1
        else:
            if alist[midpoint + 1] > item:
                found = midpoint
            else:
                first = midpoint + 1

    return found


#  Think of it as searching on N semi-closed intervals instead of searching on points.
#  For N points there are N-1 sections., indexed 0 --> N-2, with the interval being represented by the lower point index.
#  The critical test is seeing if 'item' is within the interval that starts with midpoint
def find_lower(alist, item):
    num_pts = len(alist)
    num_sections = num_pts - 1

    if item >= alist[num_pts - 1]:
        return num_pts - 1
    if item < alist[0]:
        return -1

    first = 0;
    last = num_sections - 1
    found = -1

    while first <= last and found == -1:
        midpoint = (first + last) // 2
        if item >= alist[midpoint] and item < alist[midpoint + 1]:
            found = midpoint
        if item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found

# test line for branching