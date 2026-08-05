# get function
Student_data={"name":"David","age":13,"marks":87}
x=Student_data.get("marks")
print(x)

# item-keys value can be obtain in tuple format
a=Student_data.items()
print(a)

# keys
b=Student_data.keys()
print(b)

# values
c=Student_data.values()
print(c)

# copy
d=Student_data.copy()
print(d)

# setdefault
Student_data={"name":"David","age":13,"marks":87}
Student_data.setdefault("grade","A")
print(Student_data)

# update
student = {"name": "Sita", "age": 18}
student.update({"city": "Pokhara", "age": 19})
print(student)

# pop
student = {"name": "Hari", "age": 21, "city": "Kathmandu"}
removed_value = student.pop("city")
print(removed_value)
print(student)

# popitem()-removes last key-value
student = {"name": "Gita", "age": 20, "grade": "B"}
removed_pair = student.popitem()
print(removed_pair)
print(student)

# clear
student = {"name": "Ravi", "age": 22}
student.clear()
print(student)

name = "Python"
for item in name:
    print(item)

print("Welcome to number guessing game.")
right_number=3
print("I've picked a number for you to guess.")
print("The number is betwen 1 and 5")
guessed_number=int(input("enter a number"))








