# max sum of subarray size k
def slidingwindow(data, k):

    answer = float('-inf')
    windowSum = sum(data[:k])
    answer = max(windowSum, answer)
    
    for i in range(k, len(data)):
        # window 
        windowSum += data[i] - data[i-k]
        answer = max(answer, windowSum)
    return answer

#Basic Input
arr = [2, 1, 5, 1, 3, 2]
print(arr, slidingwindow(arr, 3))

#Case That Tests Negative Numbers- this doesnt work for all scenarios. thus sw is not used for negative integers
arr = [-1, -3, 4, -2, 5, -6]
print(arr, slidingwindow(arr, 2))

# Case Where the Maximum Window Is at the End
arr = [1, 2, 3, 4, 10, 20]
print(arr, slidingwindow(arr, 2))

# Case Where All Elements Are the Same
arr = [7, 7, 7, 7, 7]
print(arr, slidingwindow(arr, 3))