
T = int(input())
for t in range(T):
    
    #K = 최대 이동 정류장 수, N 종점 번호,  M 충전기가 있는 정류장 번호

    K, N, M = map(int, input().split())
    chrg_Station = list(map(int, input().split())) # 충전소 번호
    dst_List =[]
    cnt = 0
    swch = False
    btry = int(K)
    
    #거리차 리스트 만들기.
    dst_List.append(chrg_Station[0])    #출발지와 첫 충전소 거리 차이 추가
    for i in range(0, len(chrg_Station)-1):
        dist = chrg_Station[i+1] - chrg_Station[i] #충전소 간 거리차 = dist
        dst_List.append(dist)    #dist 리스트에 거리차 추가.
    dst_List.append(N - chrg_Station[-1])   #종점과 마지막 충전소간 거리차 추가
    #이로써 dst_List 거리까지 차이는 '구간별 길이 리스트'가 됨.
    for i in range(0, len(dst_List)-1): # 0부터 충전소들간 거리 마지막까지.
        if dst_List[i] < btry:
            if dst_List[i] + dst_List[i+1] <= btry:
                continue
            elif dst_List[i] + dst_List[i+1] > btry:
                cnt += 1
                btry = K
                continue
            continue
        elif dst_List[i] > btry:
            print(0)
            swch = True
            break
        elif dst_List[i] == btry:
            btry = K
            cnt += 1 
            continue
    if swch == False:
        print(cnt)
        








T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    chrg_Station = list(map(int, input().split()))
    dst_List =[]
    cnt = 0
    swch = False
    btry = int(K)
    dst_List.append(chrg_Station[0])
    for i in range(0, len(chrg_Station)-1):
        dist = chrg_Station[i+1] - chrg_Station[i]
        dst_List.append(dist)
    dst_List.append(N - chrg_Station[-1])
    for i in range(0, len(dst_List)-1):
        if dst_List[i] < btry:
            if dst_List[i] + dst_List[i+1] <= btry:
                continue
            elif dst_List[i] + dst_List[i+1] > btry:
                cnt += 1
                btry = K
                continue
            continue
        elif dst_List[i] > btry:
            print(0)
            swch = True
            break
        elif dst_List[i] == btry:
            btry = K
            cnt += 1 
            continue
    if swch == False:
        print(f'#{t+1} {cnt}')















    # roadLst = [0] * N
    # cnt = 0
    # btry = int(K) #시작할 때 풀 충전
    # for chrg in chrg_Station:
    #     roadLst[chrg] = K
        
    # for i in range(N):
    #     if btry >= 0:
    #         if roadLst[i] == K: #충전소가 있으면  (배터리 갱신 or 뛰어넘기)
    #             if btry >=  #배터리가 다음 충전소 거리보다 같거나 크다면 --> 패스
                
    #                 btry = int(K)
    #                 cnt += 1
    #         else: btry -= 1 #아니면 배터리 -1
                
    #     elif btry < 0: #이래야 마지막 도착때 에러 안생김.
    #         print(0)
    #         break
        
    # print(cnt)
            

    
    
    
    
    
    
    # roadLine = [0]*N
    # point, cnt = 0, 0
    # #로드 라인에 차지량 만큼 (숫자)배치.
    # for chrg in chrg_Station:
    #     roadLine[chrg] = K
        
    # #버스는 0번에서 출발함. 출발지에서는 풀 배터리.
    # #충전 횟수 최소화.
    
    # #변수 생성
    # btry = K #배터리 변수 ~ 배터리가 0이되면 break 걸고 0 출력
    # for dist in range(N):
    #     print(point, btry)
    #     if btry > 0 :
    #         btry -= 1
    #         point += 1
    #         if roadLine[dist] > 0:
    #             if 0 <= btry and btry <= K:
    #                 btry = K # 배터리 갱신
    #                 cnt += 1
                    
    #         elif point == N:
    #             print(cnt)
    #         elif point <= N:    
    #             print(0)
    #             break
    #     print(cnt)