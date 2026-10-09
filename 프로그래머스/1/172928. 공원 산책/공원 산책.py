def solution(park, routes):
    answer = []
    r={'S': [1,0], "E":[0,1], "W":[0,-1], "N": [-1,0]}
    h=len(park)
    w=len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j]=="S":                
                x,y=i,j
    
    for route in routes:
        dx, dy = r[route.split()[0]]
        n=int(route.split()[1])
        
        cur_x, cur_y=x,y
        for _ in range(n):
            nx,ny=x+dx, y+dy
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w: 
                x,y=cur_x, cur_y
                break
            if park[nx][ny] == "X":
                x,y=cur_x, cur_y
                break
            x,y=nx,ny
                
        
    return [x,y]