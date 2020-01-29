n=int(input())
t=1
while(n>0):
    d=n%10
    t*=d
    n=n//10
print(t)
