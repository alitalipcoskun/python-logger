# Purpose of this File
It is created to take notes while doing research about `static, class and instance methods`. It contains definition of these methods with examples that are obtained by `Gemini`. The comment lines, that are located at the code snippets, are written by me.



## Instance methods
It implicitly `receives the instance of the class` as their first argument which is named as `self`. This allows them to access and modify the attributes of the instances.

- They are able to access and modify instance based attributes.

- They are called on an instance of the class.


```python
class MyClass:
    def __init__(self, value):
        self.value = value

    # The function accesses to an instance based attribute of an instance. It is dependent to the attribute of instance, thus it is instance method.
    def instance_method(self):
        return self.value * 2

instance = MyClass(10)
result = instance.instance_method() 
```

## Class methods
They are bounded to the class itself, not to an instance. They receive the class as their first argument, conventionally it is named as `cls`.

- They can access and modify  class-level attributes. They cannot directly access instance-specific attributes, unless they create an instance with the defined class method.

### Use cases
- Factory methods: creating instances of the class with different ways.

- Modifying class-level state: changing attributes that apply to all instances.

- Alternative constructor: providing different ways to initialize the class

```python
class MyClass:
    class_attribute = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        cls.class_attribute = 10  # Modify class-level attribute
        return cls.class_attribute

    @classmethod
    def from_string(cls, s):  # Factory method
        value = int(s)
        return cls(value)  # Create and return an instance

result = MyClass.class_method()  # result will be 10
instance2 = MyClass.from_string("25")  # Creates an instance with value 25
```

## Static methods
These methods are not bound to the class or the instance. They are functions that are part of the namespace of the class. They do not receive any implicit first argument `(self, cls)`.

- They do not have access to the class or the instance implicitly.

# Use cases
- Utility functions are very popular for static methods. They are helper functions that are related to the class, but the access to the data of the class is not needed.

- Grouping functions: Organizing functions that are logically belong with the class.

```python
class MyClass:
    @staticmethod
    def static_method(x, y):  # No implicit argument
        return x + y


# Static methods are called with the class name.
result = MyClass.static_method(5, 3)  # result will be 8
```
# Instance Methods vs. Class Methods vs. Static Methods

| Feature        | Instance Method | Class Method    | Static Method   |
|----------------|-----------------|-----------------|-----------------|
| Binding        | Instance        | Class           | None            |
| First Argument | `self`          | `cls`           | None            |
| Access         | Instance data   | Class data      | None (data passed as arguments) |
| Calling        | `instance.method()` | `MyClass.method()` or `instance.method()` | `MyClass.method()` |
| Use Cases      | Operations on instance data | Factory methods, class-level operations | Utility functions, grouping related functions |

## When to Use Which

*   **Instance Methods:** Use when the method needs to work with the data of a specific instance. This is the most common type of method.

*   **Class Methods:** Use when the method needs to work with class-level data or when you want to create instances of the class in different ways (factory methods).  Commonly used for alternative constructors.

*   **Static Methods:** Use when you have a utility function that is related to the class but doesn't need access to its data.  They are often used for organizing related functions within the class namespace.  They are essentially regular functions that happen to be part of the class.

## Example: Pizza Class
Created by Gemini.
```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def describe(self):  # Instance Method
        return f"A {self.size} pizza with {', '.join(self.toppings)}"

    @classmethod
    def from_string(cls, pizza_string):  # Class Method (Factory)
        size, toppings_str = pizza_string.split(":")
        toppings = toppings_str.split(",")
        return cls(size, toppings)

    @staticmethod
    def validate_topping(topping):  # Static Method (Utility)
        valid_toppings = ["pepperoni", "mushrooms", "onions", "olives"]
        return topping in valid_toppings

my_pizza = Pizza("large", ["pepperoni", "mushrooms"])
print(my_pizza.describe())  # Output: A large pizza with pepperoni, mushrooms

pizza_str = "medium:onions,olives"
another_pizza = Pizza.from_string(pizza_str)
print(another_pizza.describe()) # Output: A medium pizza with onions, olives

print(Pizza.validate_topping("anchovies"))  # Output: False

