def solution(plans):
    answer = []
    def ch_time(time):
        mm,dd=map(int,time.split(":"))
        return mm*60 + dd
    plans=sorted(plans, key=lambda x: x[1])  
    stack=[]
    for i in range(len(plans)-1): 
        name, start, dur=plans[i]
        dur=int(dur)
        gap=ch_time(plans[i+1][1])-ch_time(start) 
        if gap >= dur: 
            answer.append(name)
            remain_gap=gap-dur
            while stack and remain_gap > 0:
                old_name, remain =stack.pop()
                
                if remain <= remain_gap: 
                    answer.append(old_name)
                    remain_gap-=remain
                else:
                    stack.append((old_name, remain-remain_gap))
                    remain_gap=0
            
        else:
            stack.append((name, dur-gap))
            
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
            
        
    return answer