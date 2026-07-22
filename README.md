## Introduction to Object-Oriented Programming:

Object-Oriented Programming (OOP) is a way of organizing your code that focuses on creating reusable structures called objects.

## What is a Class?
*A class is a blueprint or template that defines the structure and behavior of objects.*  Understanding classes is fundamental to OOP.
When you create a class, you're essentially designing a new type of data structure. Python comes with built-in data types like integers (int), `strings (str)`, `lists (list)`, and `dictionaries (dict)`.

`Every class definition includes two main components:`

`Attributes` are the data that objects created from the class will store. These are like variables, but they belong to the object.

*Example:* For a User class, `attributes might include` name, email, age, and registration_date

`Methods` are functions that belong to the class and define what actions objects can perform.

class User:  `declares that we're creating a new class called User.` 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.is_active = True  # Default value for all users
    
The __init__ method is a special method called a constructor. It runs 

**Self**: automatically whenever you create a new object from the class.
When you define methods inside a class, the first parameter is always self. This parameter is a reference to the specific object instance that the method is being called on. In other words, self is how a method knows which object's data to work with.

Metaphot 
Class → the blueprint for one type of room
Objects → different rooms created from that blueprint
Attributes → items or information inside each room
Methods (def) → actions that can be performed in the room

For example:

### Encapsulation and Data Protection
Encapsulation is one of the four fundamental principles of Object-Oriented Programming. The term means "enclosing" or "wrapping" data and the methods that work on that data together within a single unit — the class. However, encapsulation goes beyond just bundling things together. It also involves controlling access to an object's data.