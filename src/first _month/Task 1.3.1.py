#1.Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.
def divider(a,b):
    if b%a==0:
        return True
    else:
        return False

#2.Write a Python function, which gets a number, and return True if that number is palindrome, otherwise False.
def palindrome(a):
    a=str(a)
    if a[::-1]==a:
        return True
    else:
        return False

#3.Write a Python function, which gets a number, and return True if that number is prime, otherwise False.
def prime(a):
    if a<=1:
        return False
    for i in range(2,a):
        if a%i:
            return True
        else:
            return False

#4.Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.
def perfect(a):
    s=[]
    if a<=1:
        return False
    for i in range(1,a):
        if a%i==0:
            s.append(i)
    if sum(s)==a:
        return True
    else:
        return False

#5.Write a function, which gets 2 numbers, and return their Great common divisor.
def gcd(a,b):
    s=[]
    if a>=0 or b>=0:
        if a>b:
            for i in range(1,a):
                if a%i==0 and b%i==0:
                    s.append(i)
        if b>a:
            for i in range(1,b):
                if b%i==0 and a%i==0:
                    s.append(i)
        if a==b:
            s.append(a)
        return max(s)
    else:
        print("Your number must be positive")

















