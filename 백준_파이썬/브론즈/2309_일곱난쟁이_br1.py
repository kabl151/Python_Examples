"""
<문제 링크>
    https://www.acmicpc.net/problem/2309
    
<풀이 링크>
    

#----------------------------------------#
#             S U D O _ C O D E          #
#----------------------------------------#

9개 줄 난쟁이 키 입력
for i in range(9):
입력받기 
리스트에 저장하기. append


9명 중 2명 버리기 -> 9C2 (36가지 경우 브루트 포스?)

전체 리스트 있으면 
for i in range(9):
    
    for j in range(8):
    
    list_name.pop(i)
    list_name.pop(j)
    
    if sum(list_name) == 100:
        new_list = sorted(list_name)
        for p in new_list
        print (p)
    else:
        break

"""
#-----------------------------------------------------
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################

import sys

dwarfHieght = []

for t in range(9):
    height = int(input())
    dwarfHieght.append(height)

temp_Height = dwarfHieght
sum_Height = sum(dwarfHieght)
diff_Height = sum_Height - 100

a = 0
if a == 0:
    for i in range(9):
        for j in range(9):
            if dwarfHieght[i] != dwarfHieght[j] and dwarfHieght[i] + dwarfHieght[j] == diff_Height:
                del dwarfHieght[i]
                del dwarfHieght[j-1]
                align_Height = sorted(dwarfHieght)
                dwarfHieght = temp_Height
                for k in align_Height:
                    print(k)
                sys.exit()
            else:
                dwarfHieght = temp_Height
else:
    pass            
######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
""" Comment
loop 종료가 해결이 안되어서 sys.exit()를 사용했음
비둘기 머리콥터 문제인걸까?
"""