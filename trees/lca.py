class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'Node({self.val})'

"""    3
      / \
     5   1
    / \ / \
   6  2 0  8
     / \
    7   4 
"""

def lca(root, val1, val2): 
    if not root or root.val == val1 or root.val == val2:
        return root
    
    # lca traversal is mostly postorder
    left = lca(root.left, val1, val2)
    right = lca(root.right, val1, val2)

    # if left and right were found in the chilren then lca is root current node
    if left and right:
        return root
    
    return left if left else right

# construction done
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right = Node(1)
root.right.left = Node(0)
root.right.right = Node(8)

print(root)
print(lca(root, 5, 1)) # 3
print(lca(root, 5, 4)) # 5 
print(lca(root, 6, 4)) # 5