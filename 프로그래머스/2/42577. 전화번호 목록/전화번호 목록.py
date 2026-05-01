def solution(phone_book):
    answer = True
    hash_map={}
    for num in phone_book: #해시맵으로 미리 그려놓는거야.. 
        hash_map[num]=1
    
    for num in phone_book:
        arr=""
        for n in num:
            arr+=n
            if arr in hash_map and arr != num:
                return False
    return answer