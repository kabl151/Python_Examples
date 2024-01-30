T = int(input())
for t in range(T):
    N = int(input())
    cntLst = [0] * 10 # 0부터 9까지  카운트 할 리스트
    cardLst = []
    number = input()      #카드 나온 종류들 하나하나 받아올 리스트 생성
    for n in number:    #리스트에 카드들 정리.
        cardLst.append(int(n))
    for i in cardLst:   #카운트 리스트에 카드 장수 저장.(인덱스 = 카드 적힌 수)
        cntLst[i] += 1
    cntLst.reverse()
    print(f'#{t+1} {9 - cntLst.index(max(cntLst))} {max(cntLst)}')