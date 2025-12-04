# 맵을 그려.. 
# 마지막부터 시작 아래,오른쪽,위쪽,왼쪽. 벽을 마주치거나 이미 채워져있으면 꺾는다 
# 리스트 다 0으로 채워두고 0이 아니면 패스하는 식으로 
# 좌표 표시도 해야돼.. 

n=int(input())
l=[[0]*n for _ in range(n)]
x,y=0,0

l[x][y]=n**2

dx=[1,0,-1,0]
dy=[0,1,0,-1]
dir=0
tx = ty = None

target=int(input())
for num in range(n*n-1, 0, -1):
    nx=x+dx[dir]
    ny=y+dy[dir]

    if nx < 0 or ny <0 or nx >= n or ny >=n or l[nx][ny] != 0:
        dir=(dir+1)%4
        nx=x+dx[dir]
        ny=y+dy[dir]
    x,y=nx,ny
    l[x][y]=num

    if num==target:
        tx,ty=x+1,y+1
if target==n*n:
    tx,ty=1,1

for n in l:
    print(*n)
print(tx,ty)
