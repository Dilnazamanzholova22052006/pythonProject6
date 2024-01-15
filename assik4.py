a1,b1,a2,b2=map(int,input().split())
if b1<a2 or b2<a1:
    print("empty set")
else:
    start=max(a1,a2)
    end=min(b1,b2)
    if start==end:
        print(start)
    else:
        print(start,end)