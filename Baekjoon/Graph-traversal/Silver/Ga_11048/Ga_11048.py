from collections import deque

N = int(input())
for _ in range(N):
    n = int(input())
    board = [input() for _ in range(n)]
    board = [list(x) for x in board]
    
    pos_w = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'w':
                pos_w.append(i*n + j)
    
    # 11,12,1,9,3,7,6,5시 순서
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    ret = 0
    while pos_w:
        one_dim_idx = pos_w.pop()
        x, y = one_dim_idx // n, one_dim_idx % n
        for idx in range(len(dx)):
            if 0 <= x+dx[idx] < n and 0 <= y+dy[idx] < n:
                if board[x+dx[idx]][y+dy[idx]] == '-':
                    pos_w.append( ((x+dx[idx]) * n + y+dy[idx]) )
                    board[x+dx[idx]][y+dy[idx]] = 'w'
                    ret += 1
    
    print(ret)