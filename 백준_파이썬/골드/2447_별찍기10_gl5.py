N = 3
def PEKA_1(n):
    if n == 3:
        return '***'
    else:
        return f'{PEKA_1(n/3)*3}'
    
def PEKA_2(n):
    if n == 3:
        return '* *'
    else:
        return f'{PEKA_2(n/3)} {PEKA_2(n/3)}'


def sTarK(n):
    if n == 3:
        return "***\n* *\n***"
    else:
        return f'{PEKA_1(n)}\n{PEKA_2(n)}\n{PEKA_1(n)}'

print(sTarK(9))