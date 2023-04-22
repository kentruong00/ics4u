# Object oriented programming note #1

### What is an Object?

In computer science, objects are locations in memory with with a value, referenced by an identifier. In OOP, objects are instances of classes that can exist as variables, functions, data structures or a combination of all of these things. 
- Combination of data and functional code
- Objects in real life have data and also behavior, so do objects in coding\
- Instance of a class
- Data is called attributes
- Code is called methods

### What is OOP

- Goal is to create modular reusable software
- Design programs with objects
- Focuses on definition of data rather than procedural programming 

### What is a class?
- A blank slate for an object to be instantiated from
- Contains fields, variables that store information about the object
- Contains methods, functions that belong to the object 
- fields and methods are both attributes

```python
# example of a class definition in python:
class Person():
    def __init__(self, name):
    self.name = name
    
    def __str__():
    return f'Person objected named {self.name}'
```
- ```class``` is a keyword in python to create a class
- ```__init__``` is a base override
- Class names are capitalized

### Encapsulation
- Hiding information so that only the class can access it
- Used for data protection
- Restricting certain methods from being called
- In python attributes are hidden by using a double underscore

### Inheritance
- child class created from a parent class, has the same attributes and methods, but can be changed into their own class
- child class can override attributes and methods
```python
class ParentClassName:
	“”” Define Parent Class “””
	.
	.
	.

class InheritanceClass(ParentClassName):
	“”” Define Inherited Class “””

	def __init__(self, param, param2):
		ParentClassName.__init__(self, param)
		self.param2 = param2
```
