#세션 랜덤으로 생성하는 코드
import random
import math
from datetime import datetime

nowTimeStamp = datetime.now()
memberList = []
newMemberList = []
print("----------------------------------------------------------------------------")
print(" ")
memberNum = int(input("스터디 전체 멤버수를 입력하세요. ▶  "))
sessionNumber = int(input("나눌 세션의 수를 입력하세요. ▶  "))

print("----------------------------------------------------------------------------")
print(" ")
#멤버 이름 입력
for t in range(memberNum):
    
    
    print(" ")
    a = str(input(f'{t+1} 번째 멤버 ▶ '))
    memberList.append(a)
    print(f'현재 입력된 멤버는 {memberList} 입니다.')
#멤버 랜덤 셔플
random.shuffle(memberList)

#새로운 세션 생성.
#근데 이거 문제가 있음. 7명 3세션으로 나누면 3-2-2가 아니고 3-3-1로 나누어짐.
for s in range(sessionNumber):
    n = math.ceil(memberNum/sessionNumber) # 한 세션에 속할 수 있는 최대인원.
    newMemberList.append(memberList[n*s:n*(s+1)])
    
#출력
print(" ")
print(f'----------------------결과 출력 일시 : {nowTimeStamp}-----------------------')
print(" ")
for s in range(sessionNumber):
    leader = random.choice(newMemberList[s])
    print(f'# {s+1} 세션의 멤버의 구성원은 {newMemberList[s]} 이고, 세션 리더는 [{leader}]님 입니다.')
    print(" ")
print('-----------------------프로그램 실행 완료------------------------------------------------------------')
