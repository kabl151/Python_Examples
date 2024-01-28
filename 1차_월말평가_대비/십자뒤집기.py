import sys
batoLst = []
for i in range(19):
    batoLst.append(list(map(int, input().split())))

print(batoLst)
N = int(input())

for n in range(N):
    X, Y = map(int, input().split())
    #가로줄 바꾸기
    for k in range(19):
        if batoLst[X-1][k] == 1:
            batoLst[X-1][k] = 0
            
        elif batoLst[X-1][k] == 0:
            batoLst[X-1][k] = 1
            
    #세로줄 바꾸기
    for j in range(19):
        if batoLst[j][Y-1] == 1:
            batoLst[j][Y-1] = 0
            
        elif batoLst[j][Y-1] == 0:
            batoLst[j][Y-1] = 1
            
for i in range(19):
    print(*batoLst[i])
    
# for i in range(1,20):
#     print(*batoLst[i])