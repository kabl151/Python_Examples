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

# 특정 데이터 출력

dummy_data = []
dummy_dict_TEMP = {'company':'','lat':'','lng':'','name':''}

for i in range(10):
    dummy_dict_TEMP['company'] = parsed_data[i]['company']['name']
    dummy_dict_TEMP['lat'] = parsed_data[i]['address']['geo']['lat']
    dummy_dict_TEMP['lng'] = parsed_data[i]['address']['geo']['lng']
    dummy_dict_TEMP['name'] = parsed_data[i]['name']
    dummy_data.append(dummy_dict_TEMP)
    dummy_dict_TEMP = {'company':'','lat':'','lng':'','name':''} # 초기화


print(dummy_data)
