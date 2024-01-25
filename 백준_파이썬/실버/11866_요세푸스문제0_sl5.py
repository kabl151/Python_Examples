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
import sys

n, k = map(int, sys.stdin.readline().split())

idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue: #queue가 empty이면 False 반환.
    idx += k - 1
    if idx >= len(queue):
        idx %= len(queue)
    res.append(str(queue.pop(idx)))

print("<", ", ".join(res), ">", sep="")
######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
순환 인덱스 돌리는 원리는 인덱스 % 전체크기 = 나머지가 핵심.
0이 나오는 순간이 원점이거든!
"""

