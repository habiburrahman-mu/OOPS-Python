# OOPS-Python
Object Oriented Programming using Python

### Classes and Objects
- [car.py](car.py)
- [rectangle.py](rectangle.py)


- - -


### Constructor [`__init__()`]
- [car_init.py](car_init.py)
- [rectangle_init.py](rectangle_init.py)

- - -

### Encapsulation
*In object-oriented programming (OOP, encapsulation refers to the bundling of data with the methods that operate on that data, or the restricting of direct access to some of an object's components. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing direct access to them by clients in a way that could expose hidden implementation details or violate state invariance maintained by the methods.*

- [car_encapsulation.py](car_encapsulation.py)
- [rectangle_encapsulation.py](rectangle_encapsulation.py)

#### Private Method

*Private methods are those methods which can't be accessed in other class except the class in which they are declared. We can perform the functionality only within the class in which they are declared.*

*Private methods are useful for breaking tasks up into smaller parts, or for preventing duplication of code which is needed often by other methods in a class, but should not be called outside of that class.*

- [hello.py](hello.py)

- - -
### Inheritance

*It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.*

*Inheritance is a mechanism in which one class acquires the property of another class. For example, a child inherits the traits of his/her parents. With inheritance, we can reuse the fields and methods of the existing class. Hence, inheritance facilitates Reusability and is an important concept of OOPs.*

- [polygon.py](polygon.py)

#### Multiple inheritance

- [human.py](human.py)


- - -

### `super()` function

*The `super()` function is used to give access to methods and properties of a parent or sibling class. The `super()` function returns an object that represents the parent class. It allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.*

- [super_parent_child.py](super_parent_child.py)

- - -
### Composition

*Composition is one of the fundamental concepts in object-oriented programming. It describes a class that references one or more objects of other classes in instance variables. This allows you to model a has-a association between objects. The main reason to use composition is that it allows you to reuse code without modeling an is-a association as you do by using inheritance. That allows stronger encapsulation and makes your code easier to maintain*

- [salary_composition.py](salary_composition.py)

- - -
### Aggregation

*Aggregation is a special form of association. It is a relationship between two classes like association, however its a directional association, which means it is strictly a one way association. It represents a HAS-A relationship.*

- [salary_aggregation.py](salary_aggregation.py)

- - - 

### Abstract Class and Method

*Abstraction is the concept of object-oriented programming that "shows" only essential attributes and "hides" unnecessary information. The main purpose of abstraction is hiding the unnecessary details from the users. Abstraction is selecting data from a larger pool to show only relevant details of the object to the user. It helps in reducing programming complexity and efforts. It is one of the most important concepts of OOPs.
*

*Abstract Class is a type of class in OOPs, that declare one or more abstract methods. These classes can have abstract methods as well as concrete methods. A normal class cannot have abstract methods. An abstract class is a class that contains at least one abstract method.
*

*Abstract Method is a method that has just the method definition but does not contain implementation. A method without a body is known as an Abstract Method. It must be declared in an abstract class. The abstract method will never be final because the abstract class must implement all the abstract methods.
*

- [square_abstraction](square_abstraction.py)
- - -