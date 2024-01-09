"""
<문제 링크>
https://www.acmicpc.net/problem/2839
"""
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################

# N = int(input())

# k = 0
# # N =5x + 3y
# num_divided_5 = N // 5
# num_divided_3 = (N - (5 * num_divided_5)) // 3
# num_divided_3_First = N // 3

# if N - ((5 * num_divided_5) + (3 * num_divided_3)) == 0:
#     print(num_divided_3 + num_divided_5)
# else: # 5부터 조졌는데 안 될 때.
#     if N - 3 * num_divided_3_First == 0:
#         print(num_divided_3_First)
#     else:
#         for t in range(1000):
#             if (N - (5 * t)) >= 0:
#                 if (N - (5 * t))%3 == 0:
#                     k = (N - (5 * t)) // 3
#                     print( t + k )
#                     break
#         print(-1)
#------------------------------------------------

# N = int(input())

# for t in range(1000):
    
#     if (N - (5 * t)) < 0:
#         if (N - (5 * (t-1)))%3 == 0:
#             k = (N - (5 * (t-1))) // 3
#             print("2", (t-1) + k )
#             break
    
#     if (N - (5 * t)) >= 0:
#         if (N - (5 * t)) == 0:
#             print (t)
#             break
        
#         if (N - (5 * t)) > 0:
#             if (N - (5 * t))%3 == 0:
#                 k = (N - (5 * t)) // 3
#                 print( t + k )
#                 break
            
#     else:
#         print(-1)
#         break
# -----------------------------------------------    
# N = int(input())

# for t in range(1000):
#     if (N - (5 * t)) <= 0:
#         if (N - (5 * t)) == 0:
#             print ("1", t)
#             break
        
#         if (N - (5 * t)) < 0:
#             if (N - (5 * (t-1)))%3 == 0:
#                 k = (N - (5 * (t-1))) // 3
#                 print("2", (t-1) + k )
#                 break
#         else:
#             print(-1)
#             break
#--------------------------------------------------
# N = int(input())
# for i in range(1000):
#     #그리디다. 먼저 큰 거부터 취해보자.
#     if N - (5 * i) >= 0:  #!
#         if N - (5 * i) == 0:
#             print ("1번", N // 5)
#             break
#         #최대한 5를 빼보고 3을 확보한다. 단 성공케이스임.
#         if N - (5 * i) > 0: #!
#             if (N - (5 * i)) % 3 == 0: # 16, 18같은 케이스
#                 print ("2번", i + ((N - (5 * i)) // 3))
#                 print (i)
#                 print (((N - (5 * i)) // 3))
#                 break
            
#             if (N - (5 * i)) % 3 != 0: # 11같은 케이스 #!
#                 if (N - (5 * (i-1))) // 3 == 0:
#                     print("3번",i+(N - (5 * (i-1)) // 3))
#                     break
#                 if (N // 5) != 0:
#                     print(-1)
#                     break
#--------------------------------------------------



for p in range(100):
    n = p
    if n % 5 == 0 and n != 0:
        print("5의 배수 : ", n," : ", n//5)
    elif n == 0:
        print(-1)
        
    elif n < 5 and n % 3 == 0:
        print("5미만 3의 배수 : ", n," : ",n//3)
        
    elif n % 5 != 0: # 처음부터 5로 나누어 떨어지지 않는 경우.
        for i in range(1000): # 11처럼 애초에 3의 배수가 아니지만, 5를 몇 번 빼니까 3으로 나누어 떨어지는 경우.
            #5를 최소한으로 빼야 하는 경우
            if n - (5 * i) > 0 and (n - (5 * i)) % 3 == 0 and n % 3 != 0:
                #print(i)
                #print((n - (5 * i)) % 3)
                print("5를 최소한으로 빼서 해가 있는 경우 : ", n," : ",i + ((n-( 5 * i)) //3))
                break
            
            #18처럼 애초에 '3의 배수지만', 5를 최대한 빼니까 3으로 나누어 떨어지는 경우.
            # ! 5를 최대한 빼야 하는 경우 --> (33,51,69 등에서 오류 발생)
            if n % 3 == 0 and n >= 13: #(18)
                if (n - (5 * (i))) < 0 and (n - (5 * (i-(1)))) % 3 == 0:
                    for k in range(1000):
                        
                        if (n - (5 * (i))) < 0 and (n - (5 * (i-(1+k)))) % 3 == 0:
                            print("5를 최대한 빼서 해가 있는 경우 : ", n,i,k," -> ",(k+1), ((n - (5 * (k+1))) // 3))
                            break
                        #     if (n - (5 * (k+1))) % 3 == 0:
                        #         #print(i)
                        #         #print(k+1)
                        #         print("5를 최대한 빼서 해가 있는 경우 : ", n," : ",k+1 + ((n - (5 * (k+1))) // 3))
                        #         break
                        # else:
                        #     if (n - (5 * (k+1))) % 3 == 0:
                        #         #print(i)
                        #         #print(k+1)
                        #         print("5를 최대한 빼서 해가 있는 경우 : ", n," : ",k+1 + ((n - (5 * (k+1))) // 3))
                        break    
                    break
            if n < 13 and n % 3 == 0:
                print("13 미만의 3의 배수 : ", n," : ",n // 3)
                break
            
            #5보다 크지 않지만, 3으로도 나누어 떨어지는 놈이 아닌 놈들 1,2,4    
            if n < 5 and n % 3 != 0:
                print("노답",n, ":", -1)
                break
        

# 오로지 3의 배수
    
            
            
            #print(-1)
            #break
    

#11은 5가 1개 3이 2개
#######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")