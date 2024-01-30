N = 6
k = 9
data = [7,2,4,5,2,3] #원본 배열
counts = [0]*(k+1) #횟수 기록하는 배열
temp = [0]*N

#counts 배열에 기록하기 -- 횟수가 기록됨.
for x in data:
    counts[x] += 1
    
#counts 누적합 구하기 -- counts 정렬 항목의 앞에 위치할 항목의 개수를 반영하기 위해 카운트 원소 조정
for i in range(1, k+1):
    counts[i] += counts[i-1] + counts[i] #i번째에는 i-1번째 개수와 현재 값을 저장 == 누적
#나중에 그 누적합이 temp의 인덱스로 쓰인다.!!!!!    
    
    
#data의 마지막 원소부터 정렬하기
for i in range(N-1, -1, -1): #N-1 -> 0번 인덱스
    counts[data[i]] -= 1 #개수를 인덱스로 변환(남은 개수 계산)
    temp[counts[data[i]]] = data[i]
    
    
print(*temp)