def draw_StarS(n):
    if n == 1:
        return ['*']

    starsss = draw_StarS(n//3)
    L = []
    
    for star in starsss:
        L.append(star*3)
    for star in starsss:
        L.append(star+' '*(n//3)+star)
    for star in starsss:
        L.append(star*3)
    
    return L

N = int(input())
print('\n'.join(draw_StarS(N)))










# N = 3
# def PEKA_1(n):
#     if n == 3:
#         return '***'
#     else:
#         return f'{PEKA_1(n/3)*3}'
    
# def PEKA_2(n):
#     if n == 3:
#         return '* *'
#     else:
#         return f'{PEKA_2(n/3)*3}'


# def sTarK(n):
#     if n == 3:
#         # return f'***''\n'f'* *''\n'f'***' 
#         return f'{PEKA_1(n)}{PEKA_2(n)}{PEKA_1(n)}'
#     else:
#         tick = f'{sTarK(n/3)*int(n/3)}'
#         return tick

# print(sTarK(9))
