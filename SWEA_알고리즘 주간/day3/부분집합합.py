arr = [1,2,3,4,5,6,7,8,9,10,11,12]
T = int(input())
for t in range(T):
    rslt = 0
    realLst=[]
    temp2Lst = []
    N, K = map(int, input().split())
    for i in range(1 << len(arr)): 
        tempLst=[]
        for j in range(len(arr)):
            if i & (1 << j):
                tempLst.append(arr[j])
        temp2Lst.append(tempLst)
        if len(temp2Lst[i]) == N and sum(temp2Lst[i]) == K:
            realLst.append(temp2Lst[i])
    rslt = len(realLst)
    print(f'#{t+1} {rslt}')