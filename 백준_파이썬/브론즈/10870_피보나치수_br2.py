def Fivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return Fivo(n-1) + Fivo(n-2)



N = int(input())
print(Fivo(N))