print(" -=-= P R O G R A M _ S T A R T =-=-")
print(" -----------------------------------")
######################################################

num_List = []
namuji_Temp_List = []
cnt_num =[]

for i in range(10):
    add_Num = int(input())
    num_List.append(add_Num)

for k in range(len(num_List)):
    namuji_Temp = num_List[k] % 42
    namuji_Temp_List.append(namuji_Temp) 

sorted_namuji_Temp_List = sorted(namuji_Temp_List)
#print(sorted_namuji_Temp_List)
Set_Namuji = set(sorted_namuji_Temp_List)

#for t in Set_Namuji:
#    cnt_num.append(Set_Namuji.count(t))
    
    #try: counts[t] += 1
    #xcept: counts[i] = 1
#print(cnt_num)
print(len(Set_Namuji))
#######################################################
print(" -----------------------------------")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")
