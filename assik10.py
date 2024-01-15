n=int(input())
fib=[1,1]
while len(fib)<n:
    next_num=fib[-1]+fib[-2]
    fib.append(next_num)
print(fib[:n])