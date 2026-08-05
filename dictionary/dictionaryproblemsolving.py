# WAP to sort a dictionary by value
a={"a":12,"b":23,"c":40,"d":50,"e":91}
a=sorted(a.values())
print(a)

# wap script to print a dictionary where the keys are numbers between 1 and 15 and the values
# are square of keys
a={}
for i in range(1,16):
    a[i]=i**2
print(a)

# wap to multiply all the items in dictionary
a={"a":12,"b":23,"c":40,"d":50,"e":91}
mul=1
for i in a:
    mul*=a[i]
print(mul)

# wap to po sort a dictionary by key.
a={12:"a",90:"b",40:"c",17:"d",20:"e"}
a=sorted(a.keys())
print(a)

# keyword arguments
def print_info(**person):
    print(person)

print_info()
print_info(name = 'Steve')
print_info(name = 'Steve', age = 22)

numbers = [1, 2, 3, 4]
# creating an empty dictionary
square_numbers = {}
# using a loop to add items to dictionary
for number in numbers:
    square_numbers[number] = number**2

print(square_numbers)