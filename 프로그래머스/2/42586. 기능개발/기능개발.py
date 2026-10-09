def solution(progresses, speeds):
    answer = []
    
    spans = []
    for i in range(len(speeds)):
        if (100-progresses[i]) % speeds[i] == 0:
            span=(100-progresses[i]) // speeds[i]
        else: span = (100-progresses[i]) // speeds[i] +1
        
        if not spans:
            spans.append(span)
        
        elif span <= spans[0]:
            spans.append(span)
            
        else: 
            answer.append(len(spans))
            spans=[span]
    
    answer.append(len(spans))
        
    return answer