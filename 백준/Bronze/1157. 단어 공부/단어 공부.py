from collections import Counter
w=input().upper()
word=Counter(w).most_common()

if len(word)>=2 and word[0][1]==word[1][1]:
    print("?")
else:print(word[0][0])