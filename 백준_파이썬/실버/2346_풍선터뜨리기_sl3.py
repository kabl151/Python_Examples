"""
[1,2,3,4,5,6,7]
[-7~7]
터진 풍선 받아올 리스트 = [] # 나중에 언팩
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
baloonsDeque = deque(map(int,sys.stdin.readline().split()))
numberingLst = deque([n+1 for n in range(len(baloonsDeque))])
basket = []
#일단 1번 풍선 펑
# 터진 풍선 받아올 리스트에 풍선번호 추가
# baloonsDeque .popleft -> pop된 수(양수/음수)나누어서 .rotate() 기능 구현.
while baloonsDeque:
    cardNum = baloonsDeque[0]
    
    baloonsDeque.popleft()
    basket.append(numberingLst.popleft())
    if cardNum > 0:
        baloonsDeque.rotate(-(cardNum-1))
        numberingLst.rotate(-(cardNum-1))
    else:
        baloonsDeque.rotate(-(cardNum))
        numberingLst.rotate(-(cardNum))
        
print(*basket)