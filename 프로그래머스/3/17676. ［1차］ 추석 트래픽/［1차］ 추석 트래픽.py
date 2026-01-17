def solution(lines):
    traffic=[]
    for l in lines:
        _, time, duration= l.split(' ')
        h,m,s=time.split(":")
        end=(int(h)*3600000 + int(m)*60000
        +int(s.split(".")[0])*1000 + int(s.split(".")[1]))
        start=end-int(float(duration[:-1])*1000)+1
        traffic.append((start, end))
    answer=0
    for start,end in traffic:
        for check in [start, end]:
            count=0
            window_start=check
            window_end=check+999
            
            for s,e in traffic:
                if not (s > window_end or e < window_start):
                    count+=1
            
            answer=max(count,answer)
    return answer
        