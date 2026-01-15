def solution(lines):
    answer = 0
    '''
    누적합으로 해야될듯 
    '''
    times=[]
    for l in lines:
        time=l.split(' ')[1]
        
        end=(int(time.split(":")[0])*3600000 + int(time.split(":")[1])*60000
        + int(time.split(":")[2].split('.')[0])*1000 + int(time.split(":")[2].split('.')[1]))
        start=end-int(float(l.split(' ')[2][:-1])*1000)+1
        
        times.append((start,end))
        
    for start, end in times:
        for check in [start,end]:
            count=0
            window_start=check
            window_end=check+999
            
            for s,e in times:
                if not (s > window_end or e<window_start):
                    count+=1
            answer=max(answer,count)
    return answer