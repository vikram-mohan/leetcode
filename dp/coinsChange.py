import math
def coinsChange(coins, target ):
    memo = {}
    answer = math.inf
    def backtrack(coins, remainder, path = []):
        nonlocal nways, memo , answer  
        if remainder < 0:
            return 
        
        if remainder == 0:
            nways += 1 
            answer = min(answer, len(path))
            return
        
        for coin in coins:
            backtrack(coins, remainder-coin, path + [coin])        
    
    nways = 0
    backtrack(coins, target)
    # return nways
    return answer

print(coinsChange([1,2,4], 5))
print(coinsChange([1,5,10], 17))