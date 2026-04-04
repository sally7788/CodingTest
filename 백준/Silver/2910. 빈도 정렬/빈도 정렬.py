n,c=map(int, input().split())
nums=list(map(int, input().split()))

freq={}
order={}

for i,n in enumerate(nums):
    if n not in order:
        freq[n]=0
        order[n]=i
    freq[n]+=1

nums.sort(key=lambda x: (-freq[x], order[x]))
print(*nums)