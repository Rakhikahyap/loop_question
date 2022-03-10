a=int(input("enter a number"))
i=1
l=''
while i<=1000:
    if i%2==0:
        l+=str(i)
    i=i+1
j=0
while j<=a:
    print(l[j])
    j+=1