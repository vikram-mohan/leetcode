#longest subarray with sum less than k
def slidingwindow(data, k):

    left, windowSum = 0, 0
    answer = 0
    
    for right in range(len(data)):

        # include the element in the window
        windowSum += data[right]

        # window invariant
        while windowSum >= k:
            windowSum -= data[left]
            left += 1
        
        # window invariatn satisifed so calculate the answerr
        answer = max(answer, right - left + 1)
    return answer

# Simple, Clear Case
arr = [1, 2, 3, 4, 5]
print(arr, slidingwindow(arr, 9))

# A Case Where Small Numbers Hide a Big Value
arr = [2, 1, 1, 20, 1, 1]
print(arr, slidingwindow(arr, 5))

# Maximum Valid Subarray Is at the End
arr = [10, 9, 8, 1, 1, 1]
print(arr, slidingwindow(arr, 4))

# Contains Negative Numbers
#arr = [3, -2, 5, -1, 2]
# print(arr, slidingwindow(arr, 6))