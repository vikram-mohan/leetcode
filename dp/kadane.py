
import math

def maxSubArraySum(arr):
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    answer = 0
    curr_sum = -1 * math.inf
    for num in arr:
        curr_sum += num
        if curr_sum < 0:
            curr_sum = 0
            continue
        answer = max(answer, curr_sum)
    return answer

print(maxSubArraySum([1, 2, 3, 4, 5]))
print(maxSubArraySum([1, -2, 3, -4, 5, -1, 8]))
print(maxSubArraySum([0 , -1, -2, -3, -4, 8, 9, -1, -2, -3, -4]))