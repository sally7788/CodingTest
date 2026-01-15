def solution(prices):
    answer = [0] * len(prices)
    stack=[]
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            past=stack.pop()
            answer[past]=i-past
        stack.append(i)
        
    while stack:
        past=stack.pop()
        answer[past]=len(prices)-1-past
               
    return answer