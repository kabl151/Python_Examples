import sys
sys.stdin = open("input01.txt", "r")

for _ in range(10):
    t = int(input())
    lst = []
    for _ in range(100):
        tempLst = list(map(int,input().split()))
        lst.append(tempLst)
    Maxi, colSum, digSum1, digSum2 = 0, 0, 0, 0
    #행 먼저
    for i in range(100):
        colSum = 0
        if Maxi <= sum(lst[i]):#행 합 구하기
            Maxi = sum(lst[i])
        for j in range(100): # 열 합 구하기
            colSum += lst[j][i]
        if Maxi <= colSum:
            Maxi = colSum
    #대각선 1
    for i in range(100):
        digSum1 += lst[i][i]
        if Maxi <= digSum1:
            Maxi = digSum1
    #대각선 2
    for i in range(100):
        digSum2 += lst[i][99-i]
        if Maxi <= digSum2:
            Maxi = digSum2

    print(f'#{t} {Maxi}')