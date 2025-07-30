#basic polymorphism

class Duck:
    def quack(self):
        print("Quack!")

class Human:
    def quack(self):
        print("Quack! Quack!, like a duck")

def make_it_quack(thing):
    thing.quack()

make_it_quack(Duck())  # Prints "Quack!"
make_it_quack(Human())  # Prints "Quack! Quack!, like a duck"