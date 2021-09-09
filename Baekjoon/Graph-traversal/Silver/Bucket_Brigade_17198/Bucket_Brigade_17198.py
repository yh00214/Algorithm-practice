from collections import deque

N = 10

board = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            B_row = i
            B_col = j
        elif board[i][j] == 'R':
            R_row = i
            R_col = j
        elif board[i][j] == 'L':
            L_row = i
            L_col = j


            

stack = deque()
stack.append([B_row, B_col, 0])
dx = [0,-1,0,1]
dy = [-1, 0, 1, 0]
ret = 1000

while stack:
    x, y, cnt = stack.popleft()
    if board[x][y] == 'L':
        ret = min(ret, cnt-1)
        continue
        
    visited[x][y] = True
    for i in range(len(dx)):
        if 0 <= x + dx[i] < 10 and 0 <= y + dy[i] < 10:
            if not visited[x+dx[i]][y+dy[i]] and board[x+dx[i]][y+dy[i]] != 'R':
                stack.append([x+dx[i], y+dy[i], cnt+1])
print(ret)