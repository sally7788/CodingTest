def solution(lines):
    traffic=[]
    for l in lines:
        _, time, seconds=l.split(" ")
        t,s=time.split(".")
        end_time=(int(t.split(":")[0])*3600000+int(t.split(":")[1])*60000+int(t.split(":")[2])*1000+int(s))
        start_time=end_time-int(float(seconds[:-1])*1000)+1
        traffic.append((start_time, end_time))
    answer=0   
    for start, end in traffic:
        for check in [start, end]:
            window_start=check
            window_end=check+999
            count=0

            for s,e in traffic:
                if (s<=window_end and e >= window_start): 
                    count+=1
            answer=max(answer,count)
 
    return answer
        