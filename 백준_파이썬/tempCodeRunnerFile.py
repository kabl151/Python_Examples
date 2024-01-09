N = int(input())
k = 0
# N =5x + 3y
num_divided_5 = N // 5
num_divided_3 = (N - (5 * num_divided_5)) // 3
num_divided_3_First = N // 3

if N - ((5 * num_divided_5) + (3 * num_divided_3)) == 0:
    print(num_divided_3 + num_divided_5)
else: # 5부터 조졌는데 안 될 때.
    if N - 3 * num_divided_3_First == 0:
        print(num_divided_3_First)
    else:
        for t in range(1000):
            if (N - (5 * t)) >= 0:
                if (N - (5 * t))%3 == 0:
                    k = (N - (5 * t)) // 3
                    print( t + k )
                    break
        print(-1)