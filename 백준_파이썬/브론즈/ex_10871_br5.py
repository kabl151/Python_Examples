print(" -----------------------------------")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼")
######################################################
N, X = map(int,input().split())
new_List = list(map(int,input().split()))

sol_List =[]

for i in new_List:
    if i < X:
        sol_List.append(i)

print(*sol_List)
#######################################################
print(" ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")