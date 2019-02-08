def linearSearch(nlist, item):
    for n in nlist:
        if item == n:
            return 'Item found at index: %s' % nlist.index(n)
    else:
        return 'Item not found'


def binarySearch(nlist, item):
    mid = len(nlist) // 2
    if len(nlist) == 0:
        return 'Item not found'
    else:
        if int(item) > nlist[mid]:
            return binarySearch(nlist[mid+1:], item)
        elif int(item) < nlist[mid]:
            return binarySearch(nlist[:mid], item)
        else:
            return 'Item found at index: %s' % mid  # sometimes false index


def interpolationSearch(nlist, item):
    high = len(nlist) - 1
    low = 0
    mid = -1

    while nlist[low] <= item <= nlist[high]:
        if low == high or nlist[low] == nlist[high]:
            return None  # weird
        mid = int(low + ((high - low) / (nlist[high] - nlist[low])) * (item - nlist[low]))

        if nlist[mid] == item:
            return 'item found at index %s' % mid

        elif nlist[mid] < item:
            low = mid + 1

        else:
            high = mid - 1

