

#text = "gotxxotgxdogt";
# word = "got"
# rules
# individual letters in an anagram must be contiguous in a seguence without breaking
# forward sequence tog is not allowed
# answer =  "got", "otg", "ogt"

def isAnagram(word1, word2):
    return True if  set(word1) == set(word2) else False

def countAnagram(text : str, word: str):
    answer = 0
    ana = ""
    if isAnagram(text, word):
        answer = answer + 1
        return answer        
    
    if len(text) < len(word):
        return answer
    
    if len(text) == len(word):
        return isAnagram(text, word)
    
    for i in range(len(text) - len(word)):
        ana = text[i:i+len(word)]
        if len(ana) == len(word) and isAnagram(ana, word):
            answer += 1
    return answer

print(countAnagram("got", "got"))
print(countAnagram("tog", "tog"))
print(countAnagram("gotxxotgxdogtogt", "got"))