aPT_List = []
for s in range(15):
    aPT_List.append([])

for s in range(15): # floor
    print(s)#0층 부터 14층 까지
    for i in range(14): # section
        aPT_List[s].append(0)
        
print(aPT_List)