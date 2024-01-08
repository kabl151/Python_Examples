"""
<문제 링크>
https://www.acmicpc.net/problem/10798
"""
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################
Ea = int(input())
fieldList = []
area = 0
# 100*100 맵 생성
for i in range(100): #가로
    fieldList.append([])
    for j in range(100): #세로
        fieldList[i].append(0)
        


for e in range(Ea):
    X, Y = map(int,input().split())
    for x in range(10): #x좌표
        for y in range(10):
            fieldList[x+X][y+Y] += 1
            
            
for i in range(100):
    while 0 in fieldList[i]:
        fieldList[i].remove(0)

for i in range(100):
    area = area + len(fieldList[i])

print(area)
"""_
<숏코딩>

paper = [[0 for _ in " "*100] for _ in " "*100]

for _ in " "*int(input()):
    x,y=map(int,input().split())
    
    for i in range(y,y+10):
    
        for j in range(x,x+10):
            paper[i][j] = 1
            
print(sum([sum(i) for i in paper]))

"""

#######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")