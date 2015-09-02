def edit_distance(s, t):
    # recurse(m, n): the edit distance between the first m letters
    # of s and the first n letters of t
    cache = {}
    def recurse(m, n):
        if (m, n) in cache:
            return cache[(m, n)]
        if m == 0:
            ans = n
        elif n == 0:
            ans = m
        elif s[m-1] == t[n-1]:
            ans = recurse(m-1, n-1)
        else:
            ans = 1 + min(recurse(m-1, n), recurse(m, n-1), recurse(m-1, n-1))
        cache[(m, n)] = ans
        return ans
    return recurse(len(s), len(t))

#print edit_distance("a cat!", "the cats!")
print edit_distance("a cat!" * 10, "the cats!" * 10)
