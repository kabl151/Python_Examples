def PAC(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * PAC(n-1)
    
    
    
N = int(input())
print(PAC(N))