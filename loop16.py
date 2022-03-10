a=int(input("enter a number"))
i=1
while i<=a:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    i+=1
if c==2:
    print(a,"prime number")
else:
    print(a,"not prime no")