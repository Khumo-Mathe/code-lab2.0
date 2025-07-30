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

def animal_sound(animal: Animal):  # polymorphic function
   print(animal.speak()) # this will call the speak method of the specific animal type

animal_sound(Dog())
animal_sound(Cat())