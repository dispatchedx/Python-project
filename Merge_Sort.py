def mergeSort(nlist):
    if len(nlist) < 2:
        return nlist
    else:
        mid = len(nlist) // 2
        left = mergeSort(nlist[:mid])
        right = mergeSort(nlist[mid:])  # care +1
        return merge(left, right)


def merge(left, right):
    sorted = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sorted.append(left[0])
            del left[0]
        else:
            sorted.append(right[0])
            del right[0]
    if len(left) == 0:
        sorted += right
    else:
        sorted += left
    return sorted