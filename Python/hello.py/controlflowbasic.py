#basic inheritence 

class Animal:
   def speak(self):
      return "some sound"


class Dog(Animal):
   def speak(self):
     return "woof"

class Cat(Animal):
   def speak(self):
     return "meow"

dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak())
