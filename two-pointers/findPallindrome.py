def findPallindrome(palString):
    answer = 0   
    result = set()
    
    def count(left, right):
        # left keeps going left
        # right keeps going right
        counter = 0
        while left >= 0 and right < len(palString) and palString[left] == palString[right]:
            if palString[left:right+1] not in result:
                counter += 1
                result.add(palString[left:right+1])
            left -= 1
            right += 1
        return counter
    
    for i in range(len(palString)):
        answer += count(i, i) # pallindrome with one letter centre
        answer += count(i , i + 1) # pallindrome with two letter centre

    return answer, result


print(findPallindrome("abba")) # a, a, bb, b, b, abba  count = 6
print(findPallindrome("abbatarat")) 
# print(findPallindrome("abrakadabra")) 