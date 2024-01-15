n=int(input())
numbers=(int(input())for i in range(n))
larg,sec_larg=sorted(numbers)[-2:]
print(larg)
print(sec_larg)