import math
def solution(signals):
    def lcm(a,b):
        return a*b // math.gcd(a,b)
    
    time=1
    
    for signal in signals:        
        g,y,r=signal
        total=g+y+r
        time=lcm(total, time) #신호등 최소 공배수 
    
    for i in range(1, time+1):
        isAllYellow=True
        
        for signal in signals:
            g,y,r=signal
            total=g+y+r
            index= i%total #신호등 주기 내에서 몇번째 초인지 알려줌 
            
            if not (index <= g+y and index > g):
                isAllYellow=False
                break 
        if isAllYellow:
            return i
    
    
    return -1