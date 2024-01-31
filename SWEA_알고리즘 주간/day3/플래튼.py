for t in range(10):
    diff = 0
    dumpBx = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dumpBx):
        if max(boxes) - min(boxes) == 1:
            break
        else:
            tempMAX, tempmin = max(boxes), min(boxes)
            maxIdx, minIdx = boxes.index(tempMAX), boxes.index(tempmin)
            tempMAX -= 1
            tempmin += 1
            boxes[maxIdx], boxes[minIdx] = tempMAX, tempmin
            diff = max(boxes) - min(boxes)
    print(f'#{t+1} {diff}')