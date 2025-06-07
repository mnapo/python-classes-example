class Animal:
  kind = "animal"
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  kind = "dog"
  def __init__(self, name):
    self.name = name
  def bark(self):
    print(self.name + " the " + self.kind + ": woooff!")

class Cat(Animal):
  kind = "cat"
  def __init__(self, name):
    self.name = name
  def meow(self):
    print(self.name + " the " + self.kind + ": meooow!")

doggy = Dog("Pipo")
kitten = Cat("Carlos")

doggy.bark()
kitten.meow()
