# See also https://www.tutorialspoint.com/python3/python_classes_objects.htm


class Employee:
    "Common base class for all employees"
    # The variable empCount is a class variable whose value is shared among all the
    # instances of a in this class. This can be accessed as Employee.empCount from
    # inside the class or outside the class.
    empCount = 0

    # The first method __init__() is a special method, which is called class
    # constructor or initialization method that Python calls when you create a new
    # instance of this class.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # You declare other class methods like normal functions with the exception that
    # the first argument to each method is self. Python adds the self argument to
    # the list for you; you do not need to include it when you call the methods.
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# Creating Instance Objects
# To create instances of a class, you call the class using class name and pass in
# whatever arguments its __init__ method accepts.
# emp1 = Employee("Zara", 2000)

# Accessing Attributes
# You access the object's attributes using the dot operator with object. Class variable
# would be accessed using class name as follows −
# emp1.displayEmployee()
# print ("Total Employee %d" % Employee.empCount)

# Data Hiding
# An object's attributes may or may not be visible outside the class definition.
# You need to name attributes with a double underscore prefix, and those attributes
# then will not be directly visible to outsiders.

# Overloading Operators
# Suppose you have created a Vector class to represent two-dimensional vectors.
# What happens when you use the plus operator to add them? Most likely Python will yell at you.
# You could, however, define the __add__ method in your class to perform vector addition
# and then the plus operator would behave as per expectation −
#
# For operators, See https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15
# Examples:
# __lt__  <
# __ne__  !=
# __eq__  ==
# __add__ +
# __sub__ -
# __mul__ *
# __turuediv__ /
