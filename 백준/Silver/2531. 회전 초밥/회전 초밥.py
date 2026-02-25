from collections import defaultdict

n,d,k,c=map(int, input().split())
plates=[int(input()) for _ in range(n)]
plates+=plates[:k-1]

pset=defaultdict(int)
pset[c]+=1

for i in range(k):
    pset[plates[i]]+=1

max_kinds=len(pset)

for i in range(n):
    left=plates[i]
    pset[left]-=1
    if pset[left] == 0:
        del pset[left]
    right_idx=(i+k)%n
    right=plates[right_idx]
    pset[right]+=1

    max_kinds=max(max_kinds, len(pset))
print(max_kinds)