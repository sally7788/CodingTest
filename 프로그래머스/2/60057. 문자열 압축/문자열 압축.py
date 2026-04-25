def solution(s):
    answer = 0
    
    length=len(s)
    min_length=length
    for l in range(1, length):
        arr=""
        prev=s[0:l]
        cnt=1
        
        for i in range(l,length,l):
            cur=s[i:i+l]
            
            if prev==cur:
                cnt+=1
            else: 
                if cnt > 1:
                    arr += str(cnt)+prev
                else: 
                    arr+=prev
                prev=cur
                cnt=1
        if cnt > 1:
            arr += str(cnt)+prev
        else: 
            arr+=prev
        
        min_length=min(min_length, len(arr))
    return min_length