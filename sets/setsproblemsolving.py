# find max value
a={12,45,67,89,90}
maximum=max(a)
minimum=min(a)
print("maximum is",maximum)
print("minimum is",minimum)

# find common elements in three lists using sets
a=[1,4,5,6]
b=[6,8,9,4]
c=[4,5,6,4]
print(set(a) & set(b) & set(c))
print(type(a))

# difference between two sets
a={1,4,5,6}
b={6,8,9,4}
print(a-b)
print(a.difference(b))

# check if a set is a subset of another set
a={1,4,5,6}
b={4,5,6}
print(b.issubset(a))
