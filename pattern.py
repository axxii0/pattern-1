for i in range (5,0,-1):
    for j in  range(i):
        print("*",end="")
    print()



for i in range (1,6):
    for j in  range(i):
        print("*",end="")
    print()



for i in range (5):
    for j in range(5-i):
        print(" ",end='')
    for k in range(i):
        print(k+1,end='')
    for l in range(i-1):
        print(i+l+1,end='')
    print()




    n = int (input ("Enter the number of  Terms: " ) )
    a=0
    b=1
    for i in range (n):
        print(a, end=" ")
        c=a+b
        a=b
        b=c




number=int(input("Enter the number of terms: "))        
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
    if count==2:
        print(number,"is a prime number")    
    else:    
        print(number,"is not a prime number")




































