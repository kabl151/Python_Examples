"""
<문제 링크>
    https://www.acmicpc.net/problem/2822
    
<풀이 링크>
    -

#----------------------------------------#
#             S U D O _ C O D E          #
#----------------------------------------#




"""
#-----------------------------------------------------
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################
scoreList = []
approvedScore = []
approvedScoreCoordinate = []
TempOriginList = []
coordinatedList =[]
for t in range(8):
    score = int(input())
    scoreList.append(score)

TempOriginList = scoreList

sortedScoreList = sorted(scoreList) #오름차순 정렬.
checkScoreList = sortedScoreList[3:] #상위 5개 점수만 집어 넣음.
for i in range(5):
    # 체크스코어리스트에서의 값을 이용해 스코어리스트 인덱스를 구하는 과정
    # 마지막에 소티드 처리.
    coordinatedList.append((scoreList.index(checkScoreList[i])+1)) # 0부터 들어가서 1씩 더해줌.

totalScore = sum(checkScoreList) #상위 5개 점수 합산.
sortedApprovedScoreCoordi = sorted(coordinatedList) #상위 5개 점수 원래 좌표 오름차순 정렬.

print(totalScore)
print(*sortedApprovedScoreCoordi)

######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
다음부터는 가급적이면 변수 사용을 좀 줄여보자.
"""