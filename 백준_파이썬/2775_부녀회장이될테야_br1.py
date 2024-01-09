"""
<문제 링크>
https://www.acmicpc.net/problem/2775
<풀이 링크>

"""
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################

T = int(input())

aPT_List = []
def family_APT(k, n):
        # if n == 0: #1호 들은 모두 1임
        #     return 1
    
        if k == 0: # 0층은 고유의 값을 가짐.
            return aPT_List[0][n]
    
        if  aPT_List[k][n] != 0:
            return aPT_List[k][n]
    
        for t in range(n+1):
            aPT_List[k][n] = aPT_List[k][n] + family_APT(k-1, t)

        return aPT_List[k][n]
    
for s in range(15): #floor
    aPT_List.append([])

#각 호마다 0 대입.
for s in range(15): # floor
    for i in range(14): # section
        aPT_List[s].append(0) #0층이 아니라 1층부터 매핑.

for s in range(14): # 0층 지정 숫자 매핑.    
    aPT_List[0][s] = s+1
for s in range(15): # 0층 부터 14층까지 1호는 1명이라고 매핑.    
    aPT_List[s][0] = 1

#테스트 케이스 만큼 실행.
for tt in range(T):
    
    k = int(input())
    n = int(input()) - 1 
    
    print(family_APT(k, n))
    


#######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")