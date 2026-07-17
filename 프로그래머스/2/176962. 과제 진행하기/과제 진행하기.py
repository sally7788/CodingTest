def solution(plans):
    result = []

    def time_trans(x):
        hh,mm=map(int,x.split(":"))
        return hh*60+mm
    
    plans=sorted(plans, key=lambda x: x[1])        
    stack=[]
    
    for i in range(len(plans)-1):
        name, start, play = plans[i]
        play=int(play)

        gap = time_trans(plans[i+1][1])-time_trans(start)

        if play <= gap:
        # 현재 과제 완료
            result.append(name)
        # 남은 gap 동안 stack 처리
            remain_time=gap-play
            while stack and remain_time >0:
                old_name, remain=stack.pop() 
                
                if remain <= remain_time: 
                    result.append(old_name)
                    remain_time-=remain
                else: 
                    stack.append((old_name, remain-remain_time))
                    remain_time=0
        else:
            stack.append((name, play-gap))
        # 현재 과제 남은 시간 stack에 저장

# 마지막 과제 처리
    result.append(plans[-1][0])
# stack 비우기
    while stack: 
        result.append(stack.pop()[0])

    
            
            
    return result