# min heap is built from the bottom up by successively
# sifting downward to establish the heap property.
def heapify(a):
    size = len(a)
    # start with the last parent node;
    # the last element index is - (size - 1) and
    # the index of the node's parent is (i-1) / 2
    for i in xrange( (size-2) / 2, -1, -1 ):
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
    if a[i] > a[ileft]:
        swap = ileft
    if irght < size and a[swap] > a[irght]:
        # if there is a right child and that child is less
        swap = irght
    if swap == i:
        # the node holds the lowest element
        return
    else:
        tmp = a[i]
        a[i] = a[swap]
        a[swap] = tmp
        if 2*swap + 1 < size:
            sift_down(a, swap, size)
    return

# move a node up in the tree, as long as needed;
# used to restore heap condition after insertion.
def sift_up(a, i):
    if i <= 0:
        return
    # the index of the node's parent
    iparent = (i-1) / 2
    if a[i] < a[iparent]:
        tmp = a[i]
        a[i] = a[iparent]
        a[iparent] = tmp
        if iparent > 0:
            sift_up(a, iparent)
    return

# deletes the root node followed by moving
# last node and sifting down to maintain heap.
def delete_min(a):
    result = None
    if a:
        result = a[0]
        last = a.pop()
        if a:
            a[0] = last
            sift_down(a, 0, len(a))
    return result

# adds the new element at the end of the heap in the first
# available free space. The elements are then sifted up
# until the heap property has been reestablished.
def insert(a, c):
    a.append(c)
    i = len(a) - 1
    sift_up(a, i)

def increase_key(a, i, dif):
    a[i] += dif
    sift_down(a, i, len(a))

def decrease_key(a, i, dif):
    a[i] -= dif
    sift_up(a, i)

# input: an unordered array a
def heapsort(a):
    # Build the heap in array a so that lowest value is at the root.
    heapify(a)
    # the following loop maintains the invariants that a[0:end] is a
    # heap and every element beyond end is less than everything
    # before it (so a[end:count] is in sorted order)
    i = len(a)
    while i > 1:
        i -= 1
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp
        sift_down(a, 0, i)

"""
a = range(14, 0, -1)
heapify(a)
print a
size = len(a)
for i in xrange(size - 1, size / 2, -1):
    decrease_key(a, i, i)
    print a
"""
