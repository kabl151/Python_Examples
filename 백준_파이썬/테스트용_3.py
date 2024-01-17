number_of_book = 100

def rental_book(name, bookEa):
    global number_of_book
    decrease_book(bookEa)
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{name}님이 {bookEa}권의 책을 대여하였습니다.')
    pass

def decrease_book(bookEa):
    global number_of_book
    number_of_book -= bookEa
    pass

print(f'남은 책의 수 : {number_of_book}')


name = str(input('이름을 입력하세요. : '))
bookNum = int(input('대여할 책의 권 수를 입력하세요. : '))

rental_book(name, bookNum)


