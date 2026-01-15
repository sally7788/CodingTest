def solution(book_time):
    answer = 0
    
    def to_minutes(time):
        h,m=map(int,time.split(":"))
        return h*60+m
    
#     book_time=sorted([(to_minutes(start), to_minutes(end)+10) for start, end in book_time])
    
#     rooms=[]
#     for start, end in book_time:
#         for i in range(len(rooms)):
#             if rooms[i] <= start:
#                 rooms[i]=end
#                 break
#         else: 
#             rooms.append(end)
#         rooms.sort()
                
#     return len(rooms)
    time_table=[0 for _ in range(60*24)]
    
    for start, end in book_time:
        start,end=to_minutes(start),to_minutes(end)+10
        if end > 60*24-1:
            end=60*24-1
        for i in range(start,end):
            time_table[i]+=1
    return max(time_table)
            
        