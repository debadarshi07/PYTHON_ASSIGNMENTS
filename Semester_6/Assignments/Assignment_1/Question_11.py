'''

Duck Typing -:
    Duck typing is a programming concept where an object's suitability for a specific purpose is determined by whether it implements the required methods and properties, rather than by checking its type or class. In Python, this allows flexibility in using objects with similar behaviors, even if they belong to different classes.

'''


class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep boop!"

def describe(animal):
    print(animal.speak())

dog = Dog()
robot = Robot()

describe(dog)
describe(robot)


'''

Duck typing allows the describe() function to work without checking the object's type because it only cares if the object has a speak() method. As long as the object can "speak" (i.e., has a speak() method), the function works, regardless of the object's class or type. This flexibility is key to duck typing, where behavior, not type, determines compatibility.

'''