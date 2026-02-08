a,b,c,m=map(int, input().split())

work=0
piro=0

for _ in range(24):
    if piro+a <= m:
        piro+=a
        work+=b
    else:
        piro-=c
        if piro < 0:
            piro=0
    
    
print(work)