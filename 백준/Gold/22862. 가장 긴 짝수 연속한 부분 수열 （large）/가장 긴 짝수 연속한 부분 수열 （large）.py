n,k=map(int,input().split())
nums=list(map(int, input().split()))

left=0
odd=0
answer=0

for right in range(n):
    if nums[right] % 2 != 0:
        odd+=1
    while odd > k:
        if nums[left] % 2 != 0:
            odd-=1
        left+=1
    answer=max(answer, (right-left+1)-odd)
print(answer)
