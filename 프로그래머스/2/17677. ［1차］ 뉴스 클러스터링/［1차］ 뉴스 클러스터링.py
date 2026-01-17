from collections import Counter
def solution(str1, str2):
    answer = 0
    '''
    
    2. 두글자씩 끊는다. 리스트에 넣는다. 
    2-1.글자에 특수문자, 숫자, 공백이나 있으면 리스트에 안넣는다
    2-2. 다 소문자로 만든다 
    3. 합집합, 교집합을 구한다 | & 
    4. 유사도를 곱하고 65536을 곱한다 
    '''
    l1,l2=[],[]
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            l1.append(str1[i:i+2].lower())
            
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            l2.append(str2[i:i+2].lower())
    
    if not l1 and not l2:
        return 65536
    d1,d2=Counter(l1),Counter(l2)
    hap=d1 | d2
    gyo=d1 & d2
    
    print(hap, gyo)
    answer=int(sum(gyo.values())/sum(hap.values())*65536)
    return answer
    