board = [list(map(int, input().split())) for _ in range(19)]
visited = [[False for _ in range(19)] for __ in range(19)]

dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]

def go(x, y, color, cnt, dx, dy):
    if cnt == 5:
        return [x + (dx * -2) + 1, y + (dy * -2) + 1]
    
    nx = x + dx
    ny = y + dy

    if visited[nx][ny] == False and board[nx][ny] == color and 0 <= nx < 19 and 0 <= ny < 19:
        ret = go(nx, ny, color, cnt+1, dx, dy)
        visited[nx][ny] == True
        return ret
    
    return False

def find(x, y, color, cnt):
    for n in range(8):
        nx = x + dx[n]
        ny = y + dy[n]

        if visited[nx][ny] == False and board[nx][ny] == color and 0 <= nx < 19 and 0 <= ny < 19:
            ret = go(nx, ny, color, cnt+1, dx[n], dy[n])
            visited[nx][ny] = True
            return ret

    return False

black = False
white = False
for i in range(19):
    for j in range(19):
        if board[i][j] == 1 and not visited[i][j]:
            black = find(i, j, 1, 1)
        elif board[i][j] == 2 and not visited[i][j]:
            white = find(i, j, 2, 1)
        
        visited[i][j] = True
        
        if black or white:
            break

if black:
    print(1)
    print(black[0], black[1])
elif white:
    print(2)
    print(white[0], white[1])