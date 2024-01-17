"""
<문제 링크>
    https://www.acmicpc.net/problem/1531
    
<풀이 링크>
    -

#----------------------------------------#
#             S U D O _ C O D E          #
#----------------------------------------#




"""
#-----------------------------------------------------
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################
mapField = []
transparentField = 0

for i in range(101): # 맵필드에 각 점좌표 마다 리스트를 생성 (카운트용.)
    mapField.append([])
    for j in range(101):
        mapField[i].append(0)

N, M = map(int, input().split())
for n in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    width_diff = x2-x1 +1
    height_diff = y2-y1 +1
    
    for j in range(width_diff):
        for k in range(height_diff):
            mapField[x1+j][y1+k] += 1

for i in range(101):
    for j in range(101):
        if mapField[i][j] > M:
            transparentField += 1

print(transparentField)

######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
문제 조건을 잘 읽자. 0~99까지 for i 로 생성이면 
100,100을 입력을 못 받기 때문.
"""