def fib(n):
    a=0
    b=1
    while a < n:
        print(a, end=" ")
        temp = a+b
        a=b
        b=temp
    print()

