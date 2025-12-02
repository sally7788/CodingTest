from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    order=input().split()

    pcnt=Counter(order)
    under_team=[]
    winning=''

    for k,v in pcnt.items():
        if v != 6:
            under_team.append(k)

    dic={}
    i=1
    for o in order:
        if o not in under_team:
            if o not in dic:
                dic[o]=[]
            dic[o].append(i)
            i+=1

    score={}
    for k,v in dic.items():
        score[k] = sum(v[:4])

    

    min_score=min(score.values())

    candidates=[k for k,v in score.items() if v==min_score]

    if len(candidates)==1:
        print(candidates[0])
    else: 
        winning=min(candidates, key=lambda x:dic[x][4])

        print(winning)