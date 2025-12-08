import math

def maxContainerWater(height):
    print("height", height)
    answer = -1* math.inf
    left, right = 0, len(height) - 1

    while left < right:
        # area can be determined by
        minH = min(height[left],height[right])
        answer = max(minH * (right - left), answer)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return answer

print(maxContainerWater([1,8,6,2,5,4,8,3,7])) # 49
print(maxContainerWater([1,1])) #1
print(maxContainerWater([4,3,2,1,4])) #16