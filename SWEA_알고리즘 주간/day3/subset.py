N = 5
arr = [1,2,3,4,5]

for i in range(1<<N): # i의 비트 모양이 부분 집합의 모양임. 그래서 요소가 N개라 N개 비트 확인하면 되는 것.
    s = 0

    for j in range(N): #j = 0 1 2 3 4
        if i&(1<<j) == True: # 한 칸씩 밀어서 i를 검증하는 과정. 각 과정은 N만큼 소요됨.
            s += arr[j]
            print(arr[j], end = ' ')

    print(s)


print('---')
print(arr)