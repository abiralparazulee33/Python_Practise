class Animal:
    def eat(self):
        print("I can eat")


# the Dog class is derived from Animal        
class Dog(Animal):
    def bark(self):
        print("I can bark")



# base class
class Animal:
    def eat(self):
        print("I can eat")

# the Dog class is derived from Animal
# notice Animal inside ()        
class Dog(Animal):
    def bark(self):
        print("I can bark")

# object of the dog class
dog1 = Dog()

# call the bark() method (of Dog)
dog1.bark()

# call the eat() method (of Animal)
dog1.eat()



class Animal:
    def eat(self):
        print("I can eat")

# derive Dog from Animal      
class Dog(Animal):
    def bark(self):
        print("I can bark")

# derive Cat from Animal
class Cat(Animal):
    def get_grumpy(self):
        print("I am getting grumpy.")

# object of Dog
dog1 = Dog()

dog1.bark()
dog1.eat()

# object of Cat
cat1 = Cat()
cat1.eat()




class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges.")

        # call the display_info() method of Polygon
        super().display_info()

# create an object of Triangle
t1 = Triangle([5, 6, 7])

# call get_perimeter using t1
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

# call display_info() using t1
t1.display_info()



# Replace ___ with your code

# create the Person class
class Person:
    def __init__(self):
        person_name = input('Enter name: ')
        person_age = int(input('Enter age: '))
        self.name = person_name
        self.age = person_age
    
    def display_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')

# derive the Student class from Person
class Student(Person):
    # create the __init__() method
    def __init__(self, student_id):
        # create id attribute and assign student_id to it
        self.id=student_id
        
        # call the __init__ method of Person using super()
        super().__init__()

    # create the display_info() method
    def display_info(self):
        # call display_info() of Person using super()
        super().display_info()
        # print the id attribute
        print(f'id: {self.id}')

# create an object of Student with 12 as argument
s1=Student(12)
s1.display_info()

# call display_info() using the object




# In this example, we will add two distances (in feet-inch) using object-oriented programming.
# If you don't know,
# 1 feet = 12 inches

class Distance:
    # initialize feet and inches attributes
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def add_distances(self, distance):
        result_inches = self.inches + distance.inches
        result_feet = self.feet + distance.feet
        
        # while inch is 12 or greater,
        # increase feet by 1 and decrease inches by 12
        while (result_inches >= 12):
            result_feet = result_feet + 1
            result_inches = result_inches - 12 
            
        # create an object of Distance
        result_distance = Distance(result_feet, result_inches)
        return result_distance
        
# create distance1 object
distance1 = Distance(12, 8)

# create distance2 object
distance2 = Distance(10, 6)

# call add_distances using distance1 object
# distance2 is used as argument
result = distance1.add_distances(distance2)
print(f'Result distance: {result.feet} ft {result.inches} inches')






# Replace ___ with your code

# create the Animal class
class Animal:
    def eat(self):
        print("I can eat food")

# create the Dog class
class Dog(Animal):
    def bark(self):
        print("I can bark")
        super().eat()
# super is used to call the method from the parent class inside a child class.
# create an object of the Dog class
dog1=Dog()

# call the eat() method using the object
dog1.eat()