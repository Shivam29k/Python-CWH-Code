# Create a class of pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class Animals:
    pass

class pets(Animals):
    pass

class dogs(pets):
    def bark(self):
        print("Bow bow!!")

d = dogs()
d.bark()