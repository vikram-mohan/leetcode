def maxAreaIslands(data):
    M, N = len(data), len(data[0])
    visited = set()
    result = 0

    def dfs(i, j, s = 1):
        nonlocal result
        # running max
        result = max(result, s)   

        # mark the node as visited        
        visited.add((i, j))
        for dx,dy in [(-1, 0),(0, 1),(1, 0),(0, -1)]:
            x , y  = i + dx, j + dy
            if  (x, y) not in visited  and (0 <= x < M ) and (0 <= y < N) and data[x][y] == 1:
                dfs(x, y, s + 1)

    for i in range(M):
        for j in range(N):
            if (i, j) not in visited and data[i][j] == 1:
                dfs(i , j) 
    return result

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
] # answer is 6

print(maxAreaIslands(grid))