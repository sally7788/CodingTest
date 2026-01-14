def solution(book_time):
    answer = 0
    '''
    스택으로 구현
    '''
    def to_minutes(time):
        h,m=map(int,time.split(":"))
        return h*60+m
    
    book_time=sorted([(to_minutes(start), to_minutes(end)+10) for start, end in book_time])
    
    rooms=[]
    for start, end in book_time:
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i]=end
                break
        else: 
            rooms.append(end)
        rooms.sort()
                
    return len(rooms)