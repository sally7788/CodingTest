def solution(participant, completion):
    p_list={}
    c_list={}
    
    for p in participant:
        p_list[p]=p_list.get(p,0) + 1
    for c in completion:
        c_list[c]=c_list.get(c,0) + 1
    
    for p in participant:
        if p_list.get(p) != c_list.get(p):
            return p 
                
   