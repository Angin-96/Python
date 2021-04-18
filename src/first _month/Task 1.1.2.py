# Task 1.1.2
# Strings
# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
c='asdfghjk'
s=c[:2]+c[-2:]
print("s=", s)



# 2. Write a Python program to remove the n-th index character from a nonempty string.
d='qwertrir'
n=4
c=d[0:n]+d[n+1:]
print(c)



# 3. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
f='asdfg'
l=f[-1]+f[1:-1]+f[0]
print("l=", l)



# 4. Write a Python function to get a string made of 4 copies of the last two characters of a specified string.
df='123654'
gh=df[-2:]*4
print("gh=", gh)




# Lists
# 1. Write a Python program that make a list from given string.
bravo='bravocharlie'
foxtrot=list(bravo)
print(foxtrot)




# 2. Write a Python program to print a new list which is the equivalent given list after removing the 0th, 4th and 5th elements.
sierra=['tango', ['yanki',565], 'rojer', 5456, 'hd', '68687',69,'nhfds']
echo=sierra[1:4]+sierra[6:]
print(echo)




# 3. Write a Python program which add an element to the given list.
alfa=[1,2,3,'gh',5]
alfa=alfa+['h',122,'havana']
print("alfa=", alfa)




# 4. Write a Python program which concat 2 lists.
cyber=[1,2,3, 'crazy']
security=['hak',122,'hj',['jjkf',155]]
protection=cyber+security
print("protection=",protection)


