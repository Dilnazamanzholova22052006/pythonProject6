a=1
while a<=10:
    square=a**2
    if square%3==0:
        a+=1
        continue
    print(square)
    a+=1