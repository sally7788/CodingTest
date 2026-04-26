def sosu(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    number=""
    while n: 
        number=str(n%k)+number
        n=n//k
    
    split_number=number.split("0")
    print(split_number)
    for num in split_number:
        if num != "" and sosu(int(num)):
            answer+=1
        
    return answer