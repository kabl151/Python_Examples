T = int(input())
def pari(N, M):
    parifield = []
    catchPari = 0
    totalLst = []
    #맵 형성
    for n in range(N):
        row = []
        row = list(map(int, input().split()))
        parifield.append(row)
    
    #포인터 탐색 영역
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            catchPari = 0 #파리수 초기화
            #파리채 크기 게더링
            for m in range(M):
                for mm in range(M):
                    catchPari += parifield[i+m][j+mm]
            totalLst.append(catchPari)
            
    return max(totalLst)

for t in range(T):
    N, M = map(int,input().split())
    #N : arraySize, M: PA-Ri-CHEA
    print(f'#{t+1} {pari(N,M)}')
    
    
    