n= int(input())
for i in range(20000):
    if n <= 3*i**2+3*i+1:
        print(i+1)
        break 