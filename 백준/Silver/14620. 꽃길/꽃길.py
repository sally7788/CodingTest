n=int(input())
ground=[list(map(int,input().split())) for _ in range(n)]

def cost(x,y):
    return ground[x][y]+ground[x+1][y]+ground[x-1][y]+ground[x][y+1]+ground[x][y-1]

def cells(x,y):
    return {(x,y),(x-1,y),(x+1,y),(x,y+1),(x,y-1)}        

answer=float("inf")

positions= [ (i,j) for i in range(1,n-1) for j in range(1,n-1)]

for i in range(len(positions)):
    x1,y1=positions[i]
    s1=cells(x1,y1)
    c1=cost(x1,y1)

    for j in range(i+1, len(positions)):
        x2,y2=positions[j]
        s2=cells(x2,y2)

        if s1 & s2:
            continue
        c2=cost(x2,y2)

        for k in range(j+1, len(positions)):
            x3,y3=positions[k]
            s3=cells(x3,y3)

            if s1 & s3 or s2 & s3:
                continue
            c3=cost(x3,y3)

            answer=min(answer, c1+c2+c3)
print(answer)