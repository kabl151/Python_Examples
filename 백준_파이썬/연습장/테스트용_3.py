# 6. 리스트에서 중복되어 있지 않은 요소 반환(하나 반환, 여러개 반환)
def no_double(origin_list):
    count_Dict = {} #딕셔너리에 넣는 방법
    for i in origin_list:
        count_Dict[i] = count_Dict.get(i, 0) + 1 #카운트 딕셔너리에 i라는 키값이 없다면 0을 세팅해주지만,
                                                #기본적으로 하나가 나오기 때문에 1을 더해줌.
    
    no_Dupli_List = [] #한 번만 등장한 숫자를 받아올 리스트
    for key, value in count_Dict.items(): #딕셔너리에 키와 밸류를 받아옴.
        if value == 1: #그 중에 밸류값이 1이라면
            no_Dupli_List.append(key)   #리스트에 키 값을 추가!
            
    return no_Dupli_List

    # list_copy = origin_list[:]
    # list_copy.sort()
    # for i in list_copy:
    #     if i not in origin_list:
    #         return i
        
a_list = [1,2,2,3,3,4,4,5]
print(no_double(a_list))