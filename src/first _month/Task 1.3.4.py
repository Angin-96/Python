from task_1_3_1 import gcd_2
#1.Write a Python function, which Implements the Euler function.
#Euler function is return a count of numbers not great than N, which are mutually simple with N.
#Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function which returns a count of numbers mutually simple with given N.
def euler_function(n):
    d=[]
    for i in range(1,n):
        if gcd_2(i,n)==1:
            d.append(i)
    return len(d)

#2.Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#Given a ticket number n, determine if it's lucky or not.
#For n = 1230, the output should be
#isLucky(n) = true;
#For n = 239017, the output should be
#isLucky(n) = false.
def lucky_ticket(n):
    f=str(n)
    if len(f)%2==0:
        c=[]
        for i in range(len(f)):
            c.append(int(f[i]))
        s=len(c)//2
        return sum(c[:s])==sum(c[s:])
    return False


#3.The robot is standing on a rectangular grid and is currently located at the point (X0, Y0). The coordinates are integers.
# It receives N remote commands(list with n elements each of them is a command). Each command is one of : up, down, left, right.
# Upon receiving a correct command, the robot moves one unit in the given direction. If the robot receives an incorrect command,
# it simply ignores it. Where will the robot be located after following all the commands?
def robot(a,b,*args):
    x=a
    y=b
    for i in args:
        if i=='up':
            y+=1
        if i=='down':
            y-=1
        if i=='left':
            x-=1
        if i=='right':
            x+=1
    return x,y


#4.Write a python function, which returns the sum of digits of given number N.
def sum_of_digits(n):
    d=str(n)
    c=[]
    for i in d:
        c.append(int(i))
    return sum(c)


#5.Write a python program to find the next smallest palindrome of a specified number. For example, for 119 next palindrome is 121.
def smallest_palindrome(n):
    a=str(n)
    while True:
        if a[::-1]==a:
            return a
        a=int(a)+1
        a=str(a)
















