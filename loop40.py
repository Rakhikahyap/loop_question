i=0
sum=0
while i<=10:
    sum=sum+i
    i=i+1
    if sum%2==0:
        print(sum,'even')
    else:
        print(sum,'odd')