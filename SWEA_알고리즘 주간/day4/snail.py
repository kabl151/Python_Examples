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
    Cnt = 1
    N = Np
    NNs = N*N
    I, J = 0, 0
    Dir = 0
    Nrr = Arr
    return rollin(Nrr, dI, dJ, Cnt, NNs, N, I, J, Dir)
    


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


# def delta_Snail(arr, N):
#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     cnt = 1
#     NN = N*N
#     i, j = 0, 0
#     dir = 0
#     while cnt < NN+1:
#         if dir == 0 and 0 <= i <= N-1 and 0 <= j <= N-1:
#             while arr[i][j] == 0 and cnt != NN+1:
#                 arr[i][j] = cnt
#                 if j != N-1:
#                     cnt += 1
#                     i += di[0]
#                     j += dj[0]
#             else:
#                 dir += 1
#                 dir %= 4
#                 if arr[i][j] != 0:
#                     j -= 1
#                     cnt -= 1
#                 i += di[1]
#                 cnt += 1
                
#         elif dir == 1 and 0 <= i <= N-1 and 0 <= j <= N-1:
#             while arr[i][j] == 0 and cnt != NN+1:
#                 arr[i][j] = cnt
#                 if i != N-1:
#                     cnt += 1
#                     i += di[1]
#                     j += dj[1]
#             else:
#                 dir += 1
#                 dir %= 4
#                 if arr[i][j] != 0:
#                     i -= 1
#                     cnt -= 1
#                 j += dj[2]
#                 cnt += 1
                
#         elif dir == 2 and 0 <= i <= N-1 and 0 <= j <= N-1:
#             while arr[i][j] == 0 and cnt != NN+1:
#                 arr[i][j] = cnt
#                 if j != 0:
#                     cnt += 1
#                     i += di[2]
#                     j += dj[2]
#             else:
#                 dir += 1
#                 dir %= 4
#                 if arr[i][j] != 0:
#                     j += 1
#                     cnt -= 1
#                 i += di[3]
#                 cnt += 1
                
#         elif dir == 3 and 0 <= i <= N-1 and 0 <= j <= N-1:
#             while arr[i][j] == 0 and cnt != NN+1:
#                 arr[i][j] = cnt
#                 if i != 0:
#                     cnt += 1
#                     i += di[3]
#                     j += dj[3]
#             else:
#                 dir += 1
#                 dir %= 4
#                 if arr[i][j] != 0:
#                     i += 1
#                     cnt -= 1
#                 j += dj[0]
#                 cnt += 1
#     return arr                    


# T = int(input())
# for t in range(T):
#     N = int(input())
    
#     snailLst = []
    
#     for i in range(N):
#         snailLst.append([])
#         for j in range(N):
#             snailLst[i].append(0)
#     aswr = delta_Snail(snailLst, N)
#     print(f'#{t+1}')
#     for n in range(N):
#         print(*aswr[n])



