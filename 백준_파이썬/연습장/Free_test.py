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
N = int(input())
queue = []
com_List = []
head_idx = 0
tail_idx = 0

for n in range(N):
    
    com_List = list(sys.stdin.readline().split())
    
    if com_List[0] == 'push':
        queue.append(int(com_List[1]))
        tail_idx += 1

    elif com_List[0] == 'pop':
        try:
            print(queue[head_idx])
            del queue[head_idx]
            try:
                head_idx = 0
            except:
                head_idx = tail_idx = 0
        except IndexError:
            print(-1)

    elif com_List[0] == 'size':
        print(len(queue))

    elif com_List[0] == 'empty':
        if len(queue) == 0: #비어있으면
            print(1)
        else:
            print(0)

    elif com_List[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[head_idx])

    elif com_List[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    
    com_List = []

######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
loop 종료가 해결이 안되어서 sys.exit()를 사용했음
비둘기 머리콥터 문제인걸까?
"""

