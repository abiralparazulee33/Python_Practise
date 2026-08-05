l1=[30,40,50,60]
l2=[]
for i in l1:
    if i>45:
        l2.append(i)
print(l2)

# to copy one list into another use comprehension method
l3=[i for i in l1]
print(l3)

l3=[i for i in l1 if i>45]
print(l3)




# Replace ___ with your code

numbers = [12, 17, 28, 19, 11]

# Use list comprehension to get only odd numbers from the numbers list
numbers1=[i for i in numbers if i%2!=0]

# print new list
print(numbers1)





# Replace ___ with your code

# get integer input for variable n
n = int(input())

# create the list using list comprehension
numbers = [i for i in range(1,n+1) ]

# # print the list
print(numbers)






# Replace ___ with your code

numbers = [1, 2, 3, 4]

# create the dictionary using comprehension
numbers1={i:i+1 for i in numbers }


# print the dictionary
print(numbers1)

