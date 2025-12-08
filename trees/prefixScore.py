# words = ["a", "ab", "abc", "cab"]
# words = ["abc","ab","bc","b"]
from typing import List

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: List[str]) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            # print("cur", c, curr)
            if not curr.children[i]:
                curr.children[i] = Node()
            curr.children[i].count += 1             
            curr = curr.children[i]

    def getScore(self, word: List[str]) -> int:
        answer = 0
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            answer += curr.children[i].count
            curr = curr.children[i]     
        return answer   
        
def prefixScore(words: List[str]) -> List[str]:
    result = []

    pt = PrefixTree()
    
    for word in words:
        pt.insert(word)

    for word in words:
        result.append(pt.getScore(word)) 

    return result

# print(prefixScore(["a", "ab", "abc", "cab"])) # answer =
print(prefixScore(["abc","ab","bc","b"])) # answer [5,4,3,2]
print(prefixScore(["abcd"]))




