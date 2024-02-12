from collections import deque
for _ in range(10):
    T = int(input())
    N = 100
    maze = []
    chckLst = [[0]*N for _ in range(N)] #빙문 리스트는 모두 0으로 깐다.
    cntLst = [[0]*N for _ in range(N)] #카운트 리스트는 모두 0으로 깐다.
    que = deque()
    cnt = 0
    d = [[1,0],[0,1],[-1,0],[0,-1]]

    #미로생성.
    for n in range(N):
        tmpList = list(map(int, input()))
        maze.append(tmpList)
        
    #시작점 찾고 시작 위치를 큐에 삽입.
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                que.append([i,j])
                
    #찾아낸 시작점을 통해 방문 리스트와, 카운트 리스트에 1로 마크
    chckLst[i][j] = 1
    cntLst[i][j] = 1
                
    while que and cnt == 0:#큐(작업열)가 존재하는 동안 루프 진행.
        x, y = que.popleft() # 선입선출 BFS의 핵심___1
        
        #인접 방향 모두 서치(델타)
        for dx, dy in d:
            ax = x + dx
            ay = y + dy
            
            #맵 넘어가지 않게 인덱스 설정
            if 0<=ax<N and 0<=ay<N:
                
                #한 칸만 더 움직이면 도착? -> 그러면 카운트에 저장.
                if maze[ax][ay] == 3:
                    cnt = 1
                    break
                
                #방문할 수 있는지 확인
                if chckLst[ax][ay] == 0 and maze[ax][ay] == 0:
                    #방문할 수 있다면~~
                    que.append([ax,ay]) #큐에 삽입(BFS의 핵심_____2)
                    chckLst[ax][ay] = 1 # 방문리스트에 1이라고 방문으로 기록.
                    cntLst[ax][ay] = cntLst[x][y] + 1 #카운트 리스트에 현재 인덱스 값에 하나를 더 더해줌.

        
    print(f'#{T} {cnt}')
