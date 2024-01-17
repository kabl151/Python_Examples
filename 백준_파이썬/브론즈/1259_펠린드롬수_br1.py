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
n = None
numberList = []
a = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        new_n = str(n)
        for nn in new_n:
            numberList.append(nn)
        length_numberList = int(len(numberList))
        length_numberList_div2 = int(len(numberList)/2)
        if len(numberList) == 1:
            print("yes")
            numberList =[]
            
        elif length_numberList % 2 == 0: #짝수일 때
            for i in range(length_numberList_div2):
                if numberList[i] == numberList[length_numberList-1-i]:
                    a = a + 1
                    if a == length_numberList_div2:
                        print("yes")
                        a = 0
                        numberList = []
                else:
                    print("no")
                    a = 0
                    numberList = []
                    break

        elif length_numberList % 2 != 0:#홀수일 때
            for i in range(length_numberList_div2):
                if numberList[i] == numberList[length_numberList-1-i]:
                    a = a + 1
                    if a == length_numberList_div2:
                        print("yes")
                        a = 0
                        numberList = []
                else:
                    print("no")
                    a = 0
                    numberList = []
                    break
######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
0을 입력받으면 종료 메커니즘
while True:
    n = int(input())
    if n == 0:
        break
        
리스트를 잘 다루고 못다루고를 극단적으로 보여주는 문제
"""
#숏코딩
while True:
    a = input()
    b = a[::-1]
    if a == '0':
        break
    elif b == a:
        print("yes")
    else:
        print("no")