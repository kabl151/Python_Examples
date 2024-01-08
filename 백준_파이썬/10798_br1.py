"""
<문제 링크>
https://www.acmicpc.net/problem/10798
"""
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################
matrixField = []
resultField = []
tempList = []

#매트릭스 필드 생성
for i in range(5):
    matrixField.append([])
    str = list(list(input())) 
    for item in str:
        matrixField[i].append(item)    
    str = [] # str 리스트 초기화

#임시 리스트 생성(최대 15글자 까지 들어가기 때문)
for k in range(15):
    tempList.append([])

#임시 리스트에 저장된 것들 매트릭스 필드에 저장(오류는 패스- 인데스 오류임. 존재하지 않은 주소들)
for k in range(15):
    for n in range(5):
        try:
            tempList[k].append(matrixField[n][k])
        except:
            pass

#이차원 배열이던거 1차원으로 다운그레이드.
for n in range(15):
    for k in range(15):
        
        try:
            resultField.append(tempList[n][k])
                        
        except:
            pass

#결과 출력
for p in resultField:
    print(p, end="")

#######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")