class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
      -5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

"""

root = Node(-5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)

def targetSum(root, target):
    # preorder - at any particular node as root, we add the current node value to the running sum
    # return - boolean if found and bubble back to the caller and proceed.    
    def dfs(node, runningSum = 0):
        if not node:
            return False
        
        runningSum += node.val 
        # print("runningSum", runningSum)
        # print("value", node.val )
        if runningSum  == target:
            return True

        if dfs(node.left, runningSum ) or dfs(node.right, runningSum):
            return True
        
        return False
        
    return dfs(root)

print(root)
print(targetSum(root, -5))  # True
print(targetSum(root, 8))  # True
print(targetSum(root, 17))  # True
print(targetSum(root, 54)) #False
print(targetSum(root, 0)) #False
print(targetSum(root, -100)) #False
print(targetSum(root, 25)) #False 