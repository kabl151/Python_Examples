# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        self.name = input('이름을 입력하세요: ')
        self.age = int(input('나이를 입력하세요: '))
        if type(self.name) is str:
            self.user_data['Name'] = self.name
        else:
            print('이름은 문자로 입력되어야 합니다.')
            print('사용자 정보가 입력되지 않았습니다.')
            
        if type(self.age) is int:
            self.user_data['Age'] = self.age
        else:
            print('나이는 숫자로 입력해야 합니다.')
            print('사용자 정보가 입력되지 않았습니다.')
            
        if type(self.age) == None or type(self.name) == None:
            print('사용자 정보가 입력되지 않았습니다.')

    def display_user_info(self):
        print(f'사용자 정보 : ')
        print(f"이름: {self.user_data['Name']}")
        print(f"나이: {self.user_data['Age']}")



user = UserInfo()
user.get_user_info()
user.display_user_info()
