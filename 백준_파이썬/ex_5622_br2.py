print(" -----------------------------------")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼")
######################################################
String_input =[]
time_Container = 0
#str_Num_List = [0,1,[A,B,C],[D,E,F],[G,H,I],[J,K,L],[M,N,O],[P,Q,R,S],[T,U,V],[W,X,Y,Z],0]
str_Num_Dic = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}
String_input = list(input())


for i in String_input:
    time_Container = time_Container + str_Num_Dic[f'{i}'] + 1
    
print(time_Container)
#######################################################
print(" ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" -----------------------------------")