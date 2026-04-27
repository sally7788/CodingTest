def solution(files):
    answer = []
    # 1. 반복문을 써서 head, number, tail을 구분한다. 리스트에 넣는다 이중리스트  
    #     1-1. number은 int로 넣는다.
    # 2. head를 다 소문자로 바꾼다 
    # 3. 문자열 sort 진행 
    # 4. 문자열이 같은 경우, 숫자순으로 나열
    parse=[]
    for file in files:
        head, number, tail="","",""
        i=0
        while i < len(file) and not file[i].isdigit():
            head+=file[i]
            i+=1
        
        while i < len(file) and file[i].isdigit():
            number+=file[i]
            i+=1
        tail=file[i:]
        
        parse.append([head.lower(), int(number), tail, file])
    parse=sorted(parse, key=lambda x: (x[0], x[1]))
    
    for f in parse:        
        answer.append(f[3])
    
    
            
    
    return answer

    