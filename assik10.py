def task14():
    n = int(input())
    fibbonaci = [1, 1]
    for i in range(n - 2):
        fibbonaci.append(fibbonaci[len(fibbonaci) - 1] + fibbonaci[len(fibbonaci) - 2])
    for number in fibbonaci:
        print(number, end=" ")
