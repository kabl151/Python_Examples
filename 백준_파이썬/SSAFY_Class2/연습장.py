# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, keyy, vallue):
    new_dict = dictionary.copy()
    new_dict[keyy] = vallue

    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
