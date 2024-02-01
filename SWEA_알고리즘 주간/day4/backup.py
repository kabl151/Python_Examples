def rollin(arr, di,dj,cnt, NN, N, i, j, dir):
    SL = 0
    for i in range(NN+1):
        while cnt < NN+1:
            if dir == SL and 0 <= i <= N-1 and 0 <= j <= N-1:
                while arr[i][j] == 0 and cnt != NN+1:
                    arr[i][j] = cnt
                    if (SL == 0 and j != N-1) or (SL == 1 and i != N-1) or (SL == 2 and j != 0) or (SL == 3 and i != 0):
                        cnt += 1
                        i += di[SL]
                        j += dj[SL]
                else:
                    dir += 1
                    dir %= 4
                    i += di[(SL+1)%4]
                    j += dj[(SL+1)%4]
                    if arr[i][j] != 0:
                        i += di[(SL+2)%4]
                        j += dj[(SL+2)%4]
                        cnt -= 1
                    cnt += 1
            SL += 1
            SL %= 4
    return arr
def delta_Snail(Arr, Np):
    dI = [0,1,0,-1]
    dJ = [1,0,-1,0]
    Cnt,N,NNs,I,J,Dir,Nrr = 1,Np,Np*Np,0,0,0,Arr
    return rollin(Nrr, dI, dJ, Cnt, NNs, N, I, J, Dir)
T = int(input())
for t in range(T):
    N = int(input())
    if N == 1:
        print(f'#{t+1}')
        print(N)
    elif N == 2:
        print(f'#{t+1}')
        print(1, 2)
        print(4, 3)
    else:
        snailLst = []
        for i in range(N):
            snailLst.append([])
            for j in range(N):
                snailLst[i].append(0)
        aswr = delta_Snail(snailLst, N)
        print(f'#{t+1}')
        for n in range(N):
            print(*aswr[n])