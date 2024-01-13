sentenceStr = input("문자열을 입력하세요 : ")
a = []
a.extend(sentenceStr)
temp_List = []

print(a)

for i in range(len(a)):
    temp_List.append(a[i])
    print(*temp_List)
    
    