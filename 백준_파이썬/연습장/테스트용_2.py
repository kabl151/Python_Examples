number_of_people = 0
userInfo = {}
userDB = []
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people
    


def create_user():
    global userInfo
    global name
    global age
    global address
    for i in range(len(name)):
        user_name = name[i]
        user_age = age[i]
        user_address = address[i]
        print(f'{name[i]}님 환영합니다!')
        userInfo = dict(name = user_name, age = user_age, adress = user_address)
        
        userDB_done = userDB.append(userInfo)
    return userDB


many_user = create_user()



def rental_book(bookEa):
    global number_of_book
    for i in range(len(name)):
        decrease_book(bookEa)
        print(f'남은 책의 수 : {number_of_book}')
        
    
        print(f'{many_user[i][name]}님이 {bookEa}권의 책을 대여하였습니다.')
        print(f'남은 책의 수 : {number_of_book}')
        pass

def decrease_book(bookEa):
    global number_of_book
    number_of_book -= bookEa
    


create_user()