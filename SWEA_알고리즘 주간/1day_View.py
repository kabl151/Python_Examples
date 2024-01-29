for n in range(10): # 10번의 테스트 케이스 반복
    zomang_Floor = 0
    lst_Idx = int(input())
    buildMap = list(map(int, input().split()))
    for B in range(len(buildMap)):
        Lt_clear_Floor, Rt_clear_Floor = 0, 0
        if buildMap[B] != 0:
            
            #왼쪽 조망공간확보 및 카운트
            Lt_space_clear_1 = buildMap[B] - buildMap[B-1] 
            Lt_space_clear_2 = buildMap[B] - buildMap[B-2]
            if Lt_space_clear_1>0 and Lt_space_clear_2>0:
                if Lt_space_clear_1 == Lt_space_clear_2:
                    Lt_clear_Floor = Lt_space_clear_1
                elif Lt_space_clear_1 < Lt_space_clear_2:
                    Lt_clear_Floor = Lt_space_clear_1
                elif Lt_space_clear_1 > Lt_space_clear_2:
                    Lt_clear_Floor = Lt_space_clear_2    
                
            #오른쪽 조망공간확보 및 카운트    
            Rt_space_clear_1 = buildMap[B] - buildMap[B+1] 
            Rt_space_clear_2 = buildMap[B] - buildMap[B+2]
            if Rt_space_clear_1>0 and Rt_space_clear_2>0:
                if Rt_space_clear_1 == Rt_space_clear_2:
                    Rt_clear_Floor = Rt_space_clear_1
                elif Rt_space_clear_1 < Rt_space_clear_2:
                    Rt_clear_Floor = Rt_space_clear_1
                elif Rt_space_clear_1 > Rt_space_clear_2:
                    Rt_clear_Floor = Rt_space_clear_2
            
            #조망권 확보 여부 및 카운트    
            if Lt_clear_Floor > Rt_clear_Floor:
                zomang_Floor += Rt_clear_Floor
            elif Lt_clear_Floor < Rt_clear_Floor:
                zomang_Floor += Lt_clear_Floor
            elif Lt_clear_Floor == Rt_clear_Floor:
                zomang_Floor += Rt_clear_Floor

    print(f'#{n+1} {zomang_Floor}')