def solution(wallpaper):
    answer = []
    file_list=[]
    left_x, left_y=float('inf'), float('inf')
    right_x, right_y=0,0
    
    for i,wall in enumerate(wallpaper):
        for j in range(len(wall)):
            if wallpaper[i][j]=='#':
                file_list.append((i,j))
    for file in file_list:
        left_x = file[0] if left_x > file[0] else left_x
        left_y = file[1] if left_y > file[1] else left_y
        right_x= file[0] if right_x < file[0] else right_x
        right_y= file[1] if right_y < file[1] else right_y
        
    answer=[left_x,left_y,right_x+1,right_y+1]
    return answer