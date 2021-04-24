#1.Write a Python program to multiply all the items in a list.
l=[1,2,3,4,5,6]
mult=1
for i in l:
    mult=mult*i
print(mult)


#2.Write a Python program to get the largest number from a list.
h=[1,2,56,78,96,87]
for i in h:
    if i==max(h):
        print(i)


#3.Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
l=[]
for i in range(31):
    i**=2
    l.append(i)
print(l[5:])

#4.Write a Python program to remove duplicates from a list.
p=[1,2,3,4,5,6,7,1,1,11]
l=[]
for i in p:
    if i not in l:
        l.append(i)
print(l)
st=list(set(p))


#5. Write a Python program to find the most appeared element in a list.
a=[1,2,3,5,1,1,2,5,1,8,3,3,3,3,3]
c=0
d=0
for i in a:
    s=a.count(i)
    if s>c:
        c=s
        d=i
print(d)




