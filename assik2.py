num=int(input())
if 0<=num<=36:
    if num==0:
        print("green")
    elif 1<=num<=10 or 19<= num<=28:
        print("Red" if num %2==1 else "black")
    elif 11<=num<=18 or 29<= num<=36:
        print("black" if num%2==1 else "red")
else:
    print("input error")