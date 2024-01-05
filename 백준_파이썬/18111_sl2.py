print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
print("")
######################################################

"""

"""
block_Ea = 0
N, M, B = map(int, input().split())

B = block_Ea
map_Entire = []
map_Line = []


det_height_Set = set()
total_Time = 0


#맵 생성
for n in range(N):
    map_Line = list(map(int, input().split()))
    map_Entire.append(map_Line)
    
#print("")
#print(map_Entire)

def Demand_Block():
    for i in range(len(map_Entire)):
        for j in range(len(map_Line)):
            find_Max_Container =[]
            find_Max_Container.append(map_Entire[i][j])
    demand_Number = max(find_Max_Container) - B
    return demand_Number #쌓기에는 부족한 블럭 수를 리턴 받음.

def Think_Action():
    if Demand_Block() > 0:
        Max_Tile_Digging_Once()
    elif Demand_Block() <= 0:
        #! 남은거 쌓고 
        #for b in range(B):
        while B := 0:
            create_field_Container()
            for i in range(len(map_Entire)):
                for j in range(len(map_Line)):
                    if map_Entire[i][j] == min(create_field_Container()):
                        map_Entire[i][j] = map_Entire[i][j] + 1 #뺀다
                        B = B - 1 #블럭뺴기
                        total_Time = total_Time + 1 #시간추가

def create_field_Container(): #1차원 리스트로 리턴 받음.
    find_Container = []
    for i in range(len(map_Entire)):
        for j in range(len(map_Line)):
            find_Container.append(map_Entire[i][j])
    return find_Container

def Max_Tile_Digging_Once():
    #찾고 #뺸다 #블럭+1 #시간+2
    for i in range(len(map_Entire)):
        for j in range(len(map_Line)):
            if map_Entire[i][j] == max(create_field_Container()):
                #해당 블럭이 최댓값과 일치하면
                map_Entire[i][j] = map_Entire[i][j] - 1 #뺀다
                block_Ea = block_Ea + 1 #블럭추가
                total_Time = total_Time + 2 #시간추가
                
def height_Only_Two():
    for i in range(len(map_Entire)):
        for j in range(len(map_Line)):
            det_height_Set.add(map_Entire[i][j])
    height_Ea = len(det_height_Set)
    
    if height_Ea == 2:
        Think_Action()
        
    elif height_Ea > 2:
        #최소 위치에 하나 쌓기
        create_field_Container() #콘테이너 렌더링
        for i in range(len(map_Entire)):
            for j in range(len(map_Line)):
                if map_Entire[i][j] == min(create_field_Container()):
                    map_Entire[i][j] = map_Entire[i][j] + 1 #뺀다
                    B = B - 1 #블럭뺴기
                    total_Time = total_Time + 1 #시간추가
        Think_Action()


while len(set(create_field_Container())) == 1:
    print(map_Entire)
    Think_Action()
    height_Only_Two()

Demand_Block()
print(map_Entire)
print(total_Time)
print(Demand_Block())

Think_Action()
#print(map_Entire)
#print(total_Time)

create_field_Container()
print(create_field_Container())
print(map_Entire)
print(total_Time)

Max_Tile_Digging_Once()
#print(map_Entire)
#print(total_Time)

#! height_Only_Two()
#print(map_Entire)
#print(total_Time)

print(f"{total_Time} {map_Entire[0][0]}")

#######################################################
print("")
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")