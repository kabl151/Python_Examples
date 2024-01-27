import sys

stack = []

N = int(sys.stdin.readline())
for n in range(N):
    cmdLst = []
    cmdLst = list(map(int,sys.stdin.readline().split()))
    if cmdLst[0] == 1 :
        stack.append(cmdLst[1])
    elif cmdLst[0] == 2:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmdLst[0] == 3:
        print(len(stack))
    elif cmdLst[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmdLst[0] == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)