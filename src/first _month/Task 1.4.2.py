# 1.Write a python program, which adds a new value with the given key in dict.
def new_value(dict, key, value):
    dict[key] = value
    return dict


# 2.Write a python program which concat 2 dicts.
def concat_dict(a, b):
    a.update(b)
    return a


# 3.Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers
def cubs(n):
    cubs = {}
    for x in range(1, n + 1):
        cubs[x] = x ** 3
    return cubs


# 4.Write a python program which create dict from 2 lists with the same length
def dict_from_2_lists(a, b):
    d = {}
    if len(a) == len(b):
        for x in range(len(a)):
            d[a[x]] = b[x]
        return d
    print("Error- The first list's length must be the same as the second")


# 5.Write a python program which gets the maximum and minimum values of a dictionary.
def min_and_max_values(a):
    b = list(a.values())
    b.sort()
    return b[0], b[-1]


# 6.Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.
def comb_2_dicts(a, b):
    for x, y in b.items():
        if x in a.keys():
            y = y + a[x]
            a[x] = y
        a[x] = y
    return a


# 7.Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string
def dict_from_string(a):
    d = list(a)
    f = {}
    for x in d:
        f[x] = d.count(x)
    return f
