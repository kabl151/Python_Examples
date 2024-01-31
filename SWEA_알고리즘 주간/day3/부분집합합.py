arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# 집합 A의 부분집합 중 N개 원소, 원소들 합 K 부분집합 "**개수**"?
#부분집합 없으면 0을 출력함.

T = int(input())
for t in range(T):
    rslt = 0
    N, K = map(int, input().split())

    for i in range(1 << len(arr)): # 2^12번 루프

        for j in range(len(arr)): #부분 집합 원소 수.

            if i & (1 << j): #i:0부터 ~ 2^부분집합 수 만큼 매치가 되면

















        if elem == N and s == K:
            print('s는',s, 'elem', elem)
            rslt += 1




    print(f'#{t+1} {rslt}')