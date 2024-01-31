### 델타를 이용하는 2차원 배열 탐색


N = 5
arr = [[0]*N for _ in range(N)]
print((arr))
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
