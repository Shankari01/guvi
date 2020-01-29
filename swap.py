a=[]
n=int(input())
x=0
for i in range(0,n):
    x=int(input())
    a.append(x)
t=a[0]
a[0]=a[n-1]
a[n-1]=t
print (a)
