a = []
p = {} # 중요도

N, M = map(int,input().split())
a = list(map(int,input().split()))

for n in range(N):
    p[n] = a[n]

print(p[M])