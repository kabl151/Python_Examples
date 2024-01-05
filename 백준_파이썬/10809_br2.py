print(" -----------------------------------")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼")
######################################################

ex_Str = str(input())
alphabet_List = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
coordi_List = []

#print(alphabet_List)

#알파벳 좌표 리스트 생성
for alp in range(26):
    coordi_List.append(0)
    
#있으면 '인덱스'위치 삽입, 없으면 '-1'삽입.
for s in alphabet_List:
    
    if s in ex_Str:
        coordi_List[alphabet_List.index(s)] = ex_Str.find(s)

    else:
        coordi_List[alphabet_List.index(s)] = ex_Str.find(s)

#최종 출력
print(*coordi_List)


#######################################################
print(" ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")