# add
a={"apple","mango",1,40,2.4}
a.add("Spiderman")
print(a)

# pop
a={"apple","mango",1,40,2.4}
a.pop()
print(a)

# remove
a={"apple","mango",1,40,2.4}
a.remove("apple")
print(a)

# discard
a={"apple","mango",1,40,2.4}
a.discard("mango")
print(a)

# copy
a={"apple","mango",1,40,2.4}
b=a.copy()
print(b)

# isdisjoint
a={"apple","mango",1,40,2.4}
b={"apple","grapes","litchi"}
c={"apple",2.4}
print(a.isdisjoint(b))

# issubset
print(a.issubset(b))

print(c.issubset(a))

# issuperset
print(b.issuperset(a))

print(a.issuperset(c))

# update
a.update(c)
print(a)

# clear
a.clear()
print(a)

# union
a={"apple","mango",1,40,2.4}
b={"apple","grapes","litchi"}
c={"apple",2.4}
print(a.union(c))

# difference
print(a.difference(c))

# diference update
a.difference_update(c)
print(a)

# intersection
print(a.intersection(c))

# intersection_update
a.intersection_update(b)
print(a)

# symmetric difference gives set A and b only eliminates common item
a={"gg","ss","dd"}
c={"ff","cc","dd"}
x=a.symmetric_difference(c)
print(x)

a={"gg","ss","dd"}
c={"ff","cc","dd"}
a.symmetric_difference_update(c)
print(a)






