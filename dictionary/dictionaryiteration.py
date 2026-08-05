# Employee_Data={"name":"John","age":13,"gender":"male"}
# # printing key names one by one
# for x in Employee_Data:
#     print(x)

# # printing values one by one
# for x in Employee_Data:
#     print(Employee_Data[x])

# # using value function
# for x in Employee_Data.values():
#     print(x)

# # getting both at once
# for x,y in Employee_Data.items():
#     print(x,":",y)

a=[2,3,2,3,2]
b=set(a)
print(b)
c=list(b)
print(c)
count=0
counts=0
for i in a:
    if i==c[0]:
        count=count+1
print(count)
for j in a:
    if j==c[1]:
        counts=counts+1
print(counts)
if set([count,counts])=={2,3}:
    print("full house")
else:
    print("not full house")    



    




    