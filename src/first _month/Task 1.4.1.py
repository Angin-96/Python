# 1.Write a python program which returns a given list without duplicates.
def list_without_dublicate(lst: list):
    return list(set(lst))


# 2.Write a python program which returns common elements of 2 lists.
def common_elements(set1, set2):
    return set1 & set2


# 3.Write a python program which return elements which are in first list but not in second
def in_first_but_not_in_second(f1,f2):
    return f1-f2


# 4.Write a python program which return elements are or in first list, either in second, but not in both
def elements_not_in_both(g1,g2):
    return g1^g2


# 5.Write a python program which return elements which are or in first, either in second, or in both
def elements_in_both(f1,f2):
    return f1|f2



# 6.Write  python function which get set and element value, and remove from set element with given value if exist
def remove_given_value_in_set(am, n):
    am = set(am)
    am.remove(n)
    return am

# 7.Write a python python program, which return list from given set, where each element of list, is equal to cub of set element
def cube(set):
    d=[]
    for i in set:
        d.append(i**3)
    return d