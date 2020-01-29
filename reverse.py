s=int(input())
v=0
rev=0
while s>0:
    v=s%10
    rev=rev*10+v
    s=s//10
print(rev)
