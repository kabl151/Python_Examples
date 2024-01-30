T = int(input())
for t in range(T):
    
    N = int(input())
    numLst = list(map(int,input().split()))
    mxValue = numLst[0]
    mnValue = numLst[0]
    
    #최댓값 구하기
    for num in numLst:
        if num >= mxValue:
            mxValue = num   
    
    #최솟값 구하기
    for num in numLst:
        if num <= mnValue:
            mnValue = num
            
    diff = mxValue - mnValue
    print(f'#{t+1} {diff}')