arr = [3,6,7,1,5,4]

n = len(arr) # n 원소의 갯수

for i in range(1<<n): #1<<n 부분집합의 개수
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end='')

    print()
print()


