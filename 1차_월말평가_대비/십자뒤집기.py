import sys
batoLst = []
for i in range(19):
    batoLst.append(list(map(int, input().split())))

print(batoLst)
N = int(input())

for n in range(N):
    X, Y = map(int, input().split())
    #가로줄 바꾸기
    for k in range(1,19):
        if batoLst[X][k] == 1:
            batoLst[X][k] = 0
        else:
            batoLst[X][k] = 1
            
    #세로줄 바꾸기
    for j in range(1,19):
        if batoLst[j][Y] == 1:
            batoLst[j][Y] = 0
        else:
            batoLst[j][Y] = 1
            
for i in range(1,19):
    print(*batoLst[i])