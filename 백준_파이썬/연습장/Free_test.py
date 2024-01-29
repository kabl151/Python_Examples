


N = int(input())
boxLst = list(map(int, input().split()))
downScoreLst = []
for i in range(N):
    downScoreLst.append(0)

for i in range(len(boxLst)):
    for j in range(i+1,N):
        if boxLst[i] > boxLst[j]:
            downScoreLst[i] += 1
            
    
print(max(downScoreLst))