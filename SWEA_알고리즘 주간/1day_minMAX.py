T = int(input())
for t in range(T):
    
    N = int(input())
    numLst = list(map(int,input().split()))
    mxValue = numLst[0]
    mnValue = numLst[0]
    
    #최댓값 구하기 
    #값 자체로 하는거랑, 인덱스로 하는거 둘다 할 줄 알아야 함.
    
    #값 자체로 구하는 것.
    for num in numLst: 
        if num >= mxValue:
            mxValue = num   
    
    #최솟값 구하기
    for num in numLst:
        if num <= mnValue:
            mnValue = num
            
    diff = mxValue - mnValue
    print(f'#{t+1} {diff}')