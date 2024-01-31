import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temperatureArr = list(map(int, input().split()))


#누적합을 구하는 방식으로 접근할 예정
preArr = [0]
tmp_sum = []
mysum = 0

#누적합을 쌓을 리스트 : mysum
for i in range(n):
    mysum += temperatureArr[i]
    preArr.append(mysum)
    print(mysum)
print(preArr)


for i in range(n-m+1):
    tmp_sum.append(preArr[i+m] - preArr[i])

print((tmp_sum))
#단위별 온도 합계 쌓인 리스트에서 max() 사용하여 최댓값 산출
print(max(tmp_sum))
