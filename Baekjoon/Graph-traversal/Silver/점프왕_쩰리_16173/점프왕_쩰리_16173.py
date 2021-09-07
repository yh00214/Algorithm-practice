from collections import deque

N = int(input())

board = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
    
haruharu = False

dq = deque()
dq.append(0)

while dq:
    pos = dq.pop()
    x, y = pos // N, pos % N
    epoch = board[x][y]
    visited[x][y] = True
        
    if board[x][y] == -1:
        haruharu = True
        break
    
    if 0 <= x+epoch < N and not visited[x+epoch][y]:
        dq.append((x+epoch) * N + y)
    if 0 <= y+epoch < N and not visited[x][y+epoch]:
        dq.append(x * N + (y+epoch))
    


if haruharu:
    print('HaruHaru')
else:
    print('Hing')