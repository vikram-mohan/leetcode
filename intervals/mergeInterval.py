def mergeInterval(intervals):
    merged = []
    intervals.sort(key=lambda x: x[0])
    print("sorted by the starting time", intervals)

    # start time 
    for i in range(len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        if merged and merged[-1][1] > start:
            merged[-1][1] = end
            continue
        merged.append([start, end])
        print("current merged", merged)
    return merged

print(mergeInterval([[1,3],[2,6],[8,10],[15,18]]))