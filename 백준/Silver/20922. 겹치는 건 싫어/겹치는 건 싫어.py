n,k=map(int, input().split())
nums=list(map(int, input().split()))

dic=dict()
left=0
max_length=0
for right in range(n):
    num_r=nums[right]
    dic[num_r]=dic.get(num_r,0) + 1
    
    while dic[num_r] > k:
        num_l=nums[left]
        dic[num_l]-=1
        left+=1
    
    max_length=max(max_length, right-left+1)
print(max_length)