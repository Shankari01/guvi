def pattern():
    n=int(input("enter the range:"))
    for i in range(1,n+1):
        for j in range(1,n):
            print(" ",end=" ")
        for k in range(1,i):
            print(k,end=' ')
        for l in range(i,0,-1):
            print(l,end=" ")
        print()
pattern()
