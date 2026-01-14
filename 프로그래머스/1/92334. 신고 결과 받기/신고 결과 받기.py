from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    #유저한 신고한 id 딕셔너리를 만들고 muzi:frodo,neo 
    #report에서 몇 번 신고당햇는지 딕셔너리를 만든다. value가 k 이상이면, 
    #1번 딕셔너리 value 값에 위 value가 있으면 answer[순서]+=1
    
    report_dic=defaultdict(set)
    singo_dangham=defaultdict(set)
    for r in report:
        a,b=r.split()
        report_dic[a].add(b)
        singo_dangham[b].add(a)
    
    for key,val in singo_dangham.items():
        if len(val) >= k:            
            for k2,v2 in report_dic.items():                
                if key in v2: 
                    idx=id_list.index(k2)            
                    answer[idx]+=1
            
    return answer