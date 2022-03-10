print("welcome toour wonderful gaming house")
print("you have 5 chanse")
i=1
num=1
while i<=5:
    b=int(input("you thought please entre your gesssing number::"))
    if b>num:
        print("your gess high please try")
    elif b<num:
        print("your guess low please try")
    else:
        print("wah aap win ho")
        break
    i=i+1