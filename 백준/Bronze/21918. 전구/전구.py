def doing(a,b,c,l):
    if a==1:
        l[b-1]=c
    elif a==2:
        for i in range(b,c+1):
            if l[i-1]==1:
                l[i-1]=0
            else: l[i-1]=1
    elif a==3:
        for i in range(b,c+1):
            l[i-1]=0
    else: 
        for i in range(b,c+1):
            l[i-1]=1
    return l
n, m= map(int,input().split())
l=list(map(int,input().split()))

for _ in range(m):
    a,b,c=map(int,input().split())
    l=doing(a,b,c,l)

print(' '.join(map(str,l)))