arr = [input() for _ in range(5)]
res = ''

for i in range(15):
    for j in range(5):
        try:
            res += arr[j][i]
        except IndexError:
            pass
print(res)