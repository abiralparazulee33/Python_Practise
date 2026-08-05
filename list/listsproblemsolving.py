# swap the elements in list
A=["gg","ff","ll","kk","hh"]

A[0],A[3]=A[3],A[0]
print(A)

B=[13,7,12,10]
# multiply all numbers in list
mul=1
for i in B:
    mul*=i
print(mul)

# get largest and  from the list
B.sort()
print(B)
print("largest is",B[-1])
print("smallest is",B[0])

