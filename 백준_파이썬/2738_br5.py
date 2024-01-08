print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(" -=-= P R O G R A M _ S T A R T =-=-")
print("▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽ ▼▽")
######################################################


N, M = map(int, input().split())
Matrix_list_1 = []
Matrix_list_2 = []

for n in range(N):
    Matrix_list_1.append(list(map(int, input().split())))
    
for n in range(N):
    Matrix_list_2.append(list(map(int, input().split())))

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
solution(Matrix_list_1, Matrix_list_2)
for k in range(N):
    print(*Matrix_list_1[k])
"""
def Mat_new(N):
    for n in range(N):
        Temp_List = list(map(int, input().split()))
        Matrix_list.append(Temp_List)
    return Matrix_list

Mat_new(N) = Matrix_list_1
Mat_new(N) = Matrix_list_2
"""


#EOF /?////// 온라인 코테에서 나오는 오류임.
#######################################################
print(" △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲ △ ▲")
print(" -=-=   P R O G R A M _ E N D   =-=-")
print(" ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")