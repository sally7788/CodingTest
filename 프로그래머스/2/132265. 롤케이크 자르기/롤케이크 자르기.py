from collections import Counter
def solution(topping):
    answer = 0
    
    #둘로 나눴을 때 토핑 개수 세는 함수 필요할거고 
    #동생이 하나씩 갖고, 형이 뻇기는 느낌으로 가야겟다 
    bro1=Counter(topping)
    bro2=dict()
    for t in topping:
        bro2[t]=bro2.get(t,0) +1
        bro1[t]-=1
        if bro1[t] <= 0:
            del bro1[t]
        if len(bro2)==len(bro1):
            answer+=1
            
    
    return answer