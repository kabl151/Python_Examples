print(" -----------------------------------")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼")
######################################################

A, B = list(map(int, input().split()))

list_A = []
for a in str(A):
    list_A.append(a)
    
list_B = []
for b in str(B):
    list_B.append(b)

list_A.reverse()
list_B.reverse()

reversed_A = int(list_A[0])*100 + int(list_A[1])*10 + int(list_A[2])
reversed_B = int(list_B[0])*100 + int(list_B[1])*10 + int(list_B[2])

if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)
    



#######################################################
print(" ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")