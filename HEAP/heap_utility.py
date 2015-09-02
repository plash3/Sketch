# max heap is built from the bottom up by successively
# sifting downward to establish the heap property.
def heapify(a):
    # the heap size
    size = len(a)
    for i in xrange( (len(a)-2) / 2, -1, -1 ):
        sift_down(a, i, size)

# move a node down in the tree, as long as needed; used
# to restore heap condition after deletion or replacement.
def sift_down(a, i, size):
    if size < 2:
        return
    # the index of the left and the right child branch
    ileft = 2*i + 1
    irght = 2*i + 2
    swap = i
    if a[i] < a[ileft]:
        swap = ileft
    if irght < size and a[swap] < a[irght]:
        # if there is a right child and that child is greater
        swap = irght
    if swap == i:
        # the node holds the largest element
        return
    else:
        tmp = a[i]
        a[i] = a[swap]
        a[swap] = tmp
        if 2*swap + 1 < size:
            sift_down(a, swap, size)
    return

# input: an unordered array a
def heapsort(a):
    # Build the heap in array a so that largest value is at the root.
    heapify(a)
    # the following loop maintains the invariants that a[0:end] is a
    # heap and every element beyond end is greater than everything
    # before it (so a[end:count] is in sorted order)
    i = len(a)
    while i > 1:
        i -= 1
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp
        sift_down(a, 0, i)

# input: an unordered array a
def get_maxelements(a, k):
    heapify(a)
    result = []
    i = len(a)
    end = max(i - k, 0)
    while i > end:
        i -= 1
        result.append(a[0])
        tmp = a.pop()
        if a:
            a[0] = tmp
            sift_down(a, 0, i)
        print a
        print result
    return result

a = range(1, 15)
get_maxelements(a, 10)
