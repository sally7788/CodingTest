from collections import Counter
def solution(want, number, discount):
    answer = 0
    '''
    counter로 세는 건 쉬워 
    들어오고 나가는 것만 센다 
    '''
    def comp(wlist,slist):
        for k in wlist:
            if wlist[k] > slist[k]: #원하는 게 더 많으면 실패 
                return False
        return True
    
    wlist=Counter(dict(zip(want, number)))        
    slist=Counter(discount[:10])
    left=0
    
    for i in range(len(discount)-9):
        if slist == wlist:
            answer+=1
        if i+10 == len(discount):
            break
        slist[discount[i]]-=1
        slist[discount[i+10]]+=1
        
        
    return answer