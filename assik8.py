m,n=map(int,input().split())
if m<n:
    for i in range(m,n+1):
        print(i)
else:
    for i in range(m,n-1,-1):
        print(i)