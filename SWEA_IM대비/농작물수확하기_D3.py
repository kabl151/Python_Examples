world_Farm = []
corpSum = 0

T = int(input())
for t in range(T):
    N = int(input())    #입력받기 (농장크기) -> 이걸로 규칙성 만들기.
    
    for n in range(N):  #농장 작물상황 입력받기 시작
        row_Farm = []   #row_Farm 초기화
        row_Farm = list(map(int, input().split()))
        world_Farm.append(row_Farm)
        
    #수확하기
    if N == 1:
        corpSum = world_Farm[0][0]
    else: # N != 1
        for n in range(N): # row Farm의 갯수 한행 한행...
            for k in range(int(N/2),0,-1) #작물수확 로직 -- 포인터의 위치가 중점부터 1씩 감소하도록.
                world_Farm[n][k:k+n*2]
            for