'''

In Python, access control to class attributes is enforced using naming conventions rather than strict enforcement like some other programming languages. Python uses public, protected, and private attribute conventions, which are not strictly enforced by the language but rely on the programmer’s adherence to these naming conventions.

Public Attributes:
    -> Accessible from anywhere (inside and outside the class).
    -> No leading underscore (attribute).

Protected Attributes:
    -> Meant for internal use within the class and subclasses, not to be accessed directly outside the class.
    -> Single leading underscore (_attribute).

Private Attributes:
    -> Intended for internal use only within the class, and Python name-mangles them to make access harder outside the class.
    -> Double leading underscore (__attribute).
    -> Private attributes can be accessed through name mangling but should not be used outside the class.

'''