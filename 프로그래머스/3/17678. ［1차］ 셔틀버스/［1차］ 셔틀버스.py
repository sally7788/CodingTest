def time_trans(time):
    hh,mm=map(int, time.split(":"))
    return hh*60 + mm

def time2answer(time):
    hh=time//60 
    mm=time%60 
    
    hh= str(hh) if hh >= 10 else '0'+str(hh)
    mm= str(mm) if mm >= 10 else '0'+str(mm)
    return hh+":"+mm

def solution(n, t, m, timetable):
    answer = ''
    bus_time=[]
    crew=[]
    
    
    timetable.sort()
    for time in timetable: 
        new=time_trans(time)
        crew.append(new)
        
    bus_time=540
    
    idx=0
    for i in range(n):
        cnt=0
        
        while cnt < m and idx < len(crew) and crew[idx] <= bus_time:
            idx+=1
            cnt+=1
        if i == n-1: #마지막 버스 
            if cnt < m:
                return time2answer(bus_time)
            else: 
                return time2answer(crew[idx-1]-1)
        bus_time+=t
    