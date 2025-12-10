a,b,c,d,e,f=map(int, input().split())
x,y=0,0
dff=a*e-b*d

x=(c*e-b*f)/dff
y=(a*f-c*d)/dff
print(int(x),int(y))