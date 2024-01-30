
for t in range(10):
    diff = 0
    dumpBx = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dumpBx):
        tempMAX, tempmin = max(boxes), min(boxes)
        diff = max(boxes) - min(boxes)
        if tempMAX - tempmin == 1:
            break
        else:
            maxIdx, minIdx = boxes.index(tempMAX), boxes.index(tempmin)
            tempMAX -= 1
            tempmin += 1
            boxes[maxIdx], boxes[minIdx] = tempMAX, tempmin
            
            
    print(boxes)
    print(max(boxes), min(boxes))
    print(maxIdx, minIdx)
    print(f'#{t+1} {diff}')
    #수정