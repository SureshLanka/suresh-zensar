

#armstrong number

for i in range (1, 500):
    a=str(i)
    b=0
    for j in range(0, len(a)):
        b+=int(a[j])**3
    if i==b:
        print(i, end=" ")

#identity matrix

# identity matrix
print("-" * 40)
n=int(input("enter a number: "))
for i in range (0,n):
    for j in range(0,n):
        if(i==j):
            print("1", sep=" ", end=" ")
        else:
            print("0", sep=" ", end=" ")
    print()


#magic matricx
print("-" * 40)
def generateSquare(n):
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]
    i=n//2
    j=n-1
    num=1
    while num<=(n*n):
        if i ==-1 and j==n:
            j=n-2
            i=0
        else:
            if j== n:
                j=0
            if i<0:
                i=n-1
        if magicSquare[int(i)][int(j)]:
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[int(i)][int(j)]=num
            num=num+1
        j=j+1
        i=i-1
    print("magic Square for n=",n)
    print("sum of each row or column",
          n*(n*n+1)//2,'\n')
    for i in range(0,n):
        for j in range(0,n):
            print('%2d'%(magicSquare[i][j]),
                  end='')
            if j==n-1:
                print()
n= 3
generateSquare(n)