

#pascale triangle

from math import factorial

n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//factorial(j)//factorial(i-j), end=" ")
    print()




#factorial function prob
print("-" * 40)
a=int(input("enter any number"))    #40585
g=a
fact=1
sum=0
while(a>0):
    r=a%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    a=a//10
if(sum==g):
    print("satisfy number")
else:
    print("not")

print("-"*40)

#fibonacci series
print("-" * 40)
n=7
a=0
b=1
sum=0
count=1
print("fibonacci series",end=" ")
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b



#pattren problem
print("-" * 40)
n=4
num=1
for i in range(0,n):
    for j in range(0, i+1):
        print(num, end="")
        num+=1
    print("")



n=6
for n in range(n):
    for i in range(n):
        print(n, end="")
    print("")

#greety problem
count=0
for i in range(1,501):
    if i%3==1:
        a=2*((i-1)//3)
        if a%3==1:
            b=2 * ((a - 1) // 3)
            if b%3==1:
                c=2*((b-1)//3)
                if c%3==0:
                    print(i,end=',')
                    count+=1
                    if count==5:
                        break


