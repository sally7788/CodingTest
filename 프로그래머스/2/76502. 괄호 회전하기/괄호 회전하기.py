def match(sen):
    
    pair = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    stack=[]
    
    for s in sen:
        if s not in pair:
            stack.append(s)
        else: 
            if not stack or pair[s] != stack[-1]: 
                return False
            
            stack.pop()
    if stack:
        return False
    return True 
            
                
            
def solution(s):
    answer = 0
    '''
    올바른 괄호 문자열인지 확인하는 함수 
    돌리기...반복문 써서 돌리면 될듯 
    '''
    
    for x in range(len(s)):
        rotated=s[x:]+s[:x]
        if match(rotated):
            answer+=1
            
    return answer