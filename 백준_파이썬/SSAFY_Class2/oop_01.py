class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')
    
class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    PK = BaseModel.PK
    
class Other(BaseModel):
    pass

class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author,extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type
        
    def display_info(self):
        print(self.PK)
        print(self.data_type)
        print(self.extended_type)
    
    def save(self):
        print('데이터를 확장해서 저장합니다.')
        
        
extended_instance = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균', '확장편')
extended_instance.display_info()
extended_instance.save()


hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
print('Novel 모델 인스턴스의 PK와 save 메서드')
print(hong.PK) #1
print(chun.PK) #2
hong.save() #데이터를 저장합니다
chun.save() #데이터를 저장합니다
print(hong.author) #허균
print(chun.author) #작자미상
print('---')

company = Other('회사', '회사명', '회사 설명', 2000, 2023)
print('Other 모델 인스턴스의 PK와 save 메서드')
print(company.PK) # 3
company.save() # 데이터를 다른 장소에 저장합니다.

print('---')
print('모델 별 타입')
print(Novel.TYPE) #Basic Model
print(Other.TYPE) #Other Model