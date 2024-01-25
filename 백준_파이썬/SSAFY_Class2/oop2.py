class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
        
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
        
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
        
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')
        
        
class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        self.value_c = 'Child'
        
    def show_value(self):
        super().show_value()
        print(f'Value from Child: {self.value_c}')