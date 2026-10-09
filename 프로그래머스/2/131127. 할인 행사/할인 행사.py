from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_num={want[i]:number[i] for i in range(len(number))}
    
    for j in range(len(discount)-9):
        sale=dict(Counter(discount[j:j+10]))
        
        for w,n in want_num.items():
            if sale.get(w,0) < n: 
                break
        else: 
            answer+=1
    return answer