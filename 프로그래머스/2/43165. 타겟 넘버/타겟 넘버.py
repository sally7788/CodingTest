def solution(numbers, target):
    answer = 0
    hap=0
    def dfs(i,hap):
        nonlocal answer
        if i == len(numbers):            
            if hap == target: 
                answer+=1
            return 
        dfs(i+1, hap+numbers[i])
        dfs(i+1, hap-numbers[i])
    dfs(0,0)
      
    return answer