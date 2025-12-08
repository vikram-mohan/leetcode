#longest subarray of 1's with k flips
def slidingwindow(data, k):

    left = 0
    flips = 0
    answer = 0
    
    for right in range(len(data)):
        if data[right] == 0:
            flips += 1

        # If we have more than k zeros, shrink from the left
        while flips > k:
            if data[left] == 0:
                flips -= 1
            left += 1
        
        # window invariant is satisfied - so can calculate the answer
        answer = max(answer, right - left + 1)
    return answer


arr = [0, 1, 0, 1, 0, 0, 1, 1, 0]
print(arr, slidingwindow(arr, 2))

arr = [0, 0, 1, 1, 0, 1]
print(arr, slidingwindow(arr, 2))

arr = [1, 1]
print(arr, slidingwindow(arr, 2))

arr = [0, 0]
print(arr, slidingwindow(arr, 2))