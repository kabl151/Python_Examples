from collections import deque

T = int(input())
for t in range(T):
    N = int(input())
    maze = []
    chckLst = [[0]*N for _ in range(N)]
    cntLst = [[0]*N for _ in range(N)]
    que = deque()
    cnt = 0
    d = [[1,0],[0,1],[-1,0],[0,-1]]
    
    #미로와 방문리스트 작성
    for n in range(N):
        tmpList = list(map(int, input()))
        #print(tmpList)
        maze.append(tmpList)
        
    #시작점 찾고 시작 위치를 큐에 삽입.
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                que.append([i,j])
    
    chckLst[i][j] = 1
    cntLst[i][j] = 1
                
    while que:#큐가 존재하는 동안
        x, y = que.popleft() # 선입선출 BFS의 핵심
        for dx, dy in d:
            ax = x + dx
            ay = y + dy
            #맵 넘어가지 않게 인덱스 설정
            if 0<=ax<N and 0<=ay<N:
                #한 칸만 더 움직이면 도착? -> 그러면 카운트에 저장.
                if maze[ax][ay] == 3:
                    cnt = cntLst[x][y]
                #방문할 수 있는지 확인
                if chckLst[ax][ay] == 0 and maze[ax][ay] == 0:
                    #방문할 수 있다면~~
                    que.append([ax,ay]) #큐에 삽입(BFS의 핵심1)
                    chckLst[ax][ay] = 1 # 방문리스트에 1이라고 방문 기록
                    cntLst[ax][ay] = cntLst[x][y] + 1

        
    print(f'#{t+1} {cnt}')
