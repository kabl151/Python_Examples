print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################

score_Mark = {'A+': 4.5, 'A0': 4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,'D+':1.5, 'D0':1.0, 'F':0.0 }
total_Score = 0.0
su = 20
div_Count = 20
hack_jeom = 0.0
div_hack_jeom = 0.0

for ea in range(su):
    Temp_list = list(input().split())

    if Temp_list[2] == 'A+':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['A+'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])
        
    elif Temp_list[2] == 'A0':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['A0'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])
        
    elif Temp_list[2] == 'B+':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['B+'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])
        
    elif Temp_list[2] == 'B0':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['B0'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])

    elif Temp_list[2] == 'C+':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['C+'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])

    elif Temp_list[2] == 'C0':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['C0'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])

    elif Temp_list[2] == 'D+':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['D+'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])

    elif Temp_list[2] == 'D0':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['D0'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])

    elif Temp_list[2] == 'F':
        total_Score = total_Score + float(Temp_list[1]) * float(score_Mark['F'])
        div_hack_jeom = div_hack_jeom + float(Temp_list[1])

    elif Temp_list[2] == 'P':
        div_Count = div_Count -1


hack_jeom = total_Score/div_hack_jeom
print(float(hack_jeom))

#EOF /?////// 온라인 코테에서 나오는 오류임.
#######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")