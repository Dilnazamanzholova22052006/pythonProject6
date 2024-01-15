count=0
while True:
    grade=int(input())
    if grade>0 and grade<=5:
        if grade==5:
            count+=1
        else:
            break
print(count)