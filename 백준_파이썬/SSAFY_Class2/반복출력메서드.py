# 아래 클래스를 수정하시오.
class StringRepeater:
    
    def __init__(self):
        pass
    
    def repeat_string(self,times,msg):
        for i in range(times):
            print(f'{msg}')


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
