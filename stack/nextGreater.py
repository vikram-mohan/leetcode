
def nextGreater(nums):
    answer = [-1] * len(nums) # we will update out of order 
    
    stack = [] # monotonic stack
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop() # popping the index from the stack that you want to update
            answer[index] = nums[i]  # updating it with the current element
        stack.append(i)   
    return answer

print(nextGreater([2,1,2,4,3])) # [4, 2, 4, -1, -1]