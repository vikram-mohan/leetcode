import math
from collections import defaultdict 
from collections import Counter
from shlex import join

def minWindowSubstring(string, target):
    if not string or not target:
        return None

    answer = math.inf
    need = Counter(target)
    required = len(target) # cant use a set as it will neglect repeating chars
    
    left = 0
    index = 0

    for right in range(len(string)):
        if need[string[right]] > 0:
            # character present in target
            required -= 1
        need[string[right]] -= 1
        
        while required == 0:
            if right - left + 1 < answer:
                answer = right - left + 1 # grab the answer
                index = left # grab the index
            
            # logic to shrink the window
            need[string[left]] += 1  # Increase the count for the leftmost character
            if need[string[left]] > 0:
                required += 1 
            left += 1 
    return index , answer



st = "ADOBECODEBANC"
index, length = minWindowSubstring(st, "ABC")
print("min window is", st[index:index+length], index, length)
