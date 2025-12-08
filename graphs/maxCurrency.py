from collections import defaultdict, deque

def getMaxCurrency(data, input) -> float:
    result = 0
    store = defaultdict(list)
    visited = set()

    for currency in data:
        curr = currency[0]
        next = currency[1]
        conv = currency[2]
        store[curr].append((next, conv))

    print("constructed graph", store)

    queue = deque([(input[0], 1)]) # start from the first currency

    while queue:
        curr, running = queue.popleft()
        visited.add(curr)
        
        if curr == input[1]:
            result = max(result, running)

        for neighbour in store[curr]:
            if neighbour[0] not in visited:
                print("adding to queue", neighbour[0], running)
                queue.append(( neighbour[0], running * neighbour[1]))
    
    print("visited", visited)
    return result

input1 = [
    ["USD", "EUR", 0.85],  # 1 USD = 0.85 EUR
    ["USD", "GBP", 0.75],  # 1 USD = 0.75 GBP
    ["EUR", "JPY", 129.53],  # 1 EUR = 129.53 JPY
    ["GBP", "JPY", 152.34],  # 1 GBP = 152.34 JPY
    ["JPY", "CNY", 0.059],  # 1 JPY = 0.059 CNY
    ["CNY", "INR", 11.41],  # 1 CNY = 11.41 INR
    ["EUR", "USD", 1.18],  # 1 EUR = 1.18 USD
    ["GBP", "USD", 1.33],  # 1 GBP = 1.33 USD
    ["JPY", "USD", 0.0091],  # 1 JPY = 0.0091 USD
    ["INR", "USD", 0.013]  # 1 INR = 0.013 USD
]

print(getMaxCurrency(input1, ["USD", "JPY"]))