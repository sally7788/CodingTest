n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dy=[0,-1,1]
def dfs(r,c,last_dir,score):
    global min_fuel 

    if r == n-1:
        min_fuel=min(min_fuel, score)
        return #여기서 함수 끝
    
    if score >= min_fuel:
        return
    
    for i in range(3):
        if i == last_dir:
            continue
        next_r=r+1
        next_c=c+dy[i]

        if 0<= next_c < m:
            dfs(next_r, next_c,i,score+graph[next_r][next_c])

min_fuel=float('inf')

for j in range(m):
    dfs(0,j,3,graph[0][j])
print(min_fuel)
