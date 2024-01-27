import sys
from collections import deque

Deque = deque()

N = int(sys.stdin.readline())

for n in range(N):
    cmdLst = []
    cmdLst = list(map(int, (sys.stdin.readline().split())))
    if cmdLst[0] == 1:
        Deque.appendleft(cmdLst[1])
    elif cmdLst[0] == 2:
        Deque.append(cmdLst[1])
    elif cmdLst[0] == 3:
        if len(Deque) != 0:
            print(Deque.popleft())
        else:
            print(-1)
    elif cmdLst[0] == 4:
        if len(Deque) != 0:
            print(Deque.pop())
        else:
            print(-1)
    elif cmdLst[0] == 5:
        print(len(Deque))
    elif cmdLst[0] == 6:
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif cmdLst[0] == 7:
        if len(Deque) != 0:
            print(Deque[0])
        else:
            print(-1)
    elif cmdLst[0] == 8:
        if len(Deque) != 0:
            print(Deque[-1])
        else:
            print(-1)
            