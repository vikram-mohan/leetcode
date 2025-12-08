def letterCombinations(inputData):
    digitsmap = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    answer = []
    print(digitsmap)
    
    def dfs (index, path, inputData ):
        if len(path) == len(inputData):
            answer.append("".join(path))
            return
        
        for char in digitsmap[inputData[index]]:
            path.append(char)
            dfs(index+1, path, inputData)
            path.pop()
    
    dfs(0, [], inputData)
    return answer



print(len(letterCombinations("23")))
print(len(letterCombinations("456")))
print(len(letterCombinations("4657")))
