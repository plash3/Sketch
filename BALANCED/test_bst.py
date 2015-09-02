import sys
# import random
from bst import bst
from myString import myString

def main():
    bst_tree = bst()
    # vals = [round(random.random()*100) for i in xrange(15)]

    vals = [myString('(')]
    bst_tree.add_val( vals[0] )
    for i in xrange(5):
        nvals = []
        while vals:
            v = vals.pop()
            nvals.append( myString(v + '(') )
            bst_tree.add_val( nvals[-1] )
            nvals.append( myString(v + ')') )
            bst_tree.add_val( nvals[-1] )
        vals = nvals

    bst_tree.print_bfs()
    print "BALANCED LEAVES:", bst_tree.get_blncd_leaves()

if __name__ == "__main__":
    sys.exit(main())
