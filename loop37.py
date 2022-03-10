
a=input('enter a number')
b='0'
i=0
while i<len(a):
    if b in a and  a not in b:
        print('Duck number')
        break
    else:
        print('not Duck number')
        break
    i=i+1