import sys

def binary_search(arr, x, startIndex=0):
    result = -1
    length = len(arr)
    rng = (length - startIndex) / 2
    n = startIndex + rng
    # if the size of the substring is only one element then check it
    if x == arr[n]:
        result = n
    while rng > 0 and result < 0:
        correction = rng % 2
        if n + rng < length:
            riseCorrection = correction
        else:
            riseCorrection = 0
        rng = rng / 2
        if x < arr[n]:
            n -= rng + correction
        elif x > arr[n]:
            n += rng + riseCorrection
        if x == arr[n]:
            result = n

    return result

def binary_search_kons(arr, x, startIndex=0):

    lowerBound = startIndex
    upperBound = len(arr)

    while lowerBound < upperBound:

        n = lowerBound + (upperBound - lowerBound)/2

        # Check if we found the desired element in the array
        if x == arr[n]:
            return n

        if x < arr[n]:
            upperBound = n
        else:
            lowerBound = n+1

    return -1

# check if 2 elements can be found in the array lst such that
# the addition equals sum
def complement_search(lst, sum):
    strind = -1
    endind = -1
    if not lst: return (strind, endind)
    if sum <= lst[-1] + lst[-2]:
        for i in xrange(len(lst) - 1):
            x = sum - lst[i]
            if x < lst[i]:
                break
            ind = binary_search(lst, x, i + 1)
            if ind >= 0:
                strind = i
                endind = ind
                break

    print "START {0} END {1}".format(strind, endind)
    return (strind, endind)

# ==========================
def test_search(lst, sum, refrslt):
#    rndlst = [random.random() for i in xrange(5)]
    result = complement_search(lst, sum)
    assert result == refrslt

def all_tests():
    lst = range(9)
    test_search(lst, 12, (4, 8))
    test_search(lst, 13, (5, 8))
    test_search(lst, 14, (6, 8))
    test_search(lst, 15, (7, 8))
    test_search(lst, 16, (-1, -1))
    test_search(lst, 0, (-1, -1))
    lst[2] = 1
    test_search(lst, 2, (1, 2))
    test_search([], 4, (-1, -1))
    print 'All tests passed'

def main():
    all_tests()

if __name__ == "__main__":
    sys.exit(main())
