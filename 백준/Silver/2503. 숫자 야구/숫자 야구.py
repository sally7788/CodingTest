
def check(candidate, nums):
    strike, ball=0,0
    for i in range(3):
        if candidate[i] == nums[i]:
            strike+=1
        else: 
            if nums[i] in candidate:
                ball+=1
    return strike, ball 

n=int(input())
data = [input().split() for _ in range(n)]
answer=0
  

for i in range(123,1000):
    str_i=str(i)
    if '0' in str_i or len(set(str_i)) != 3:
        continue
    valid=True

    for nums, strike, ball in data:
        strike=int(strike)
        ball=int(ball)

        s, b = check(str_i, nums)
        if strike != s or ball != b:
            valid=False
            break 
    if valid==True:
        answer+=1
print(answer)