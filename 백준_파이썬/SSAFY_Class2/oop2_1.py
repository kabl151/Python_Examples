# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1
    pass


class Dog(Animal):
    sound = '멍멍'
    def __init__(self):
        pass
        


class Cat(Animal):
    sound = '야옹'
    def __init__(self):
        pass
        


class Pet(Dog, Cat):
    def __init__(self):
        self.sori = super().sound
        
    def __str__(self):
        return f'애완동물은 {self.sori} 소리를 냅니다.'


pet1 = Pet()
print(pet1)


