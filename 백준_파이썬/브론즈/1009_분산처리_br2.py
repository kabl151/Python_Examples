print(" -----------------------------------")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼")
######################################################

#파이썬 시간 오래걸리는걸 보여주는 극단적인 문제임.
import sys
sys.set_int_max_str_digits(10000000) # 최대 입력 자리수 확장시키는 방법.

T = int(input())

for t in range(T): #테스트케이스 루프
    
    a, b = map(int, input().split())
    totalData = a ** b
    
    trans_totalData = str(totalData) #토탈데이터 문자열로 만들어야 마지막 문자열 접근 가능.
    print(trans_totalData[-1])

#######################################################
print(" ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")