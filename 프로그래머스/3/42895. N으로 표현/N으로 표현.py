def solution(N, number):
    dp=[set() for i in range(9)] #n을 쓰는 횟수에 따라서 dp에 저장 
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            for first in dp[j]:
                for second in dp[i-j]: 
                    dp[i].add(first + second)
                    dp[i].add(first*second)
                    dp[i].add(first - second)
                    dp[i].add(second-first)
                    if first != 0:
                        dp[i].add(second//first)
                    if second != 0:
                        dp[i].add(first//second)
        if number in dp[i]:
            return i
                        
    return -1