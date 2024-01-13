print(" -----------------------------------")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼")
######################################################
first_num = int(input())
second_num = int(input())

a_1 = first_num//100
a_2 = (first_num-(a_1*100))//10
a_3 = (first_num -(a_1*100)-(a_2*10))

b_1 = second_num//100
b_2 = (second_num-(b_1*100))//10
b_3 = (second_num -(b_1*100)-(b_2*10))

print(first_num*b_3)# 3번라인
print(first_num*b_2)
print(first_num*b_1)
print(first_num*second_num)
#######################################################
print(" ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")