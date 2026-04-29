def solution(numbers, target):
    answer = 0
    
    def dfs(idx, hap):
        nonlocal answer
        if idx == len(numbers):
            if hap==target:
                answer+=1
            return #값 없이 함수 종료 
        dfs(idx+1, hap+numbers[idx])
        dfs(idx+1, hap-numbers[idx])
    dfs(0,0)
    return answer
        
        
    