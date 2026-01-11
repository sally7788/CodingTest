n,new,p=map(int, input().split())
if n>0:
    ranking=list(map(int, input().split()))
else: 
    ranking=[-1]


if n==p and new <= ranking[-1]:
    print(-1)
    exit()

rank=1
for score in ranking:
    if score > new:
        rank+=1
    else: break
    
print(rank)
