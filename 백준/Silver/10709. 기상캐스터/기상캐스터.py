h, w = map(int, input().split())
sky = []

for _ in range(h):
    row=input()
    result=[]
    dist=-1
    for ch in row:
        if ch=='c':
            dist=0
            result.append(0)
        else:
            if dist != -1:
                dist+=1
                result.append(dist)
            else: 
                dist=-1
                result.append(-1)
    sky.append(result)
        
for s in sky:
    print(*s)