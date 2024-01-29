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


for i in range(n-m+1):
    tmp_sum.append(preArr[i+m] - preArr[i])

#단위별 온도 합계 쌓인 리스트에서 max() 사용하여 최댓값 산출
print(max(tmp_sum))





















# n,m=map(int,input().split())   # n: 입력받을 정수의 개수, m: 연속된 구간의 크기 (10, 5)
# arr=list(map(int,input().split()))

# Max,sum=0,0

# for i in range(m): # 처음 m개의 구간 (0번 인덱스부터 4번인덱스)의 합 구하기
#     sum+=arr[i]

# for i in range(n-m+1): 
#     if sum>Max:
#         Max=sum
#     if i==n-m: break
#     sum+=arr[i+m] # i+m: 5~10
#     sum-=arr[i]   # i: 0~5

# print(Max)















######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
loop 종료가 해결이 안되어서 sys.exit()를 사용했음
비둘기 머리콥터 문제인걸까?
"""