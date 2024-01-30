world_Farm = []
corpSum = 0

T = int(input())
for t in range(T):
    N = int(input())    #입력받기 (농장크기) -> 이걸로 규칙성 만들기.
    
    for n in range(N):  #농장 작물상황 입력받기 시작
        row_Farm_frst = []
        farmNum = int(input())
        for nn in range(N):
            
            row_Farm_frst.append(farmNum % 10)
            farmNum //= 10
            
        
    row_Farm = reversed(row_Farm_frst)
    print(row_Farm)
        
    #수확하기
    if N == 1:
        corpSum = world_Farm[0][0]
    else: # N != 1 
        for n in range(N): # N = 7      n = 0 1 2 3 4 5 6
            if n <= int(N/2):
                corpSum += sum(world_Farm[n][(int(N/2) - n): (int(N/2) + n)])
            elif n >= int(N/2): # n = 4(2) 5(1) 6(0) 
                corpSum += sum(world_Farm[n][(2 * int(N/2)) - (n+1): (int(N/2) + ((N-1)-n))])
    
    print(f'{t+1} {corpSum}')
            