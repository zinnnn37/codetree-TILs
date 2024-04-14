if __name__ == '__main__':
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    r, c = map(lambda x: int(x) - 1, input().split())

    ans = [[0 for _ in range(n)] for _ in range(n)]
    depth = grid[r][c] - 1

    for i in range(-depth, depth + 1):
        if 0 <= r + i < n:
            grid[r + i][c] = 0
        if 0 <= c + i < n:
            grid[r][c + i] = 0
    
    ans = [[0 for _ in range(n)] for __ in range(n)]

    for j in range(n):
        h = n-1
        
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                ans[h][j] = grid[i][j]
                h -= 1
    
    for a in ans:
        print(*a)