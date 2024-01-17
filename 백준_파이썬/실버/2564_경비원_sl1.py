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
positionList = [[0, 0]] # 방향, 거리
myDirection = 0
myDistance = 0
shortcutTemp = 0

widthNum, heightNum = map(int, input().split()) #블록맵 필드 가로/세로 입력받기
shopNum = int(input()) #상점갯수 -> 루프돌릴 수

def SaveCoordinate(k, direc, dist):
    positionList[k][0] = direc
    positionList[k][1] = dist
    
for i in range(shopNum): # 상점 갯수만큼 루프 돌려서 상점갯수 좌표 저장.
    positionList.append([0, 0]) # 상점위치 저장할 리스트 추가.
    directionNum, distanceNum = map(int, input().split())
    SaveCoordinate(i, directionNum, distanceNum)

#           주인공 위치 추가!!!!
myDirection, myDistance = map(int, input().split()) #마지막 주인공의 위치 입력
positionList[-1][0] = (myDirection) # 유저 방위 추가.
positionList[-1][1] = (myDistance) # 유저 거리 추가.

def CompareDistance(t):
    global shortcutTemp
    if positionList[t][0] == positionList[-1][0]:
        shortcutTemp += abs(positionList[t][1]-positionList[-1][1])
        
        # 같은 선상에 존재하지 않을 때.
    elif positionList[t][0] != positionList[-1][0]:
        #납북 / 북남으로 존재할 때.
        if (positionList[t][0] == 1 and positionList[-1][0] == 2) or (positionList[t][0] == 2 and positionList[-1][0] == 1):
            # 거리비교 시작
            if positionList[t][1] + positionList[-1][1] <= (widthNum):
                shortcutTemp += heightNum + positionList[t][1] + positionList[-1][1]
            else:
                shortcutTemp += abs((2 * widthNum) + heightNum - (positionList[t][1] + positionList[-1][1]))
            
        #동서/서동으로 존재할 때.
        elif (positionList[t][0] == 3 and positionList[-1][0] == 4) or (positionList[t][0] == 4 and positionList[-1][0] == 3):
            if (positionList[t][1]) + positionList[-1][1] <= heightNum:
                shortcutTemp += widthNum + positionList[t][1] + positionList[-1][1]
            else:
                shortcutTemp += abs((2*heightNum) + widthNum - (positionList[t][1]+positionList[-1][1]))
            
        #평행하지 않을 때.
        elif positionList[t][0] == 1 and positionList[-1][0] == 3:
            shortcutTemp += positionList[t][1] + positionList[-1][1]
        elif positionList[t][0] == 1 and positionList[-1][0] == 4:
            shortcutTemp += widthNum - positionList[t][1] + positionList[-1][1]
        elif positionList[t][0] == 2 and positionList[-1][0] == 4:
            shortcutTemp += widthNum - positionList[t][1] + heightNum - positionList[-1][1]
        elif positionList[t][0] == 2 and positionList[-1][0] == 3:
            shortcutTemp += widthNum - positionList[t][1] + heightNum - positionList[-1][1]
        elif positionList[t][0] == 3 and positionList[-1][0] == 1:
            shortcutTemp += positionList[t][1] + positionList[-1][1]
        elif positionList[t][0] == 3 and positionList[-1][0] == 2:
            shortcutTemp += heightNum - positionList[t][1] + positionList[-1][1]
        elif positionList[t][0] == 4 and positionList[-1][0] == 1:
            shortcutTemp += positionList[t][1] + widthNum - positionList[-1][1]
        elif positionList[t][0] == 4 and positionList[-1][0] == 2:
            shortcutTemp += heightNum - positionList[t][1] + widthNum - positionList[-1][1]

for i in range(shopNum):
    CompareDistance(i)
        
print(shortcutTemp)
######################################################d
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
loop 종료가 해결이 안되어서 sys.exit()를 사용했음
비둘기 머리콥터 문제인걸까?
"""