def delta_Snail(arr, N):
    dI = [0,1,0,-1]
    dJ = [1,0,-1,0]
    Cnt = 1
    NNs = N*N
    I, J = 0, 0
    Dir = 0
    

    
    while cnt < NN+1:
        if dir == 0 and 0 <= i <= N-1 and 0 <= j <= N-1:
            while arr[i][j] == 0 and cnt != NN+1:
                arr[i][j] = cnt
                if j != N-1:
                    cnt += 1
                    i += di[dir]
                    j += dj[dir]
            else:
                dir += 1
                dir %= 4
                i += di[dir]
                j += dj[dir]
                if arr[i][j] != 0:
                    i += di[(dir+1)%4]
                    j += dj[(dir+1)%4]
                    cnt -= 1
                cnt += 1
                
        elif dir == 1 and 0 <= i <= N-1 and 0 <= j <= N-1:
            while arr[i][j] == 0 and cnt != NN+1:
                arr[i][j] = cnt
                if i != N-1:
                    cnt += 1
                    i += di[dir]
                    j += dj[dir]
            else:
                dir += 1
                dir %= 4
                i += di[dir]
                j += dj[dir]
                if arr[i][j] != 0:
                    i += di[(dir+1)%4]
                    j += dj[(dir+1)%4]
                    cnt -= 1
                cnt += 1
                
        elif dir == 2 and 0 <= i <= N-1 and 0 <= j <= N-1:
            while arr[i][j] == 0 and cnt != NN+1:
                arr[i][j] = cnt
                if j != 0:
                    cnt += 1
                    i += di[dir]
                    j += dj[dir]
            else:
                dir += 1
                dir %= 4
                i += di[dir]
                j += dj[dir]
                if arr[i][j] != 0:
                    i += di[(dir+1)%4]
                    j += dj[(dir+1)%4]
                    cnt -= 1
                cnt += 1
                
        elif dir == 3 and 0 <= i <= N-1 and 0 <= j <= N-1:
            while arr[i][j] == 0 and cnt != NN+1:
                arr[i][j] = cnt
                if i != 0:
                    cnt += 1
                    i += di[dir]
                    j += dj[dir]
            else:
                dir += 1
                dir %= 4
                i += di[dir]
                j += dj[dir]
                if arr[i][j] != 0:
                    i += di[(dir+1)%4]
                    j += dj[(dir+1)%4]
                    cnt -= 1
                cnt += 1
    return arr                    


T = int(input())
for t in range(T):
    N = int(input())
    
    snailLst = []
    
    for i in range(N):
        snailLst.append([])
        for j in range(N):
            snailLst[i].append(0)
    aswr = delta_Snail(snailLst, N)
    print(f'#{t+1}')
    for n in range(N):
        print(*aswr[n])