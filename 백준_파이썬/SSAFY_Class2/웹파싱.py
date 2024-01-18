import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
#API_URL = 'https://jsonplaceholder.typicode.com/users/1'
API_URL = 'https://jsonplaceholder.typicode.com/users'

# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
#print(response)

# 변환 데이터 출력
#print(parsed_data)
# 변환 데이터의 타입
#print(type(parsed_data))
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

#블랙리스트에 포함되지 아니한 회사만 등록할 수 있도록.
#문제가 있으면 {회사명} 소속의 {이용자명} 은/는 등록할 수 없습니다.
#문제가 없으면 이상이 없다고 이야기하기.

#검열이 되면 cencered_Dict = {'company 명': '유저명'}
#censored_user_list.append(cencered_Dict) 같은 느낌으로 구현
print(parsed_data)

censored_user_list ={}
censored_user_list_temp={}
def create_user(): # 여기서 리스트 체크
    for i in range(len(parsed_data)):
        company_name = str(parsed_data[i]['company']['name'])
        user_name = str(parsed_data[i]['name'])
        if censorship(company_name, user_name):
            pass
        else:    
            censored_user_list[company_name] = [user_name] # 유저 저장.
    print(censored_user_list)
    pass

def censorship(company_name, user_name):
    if company_name in black_list:
        print(f'{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

create_user()

######################################################################
# 특정 데이터 출력
# dummy_data = []
# dummy_dict_TEMP = {'company':'','lat':'','lng':'','name':''}

# for i in range(10):
#     dummy_dict_TEMP['company'] = parsed_data[i]['company']['name']
#     dummy_dict_TEMP['lat'] = parsed_data[i]['address']['geo']['lat']
#     dummy_dict_TEMP['lng'] = parsed_data[i]['address']['geo']['lng']
#     dummy_dict_TEMP['name'] = parsed_data[i]['name']
#     dummy_data.append(dummy_dict_TEMP)
#     dummy_dict_TEMP = {'company':'','lat':'','lng':'','name':''} # 초기화


# print(dummy_data)
