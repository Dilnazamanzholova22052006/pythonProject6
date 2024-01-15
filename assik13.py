number=input()
result="YES"if number==''.join(sorted(number,reverse=True)) else "NO"
print(result)