n=int(input())
first=input()
ans=0
for _ in range(n-1):
    word=input()

    cnt=0
    first_count=[0]*26
    word_count=[0]*26

    for c in first:
        first_count[ord(c)-65]+=1
    for c in word:
        word_count[ord(c)-65]+=1
    for i in range(26):
        cnt+= abs(first_count[i]-word_count[i])
    if cnt <= 2 and abs(len(first)-len(word)) <=1:
        ans+=1
print(ans)