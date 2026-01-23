from itertools import permutations

def solution(numbers):
    answer=0
    num=[]
    for i in range(1,len(numbers)+1):
        num.append(list(permutations(numbers, i)))
    num=set([int(''.join(tub)) for sub in num for tub in sub])
    
    
    for n in num:
        if n<2:
            continue
        is_prime=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            answer+=1
        
    return answer