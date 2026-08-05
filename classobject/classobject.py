class Student:

    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student()
student1.name = 'Harry'
student1.score = 85

# calling this method using student1 object
did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)

# create object
student2 = Student()
student2.name = 'Ronin'
student2.score = 35

# calling this method using student2 object
did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass?', did_pass)




# init 
class Student:

    # adding the __init__() method
    def __init__(self, name, score):
       self.name = name
       self.score = score

    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student('Harry', 85)

# calling this method using student1
did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)

class Test:
    def __init__(self, attr1, attr2):
        self.attribute_name1 = attr1
        self.attribute_name2 = attr2

# create an object
test1 = Test(10, 20)
print(test1.attribute_name1)   # 10
print(test1.attribute_name2)   # 20

# create an object
test2 = Test(100, 200)
print(test2.attribute_name1)   # 100
print(test2.attribute_name2)   # 200




# real and imaginary problem
class Complex:
    # using __init__() to create attributes
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

    # method to add complex numbers
    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary
        
        # create another object of Complex
        result = Complex(result_real, result_imaginary)  
        return result

n1 = Complex(5, 6)
n2 = Complex(-4, 2)

# The return value from the add() method
# is assigned to the n3 variable
n3 = n1.add(n2)

# printing n3 attributes
print('real part =', n3.real)
print('imaginary part =', n3.imaginary)




# creating the Test class
class Test:

   def __init__(self, a):
       self.attr1 = a

   def call_me(self):
       # creating a new object
       t2 = Test(1000)
       return t2

# object t1 of the Test class
t1 = Test(1)

result = t1.call_me()
print(result.attr1)   # 1000





# Replace ___ with your code

# create the class
class Bicycle:
    def __init__(self, gear, speed):
        # initialize attributes
        self.gear=gear
        self.speed=speed
    
    # create the print_attributes() method 
    def print_attributes(self):
        print(self.gear)
        print(self.speed)

# create the object with 4 and 80 as arguments
bicycle1 = Bicycle(4,80)

# call print_attributes() using bicycle1
bicycle1.print_attributes()









# Replace ___ with your code

# create the Coordinate class
class Coordinate:

    # initialize x and y attributes inside __init__()
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # define the add_coordinates() method
    def add_coordinates(self, other):
        new_x=self.x+other.x
        new_y=self.y+other.y
        # create and return a new Coordinate object
        return Coordinate(new_x, new_y)


# create objects c1 and c2
c1 = Coordinate(5,6)
c2 = Coordinate(7,9)

# call the add_coordinates() method
c3 = c1.add_coordinates(c2)

# print attributes of the c3 object
print(c3.x)
print(c3.y)












# Replace ___ with your code

# create the Triangle class
class Triangle:
    # define the __init__() method
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


    # define the get_perimeter() method
    def get_perimeter(self):
        return self.x+self.y+self.z
        
# take three integer inputs
a = int(input())
b = int(input())
c = int(input())

# create an object of the Triangle class
triangle=Triangle(a,b,c)

# call the get_perimeter() method
# perimeter = triangle.get_perimeter()

# print the perimeter
print(triangle.get_perimeter())







# Replace ___ with your code

# create the Student class
class Student:

    # use the __init__() method to initialize the scores attribute  
    def __init__(self,scores):
        self.scores=scores
  
    # create the get_scores_sum() method that returns the sum of scores items
    def get_scores_sum(self):
        return sum(self.scores)
  
  
# create the scores variable
scores = [55, 75, 80, 62, 77]

# create an object of Student by passing scores as an argument
s1 = Student(scores)

# call the get_scores_sum() method using the s1 object
total = s1.get_scores_sum()

# print total
print(total)








# Replace ___ with your code

# create the Engine class
class Engine:
    # use __init__() to initialize the power attribute 
    def __init__(self,power):
        self.power=power

# create the Vehicle class
class Vehicle:
    # use __init__() to initialize the wheels attribute
 
    def __init__(self, wheels):
        self.wheels = wheels
        
        # the engine attribute should be an object of the Engine class with the power attribute 400
        self.engine = Engine(400)
    
    # create the get_power() method
    def get_power(self):
        # print the power attribute of the engine attribute (which is an object of Engine) 
        print(self.engine.power)

# create an object of Vehicle
vehicle1=Vehicle(4)

# call the get_power() method using the object
vehicle1.get_power()