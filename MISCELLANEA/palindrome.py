import sys

def is_palindrome(arr, strind, endind):
    result = True
    while strind < endind:
        if arr[strind] != arr[endind]:
            result = False
            break
        strind += 1
        endind -= 1

    return result

def find_palindrome(arr):
    ln = len(arr) - 1
    diminution = 0
    while diminution < ln:
        i = 0
        j = ln - diminution
        while j <= ln:
            if is_palindrome(arr, i, j):
                return (i, j)
            i += 1
            j += 1
        diminution += 1

    return (0, 0)

def find_palindrome_kon(arr):

    def recurse(i, j):
        if is_palindrome(arr, i, j):
            return (i,j)
        r1 = recurse(i,j-1)
        r2 = recurse(i+1,j)
        if r1[1] - r1[0] >= r2[1] - r2[0]:
            return r1
        return r2

    return recurse(0, len(arr)-1)

# ==============================
def test_find_palindrome(arr, refrslt):
    #res = find_palindrome_kon(arr)
    res = find_palindrome(arr)
    print res
    assert refrslt == res

def all_tests():
    test_find_palindrome('', (0, 0))
    test_find_palindrome('A', (0, 0))
    test_find_palindrome('AB', (0, 0))
    test_find_palindrome('ABA', (0, 2))
    test_find_palindrome('AABB', (0, 1))
    test_find_palindrome('ABAddddCDCC', (3, 6))
    test_find_palindrome('ABAddddCCDCCa', (7, 11))
    test_find_palindrome('ABCDEF', (0, 0))
    test_find_palindrome('SAMPLE||ELPMAS', (0, 13))
    print 'All tests passed'

def main():
    all_tests()

if __name__ == "__main__":
    sys.exit(main())
