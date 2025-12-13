h,w=map(int, input().split())
gr=list(map(int, input().split()))

result=0
for i in range(1,w-1):
    left=max(gr[:i])
    right=max(gr[i+1:])
    comp=min(left,right)

    if comp > gr[i]:
        result+=(comp-gr[i])    
print(result)