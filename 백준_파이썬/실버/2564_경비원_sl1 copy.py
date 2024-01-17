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
positionList = [[]] # 방향, 거리
myDirection = 0
myDistance = 0

widthNum, heightNum = map(int, input().split()) #블록맵 필드 가로/세로 입력받기
shopNum = int(input()) #상점갯수 -> 루프돌릴 수

def Save_Coordinate(k, dir_Num, dist_Num): # x,y  좌표계로 변환
    if dir_Num == 1:
        positionList[k][0] = dist_Num
        positionList[k][1] = 0
    #상점이 남쪽에 있을 경우    
    elif dir_Num == 2:
        positionList[k][0] = dist_Num
        positionList[k][1] = heightNum
    #상점이 서에 있을 경우    
    elif dir_Num == 3:
        positionList[k][0] = widthNum
        positionList[k][1] = dist_Num
    #상점이 동쪽에 있을 경우    
    elif dir_Num == 4:
        positionList[k][0] = 0
        positionList[k][1] = dist_Num

#포지션 리스트에 좌표값 공간 생성 (하나 더 있는 이유는 마지막에 주인공 위치를 넣어야 하기 때문.)
for i in range(shopNum):
    positionList.append([])
    
for i in range(shopNum):
    direction_Num, distance_Num = map(int, input().split()) # 루프돌고 초기화 시켜줘야함
    Save_Coordinate(i, direction_Num, distance_Num) # 좌표값 저장.
#주인공 위치 입력받기.
myDirection, myDistance = map(int, input().split())
#주인공 위치 XY좌표계 변환해서 입력.
Save_Coordinate(shopNum, myDirection, myDistance)

#이제 좌표값과 주인공 위치를 비교하는 과정을 해보자.











#2세션 0  :  widthNum
#3세션 WidthNum  :  heightNum+WidthNum
#1세션 heightNum+WidthNum  :  heightNum+WidthNum+WidthNum
#4세션 heightNum+WidthNum+WidthNum  :  heightNum+WidthNum+WidthNum+heightNum







# for i in range(shopNum):
#     direction_Num, distance_Num = map(int, input().split()) # 루프돌고 초기화 시켜줘야함.
#     if 

# # #블록맵 필드 생성
# # for i in range(widthNum):
# #     blockMapList.append([])
# #     for j in range(heightNum):
# #         blockMapList[i].append(0)

# # #최단거리 구하는 함수
# # def ShortCut(dir, dist):
# #     if dir == 1:
        
# #     elif dir == 2:
        
# #     elif dir == 3:
        
# #     elif dir == 4:
        


# # #샵 위치 입력받기. -> 루프 도는 김에 최단거리 계속 더해나기.
# # for i in range(shopNum):
# #     direction_Num, distance_Num = map(int, input().split()) # 루프돌고 초기화 시켜줘야함.
    




######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
loop 종료가 해결이 안되어서 sys.exit()를 사용했음
비둘기 머리콥터 문제인걸까?
"""