from collections import Counter
import math

def longestUniqueSubstring(data):
    answer = -math.inf
    
    counts = Counter()
    left = 0
    
    for right in range(len(data)):
        counts[data[right]] += 1

        # If a character is repeated, shrink the window from the left
        while counts[data[right]] > 1:
            counts[data[left]] -= 1
            left += 1

        # Update the answer if the current window is longer
        answer = max(answer,right - left + 1)
    return answer

print(longestUniqueSubstring("abcabcbb"))
print(longestUniqueSubstring("apwwkewa"))
