def largestRectangleArea(heights):
    heights.append(0)  # Add a 0 to ensure we process all elements in the stack
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        # Maintain a stack of increasing heights
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]  # Height of the bar to calculate area
            w = i if not stack else i - stack[-1] - 1  # Width of the rectangle
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area

print(largestRectangleArea([2 , 1, 5, 6, 2, 3]))