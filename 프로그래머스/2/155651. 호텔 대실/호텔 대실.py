def solution(book_time):
    answer = 0
    def to_minute(time):
        h,m=time.split(':')
        return int(h)*60+int(m)
    
    total_time=[0 for _ in range(24*60)]
    for start,end in book_time:
        m_start=to_minute(start)
        m_end=to_minute(end)+10 if to_minute(end)+10 <= 24*60-1 else 24*60-1      
        for i in range(m_start,m_end):
            total_time[i]+=1
    return max(total_time)

        