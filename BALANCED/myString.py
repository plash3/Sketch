
class myString(str):

    def __init__(self, val):
        self.value = val

    # Defines tailored strings comparing. Assumes that the other
    # argument is a String.
    def __gt__(self, other):
        result = False
        sln = len(self.value)
        oln = len(other)

        for i in xrange( min(sln, oln) ):
            if self.value[i] > other[i]:
                result = True

        # meaning that -
        # '((' > '(((' but '((' < '(()'
        # '()' > '()(' but '()' < '())'
        if not result:
            if sln < oln:
                if self.value[0] == other[sln]:
                    result = True
            elif sln > oln:
                if self.value[oln] > other[0]:
                    result = True

        return result
