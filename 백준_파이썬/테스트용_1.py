import random
정답 = random.randint(1,100)
몇번 = 1 
print('** 숫자를 맞춰보세요(1~100). 0을 입력하면 프로그램을 종료합니다.')

while True :
    입력값 = int(input('숫자를 입력하세요(1~100)'))
    if 입력값 == 0 : 
        print('프로그램을 종료합니다.')
        break
    elif 입력값 > 100 : 
        print('잘못된 값이 입력됐습니다.')
        continue
    elif 입력값 == 정답 : 
        print('정답입니다!')
        print(str(몇번)+'번만에 맞추셨습니다!')
        break
    elif 입력값 > 정답 : 
        print('더 작은 숫자입니다~')
        몇번 += 1
        continue
    elif 입력값 < 정답 :
        print('더 큰 숫자입니다~')
        몇번 += 1
        continue