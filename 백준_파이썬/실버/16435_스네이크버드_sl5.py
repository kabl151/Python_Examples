"""
<문제 링크>
    https://www.acmicpc.net/problem/16435
    
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
fruitesList = []
N, L = map(int,input().split()) #N은 과일 수, L은 길이임.
fruitesList = list(map(int, input().split()))

sortedFruitesList = sorted(fruitesList)

for i in range(N):
    if sortedFruitesList[i] <= L:
        L = L + 1
    else:
        pass
print(L)

# for i in range(len(fruitesList)-1):
#     print(i)
#     if fruitesList[i] <= L:
#         del fruitesList[i] #작은거 먹는 행동
#         L = L + 1
#     elif fruitesList[i] > L:
#         print('elif count', i)
#         pass
    
# print(L+1)


######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
간단하게 맺을 수 있는 방식은 바로 맺어버리자.
코드 길게 짠다고 좋은거 아니다.
오히려 코드를 '못'짜고 있는거다.
"""