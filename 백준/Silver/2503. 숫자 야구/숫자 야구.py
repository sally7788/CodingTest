def check(candidate, condition):
    strike, ball =0,0
    for i in range(3):
        if candidate[i]==condition[i]:
            strike+=1
        elif candidate[i] in condition:
            ball+=1
    return strike, ball 

n=int(input())
questions=[tuple(map(int,input().split())) for _ in range(n)]
answer=0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a==b or a==c or b==c:
                continue
            candidate=str(a)+str(b)+str(c)
            ok=True
            for num, st, ba in questions:
                strike,ball = check(candidate, str(num))
                if strike != st or ball != ba:
                    ok=False
                    break 
            if ok:
                answer+=1
print(answer)
