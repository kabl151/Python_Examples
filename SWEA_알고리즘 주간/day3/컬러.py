#겹치는 영역 구하기
T = int(input()) #테스트 케이스 수
for t in range(T):
    # 맵 생성
    arr = []
    for i in range(11):
        arr.append([])
        for j in range(11):
            arr[i].append(0)
    cnt = 0
    TT = int(input()) # 칠할 영역의 횟수
    for tt in range(TT):

        # a1, b1, a2, b2, c 로 입력 받음 (c는 색상코드 c1 빨강/ C2 파랑)
        #좌표 입력받기
        a1, b1, a2, b2, c = map(int,input().split())

        for i in range(a1, a2 + 1):
            for j in range(b1, b2 + 1):
                arr[i][j] += c  # 빨강이라 1더해서 할당함.
                if arr[i][j] == 3:
                    cnt += 1

    print(f'#{t+1} {cnt}')



T = int(input())
for t in range(T):
    cnt = 0
    arr = []
    for i in range(11):
        arr.append([])
        for j in range(11):
            arr[i].append(0)
    TT = int(input())
    for tt in range(TT):
        a1, b1, a2, b2, c = map(int, input().split())
        for i in range(a1, a2 + 1):
            for j in range(b1, b2 + 1):
                arr[i][j] += c
                if arr[i][j] == 3:
                    cnt += 1
    print(f'#{t + 1} {cnt}')



