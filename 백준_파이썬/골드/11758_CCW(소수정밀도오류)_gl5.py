"""
<문제 링크>
    https://www.acmicpc.net/problem/1436
    
<풀이 링크>
    https://wikidocs.net/206249

#----------------------------------------#
#             S U D O _ C O D E          #
#----------------------------------------#




"""
#-----------------------------------------------------
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################
x1 , y1 = map(int, input().split())
x2 , y2 = map(int, input().split())
x3 , y3 = map(int, input().split())
xd = x3 - x2
trans_dx = x2 - x1 
#기울기 값이라서 크기 무시 가능.
if x2 - x1 == 0:
    vector_1 = 10010
else:
    vector_1 = round((y2 - y1) / (x2 - x1), 5)
    
if x3 - x2 == 0:
    vector_2 = 10010
else:
    vector_2 = round((y3 - y2) / (x3 - x2), 5)

if trans_dx > 0:
    if vector_1 == vector_2:
        print(0)
    elif (vector_2 > vector_1 and xd > 0) or (vector_2 < vector_1 and xd < 0):
        print(1)
    elif (vector_2 < vector_1 and xd > 0) or (vector_2 > vector_1 and xd < 0):
        print(-1)
        
elif trans_dx < 0:
    if vector_1 == vector_2:
        print(0)
    elif (vector_2 > vector_1 and xd < 0) or (vector_2 < vector_1 and xd > 0):
        print(1)
    elif (vector_2 < vector_1 and xd < 0) or (vector_2 > vector_1 and xd > 0):
        print(-1)


######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
loop 종료가 해결이 안되어서 sys.exit()를 사용했음
비둘기 머리콥터 문제인걸까?
"""