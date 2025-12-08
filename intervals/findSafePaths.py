def findSafePaths(planets):
    # step 1 - construct the exploded view
    # step 2 - sort the exploded view
    # step 3 - find the gaps
    result = []
    exploded = []
    for location, influence in planets:
        exploded.append((location - influence, location + influence))

    exploded.sort()
    print("exploded", exploded)
    
    if exploded[0][0] > 0:
        # handle 0 zero index edge case
        result.append((0 , exploded[0][0]))

    curend = exploded[0][1]
    for i in range(1, len(exploded)):
        nextstart, nextend = exploded[i][0], exploded[i][1]
        # print(nextstart, nextend, curstart, curend)
        if curend < nextstart:
            # no overlap, so append to window (curend, nextstart)
            result.append((curend, nextstart))
            curend = nextend
        curend = max(curend, nextend)
    result.append((curend, "MAX"))
    return result

test1 = [(3, 1), (6, 1)] # exploded [(2, 4),(5, 7)] +> answer = [(0,2),(4,5),(7, MAX)]
print(findSafePaths(test1)) # [(0,2),(4,5),(7, MAX)]

test2 = [(3, 1), (6, 1), (10,4)] # exploded [(2, 4),(5, 7)] +> answer = [(0,2),(4,5),(7, MAX)]
print(findSafePaths(test2)) # [(20, 'MAX')]