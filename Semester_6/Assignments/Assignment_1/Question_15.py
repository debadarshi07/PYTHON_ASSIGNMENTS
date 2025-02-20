from collections import namedtuple
from dataclasses import dataclass

PersonNT = namedtuple('PersonNT', ['name', 'age'])
person_nt = PersonNT(name="Alice", age=30)

try:
    person_nt.age = 31
except AttributeError as e:
    print(f"NamedTuple Error: {e}")

@dataclass
class PersonDC:
    name: str
    age: int
    city: str = "Unknown"

person_dc = PersonDC(name="Bob", age=25)

person_dc.age = 26
person_dc.city = "New York"

@dataclass
class PersonWithMethod:
    name: str
    age: int
    city: str

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old from {self.city}."

person_method = PersonWithMethod(name="Charlie", age=22, city="Los Angeles")
print(person_method.greet())

print(f"Data Class Person: {person_dc}")


'''

Advantages of Python Data Classes over Named Tuples :-

Python data classes (introduced in Python 3.7) offer several advantages over namedtuple, making them more flexible and functional:

Mutability:
    Data Classes: Instances are mutable, allowing modification of attributes after creation.
    Named Tuples: Are immutable, restricting modification of attributes.

Default Values:
    Data Classes: Support default values for attributes directly in the class definition.
    Named Tuples: Do not support default values easily, requiring additional methods.

Built-in Methods:
    Data Classes: Automatically generate methods like __repr__, __eq__, and allow adding custom methods.
    Named Tuples: Limited methods, and no support for adding custom methods.

Type Hints:
    Data Classes: Fully support type hints for attributes, improving code clarity and static type checking.
    Named Tuples: Do not natively support type hints.

Ease of Use:
    Data Classes: Provide a more intuitive and flexible way to define classes with less boilerplate.
    Named Tuples: Useful for simple data but less flexible for complex structures or behaviors.

'''