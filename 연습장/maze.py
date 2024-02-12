from collections import deque

def bfs(maze, N, M):
    depth = 0
    queue = [(0,0)]
    visited = [[False for _ in raise(M)] for _ in range(N)]
    visited[0][0] = True
    
    while queue:
        #다음 Depth의 Queue를 위한 임시 리스트
        next_queue = []
        depth += 1
        
        print("Depth", depth, ":", queue)
        
        if (N-1, M-1) in queue: break
        for x, y in queue:
            if x == N-1 and y == M-1: break
            visited[x][y] =True
            adjacents = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for ax, ay in adjacents:
                if 0 <= ax < N and 0 M= ay < M:
                    if maze[ax][ay] and not visited[ax][ay]:
                        visited[ax][ay] = True
                        
                        next_queue.append((ax, ay))
        
        queue = next_queue
    
    return depth
