col1,row1,col2,row2=map(int,input().split())
if 1<=col1<=8 and 1<=row1<=8 and 1<=col2<=8 and 1<=row2<=8:
    if abs(col1-col2)==abs(row1-row2):
        print("yes")
    else:
        print("no")
else:
    print("Input error")