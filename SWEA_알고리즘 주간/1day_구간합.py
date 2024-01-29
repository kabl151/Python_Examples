T = int(input())
for t in range(T):
    n, m = map(int, input().split()) # n은 정수의 갯수, m은 구간의 넓이
    numArr = list(map(int, input().split()))
    sumArr = []
    sumNum = 0
    
    #n-(m-1) : inspect 횟수
    
    #큰 단위(n-(m-1)) 
    for i in range(n-(m-1)):
        sumNum = 0
        #작은 단위 (m묶음)
        for j in range(m):
            sumNum += numArr[i+j]
        sumArr.append(sumNum)    
    
    maxValue = 0
    minValue = sumArr[0]
    
    sumARrr = [1,2,3,4,5,6,7]
    for i in sumArr:
        if i >= maxValue:
            maxValue = i
    
    for i in sumArr:
        if i <= minValue:
            minValue = i
            
    diff_MAXmin = maxValue - minValue
    
    print(f'#{t+1} {diff_MAXmin}')