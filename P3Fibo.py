def fib (n):
    if (n < 0):
        print("Negative number is not permissible.")
    else:
        if n <= 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
n = int(input("Enter Upper limit of Fibonacci series: "))
print("-----Fibonacci Series-----")
for i in range(n):
    print (fib(i))
    