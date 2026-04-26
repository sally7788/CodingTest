graph=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
def find_place(num):
    for i,row in enumerate(graph):
        if num in row:
            return i, row.index(num)
        
def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
     
    
def solution(numbers, hand):
    answer = ''
    ''' 지도 먼저 그리고, 거리 구하는 함수 만들어서 구현하면 될듯 '''
    curr_left_row, curr_left_col=3, 0
    curr_right_row, curr_right_col=3, 2
    
    for num in numbers:
        r,c=find_place(num)
        if num == 1 or num == 4 or num == 7:
            answer+="L"
            curr_left_row, curr_left_col=r,c
            
        elif num == 3 or num == 6 or num == 9:
            answer+="R"
            curr_right_row, curr_right_col=r,c
        else: 
            left_distance=distance(curr_left_row, curr_left_col, r,c)
            right_distance=distance(curr_right_row, curr_right_col, r,c)
            
            if left_distance < right_distance:
                answer+="L"
                curr_left_row, curr_left_col=r,c
                
            elif left_distance > right_distance:
                answer+="R"
                curr_right_row, curr_right_col=r,c
            else: 
                if hand=="left":
                    answer+="L"
                    curr_left_row, curr_left_col=r,c
                else: 
                    answer+="R"
                    curr_right_row, curr_right_col=r,c
                    
                
            
    return answer

