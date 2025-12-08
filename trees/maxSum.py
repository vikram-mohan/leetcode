class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
      -10
      /  \
     9   20
        /  \
       15   -7
"""

def maxSum(root):
    # postorder - at any particular node as root, we determine the max of the right subtree and left subtree
    # return max at any given node - final output is for the root node
    result = 0
    
    def postorderDFS(node):
        nonlocal result
        if not node:
            return 0
        
        # recurse left
        maxleft = max(postorderDFS(node.left), 0)

        # recurse right
        maxright = max(postorderDFS(node.right),0)

        # find the max sum *through* the node
        maxSum = node.val + maxleft + maxright
        result = max(result, maxSum) # update global max
        print(node.val, maxSum, result)
        return maxSum
        
    postorderDFS(root)
    return result

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(-7)

print(root)
print(maxSum(root)) # 42