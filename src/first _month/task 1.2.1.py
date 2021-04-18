#Write a Python program to get the largest number from a list.
s=[1,56,8,96,5,86,23,74,6,8]
s.sort()
print(s[-1])



#Write a Python program to get the frequency of the given element in a list to.
s=[1,2,3,5,5,6,7,8,5]
s.count(5)



#Write a Python program to remove the second element from a given list, if we know that the first elements index with that value is n.
s=[1,2,3,4,1,5,6,1]
a=s.index(1,2)
print(a)
s.pop(a)
print(s)



