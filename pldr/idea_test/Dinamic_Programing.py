
d = [0]*100 # 하나의 리스트 안에 0을 100개 생성함.
#필드 생성은 기본. -> 그냥 공란으로 두는게 아니라 일단 주소를 호출해야 하기 때문에 0이라도 넣어서 인덱스를 생성

def fibo(x): #보통 그 항의 '번호'를 변수로 준다. 왜? '몇 항'인지 대입하면 값을 나오게 하는게 우리 목표니까.
    if x == 1 or x == 2: #1항이나 2항은 값이 1이니까.
        return 1
    
    if d[x] != 0: # !! 함수 말고 내부 수식 하나 생성, 위에 생성된 "리스트"를 이용.
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환.
    d[x] = fibo(x-1) + fibo(x-2) 
    
    return d[x]

print(fibo(10))