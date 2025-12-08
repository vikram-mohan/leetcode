from math import inf


def binarySearch(data , target):
    d =  sorted(data)
    print("sorted data", d)

    M = 0
    N = len(d)-1
    result = None
    while M <= N:
        mid = (M + N) // 2
        print("iterators", M, N, mid)
        print ("sampled", d[mid])
        if d[mid] == target:
            result = mid
            N = mid - 1
        if d[mid] < target:
            print("shifting to right")
            M  = mid + 1            
        else:
            print("shifting to left")
            N = mid - 1
    return result if result else -inf

data = [34, 56, 78, 90, 32, 7, 4, 1, 90, 7, 4 , 5]
print(binarySearch(data, 7))