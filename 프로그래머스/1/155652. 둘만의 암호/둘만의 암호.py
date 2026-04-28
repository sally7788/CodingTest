def solution(s, skip, index):
    answer = ''
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha=alpha.replace(i, '')
    
    
    for p in s:
        answer+=alpha[(alpha.find(p)+index) % len(alpha)]
        
    return answer