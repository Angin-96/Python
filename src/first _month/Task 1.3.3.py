#1.Write a Python function which returns factorial value of given number n.
def fact_value(n):
    if n==1:
        return n
    return n*fact_value(n-1)


#2.Write a Python function which returns the n-th element of the fibonacci series.
def fibo_ser(n):
    if n<0:
        print("The number must be positive")
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibo_ser(n-1)+fibo_ser(n-2)
