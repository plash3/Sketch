import sys
import is_balanced
from Queue import Queue

class bst_node:

    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.value = val

class bst:

    def __init__(self):
        self.root = None

    def add_val(self, val):
        if not self.root:
            self.root = bst_node(val)
        else:
            self.bst_add_val(self.root, val)

    def bst_add_val(self, node, val):
        if not node:
            return
        if node.value > val:
            if not node.left_child:
                node.left_child = bst_node(val)
            else:
                self.bst_add_val(node.left_child, val)
        else:
            if not node.right_child:
                node.right_child = bst_node(val)
            else:
                self.bst_add_val(node.right_child, val)

# =====================================

    def is_balanced(self):
        result = True
        if not self.root:
            return result
        else:
            level = 0
            levels = []
            self.bst_is_balanced(self.root, level, levels)

        if len(levels) < 2:
            levels.insert(0, 1)
        if levels[1] - levels[0] > 1:
            result = False
        return result

    def bst_is_balanced(self, node, level, levels):
        level += 1
        if not node.left_child and not node.right_child:
            if len(levels) < 2:
                levels.append(level)
                levels.sort()
            elif levels[0] > level:
                levels[0] = level
            elif levels[1] < level:
                levels[1] = level
            return
        if node.left_child:
            self.bst_is_balanced(node.left_child, level, levels)
        if node.right_child:
            self.bst_is_balanced(node.right_child, level, levels)

# =====================================

# =====================================

    def is_present(self, val):
        if not self.root:
            return False
        else:
            return self.bst_is_present(self.root, val)

    def bst_is_present(self, node, val):
        if node.value == val:
            return True
        if node.value > val:
            if not node.left_child:
                return False
            else:
                return self.bst_is_present(node.left_child, val)
        else:
            if not node.right_child:
                return False
            else:
                return self.bst_is_present(node.right_child, val)

# =====================================

    # Depth-first search (DFS) Pre-order
    # Finds all balanced leaves on a tree
    def get_blncd_leaves(self):
        blncdlvs = []
        if self.root:
            self.bst_get_blncd_leaves(self.root, blncdlvs)

        return blncdlvs

    def bst_get_blncd_leaves(self, node, blncdlvs):
        if not node.left_child and not node.right_child:
            if is_balanced.is_balanced( node.value ):
                blncdlvs.append( node.value )
            return
        if node.left_child:
            self.bst_get_blncd_leaves(node.left_child, blncdlvs)
        if node.right_child:
            self.bst_get_blncd_leaves(node.right_child, blncdlvs)

# =====================================

    def print_bfs(self):
        if not self.root:
            print "Empty bst."
            return

        count = 0
        level = 1
        nnz_row = 0
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node:
                nnz_row = 1
                print node.value, " ",
                queue.put(node.left_child)
                queue.put(node.right_child)
            else:
                print "x ",
                queue.put(None)
                queue.put(None)
            count += 1
            if level == count:
                print
                level *= 2
                count = 0
                if nnz_row == 0: return
                nnz_row = 0

def main():
    bst_tree = bst()
    vals = [4,-16,7,-4,7,-8, -32,6,-18]
    for v in vals:
        bst_tree.add_val(v)

    bst_tree.print_bfs()

    print "BALANCED IS", bst_tree.is_balanced()
    print "is present:", bst_tree.is_present(-8.0)

if __name__ == "__main__":
    sys.exit(main())
