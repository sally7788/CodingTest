def solution(record):
    answer = []
    '''
    id:닉네임 변천사 value값으로 적용. 그냥 마지막 value만 저장하면 되잖아
    enter {dic[id]} 들어왓습니다 
    '''
    change_nickname={}
    for r in record:
        if r[:r.index(" ")]!="Leave":
            _, uid,nickname=r.split()       
            change_nickname[uid]=nickname
     
    for r in record:
        res=""
        if r[:r.index(" ")]=="Enter":
            behavior, uid, nickname=r.split()         
            res=f"{change_nickname[uid]}님이 들어왔습니다."
                
        elif r[:r.index(" ")]=="Leave":
            behavior, uid=r.split()
            res=f"{change_nickname[uid]}님이 나갔습니다."
        if res != "":
            answer.append(res)
        
    return answer

