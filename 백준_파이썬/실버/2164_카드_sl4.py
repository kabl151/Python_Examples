import sys
from collections import deque

N = int(sys.stdin.readline())
cardDeque = deque(n+1 for n in range(N))
len_card = len(cardDeque)
if N == 1:
    pass
else:
    while cardDeque:
        cardDeque.popleft()
        cardDeque.rotate(-1)
        len_card -= 1
        if len_card == 1:
            break
    
print(cardDeque[0])