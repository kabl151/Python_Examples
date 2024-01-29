N = 6
arr = [7,2,5,3,1,4]

for i in range(N-1, 0,-1 ):
    for j  in range(i): # range(i) 이유에 대해서 더 생각해보자.
        if arr[j] > arr[j+1]: #왼쪽이 더 크다면
            arr[j], arr[j+1] = arr[j+1], arr[j] # 위치교환
            
print(arr)

def dec(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
dec(arr, N)
print(arr)