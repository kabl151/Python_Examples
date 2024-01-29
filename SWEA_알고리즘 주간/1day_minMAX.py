T = int(input())
for t in range(T):
    
    N = int(input())
    numLst = list(map(int,input().split()))
    
    diff = max(numLst) - min(numLst)
    print(f'#{t+1} {diff}')