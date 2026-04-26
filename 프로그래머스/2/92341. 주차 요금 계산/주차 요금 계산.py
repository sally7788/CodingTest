from collections import defaultdict
import math
def time_trans(time):
    hh,mm=map(int, time.split(":"))
    return hh*60+mm

def solution(fees, records):
    answer = []
    
    def fee(time):
        if time <= fees[0]:
            money=fees[1]
        else:
            money=fees[1]+math.ceil((time-fees[0])/fees[2]) * fees[3]
        return money
    inout=defaultdict(list)
    for r in records:
        print(r)
        time, num, _ = r.split(" ")
        inout[num].append(time)
    
    for k in sorted(inout.keys()):
        v=inout[k]
        total_time=0   
        
        if len(v) % 2 != 0: 
            v.append('23:59')            
        
        for i in range(0,len(v),2):
            total_time+=(time_trans(v[i+1])-time_trans(v[i]))
        final_fee=fee(total_time)
                       
        answer.append(final_fee)
            
    return answer